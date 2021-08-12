from bs4 import BeautifulSoup
from time import sleep
import urllib.request
import datetime

from .analyzeInfos import *

BACK_YEAR = 0

def scrap_all():
    print("start scrapping", flush=True)

    print("get indexes...", flush=True)
    index_htmls = get_indexes()
    detail_pages = []

    print("analyze indexes...", flush=True)
    for index_html in index_htmls:
        urls = analyze_index_url(index_html)
        detail_pages.extend(get_detail_pages(urls))

    print("analyze pages...", flush=True)
    page_infos =  []
    for detail_page in detail_pages:
        page_infos.append(analyze_page(detail_page))

    print("done", flush=True)
    return page_infos

def get_indexes():
    htmls = []

    for year_offset in range(BACK_YEAR + 1):
        search_year = datetime.date.today().year - year_offset
        page = 1

        while True:
            html = get_index_page(page, search_year)

            if not html == -1:
                htmls.append(html)
            else: 
                break

            page += 1

    return htmls

def get_index_page(page, year):
    url = "https://syllabus.sfc.keio.ac.jp/courses?&page=" + str(page) + "&search%5Byear%5D=" + str(year)

    with urllib.request.urlopen(url) as response:
        html = response.read()

    sleep(1)

    if not "<li>" in str(html):
        return -1

    return html

def analyze_index_url(index_page):
    bs = BeautifulSoup(index_page, "html.parser")
    list_elements = bs.find_all("li")
    result_url = []

    for element in list_elements:
        try:
            url = element.select(".detail-btn-wrapper")[0].select("a")[0]["href"]
        except:
            continue

        if not url:
            continue

        url = "https://syllabus.sfc.keio.ac.jp" + url
        url = url.strip()
        result_url.append(url)

    return result_url

def get_detail_pages(urls):
    result_analyze = []

    for url in urls:
        with urllib.request.urlopen(url) as response:
            r_html = response.read()
        result_analyze.append(r_html)
        sleep(1)

    return result_analyze


def analyze_page(html):
    bs = BeautifulSoup(html, "html.parser")

    main = bs.body.contents[3].div

    title = main.h2.find('span', class_="title").text

    class_info_sections = main.find('div', class_="class-info").find_all("div", class_="subject")

    year_semester = ""
    sort_code = ""

    field_infos = []
    for info_section in class_info_sections:
        contents = info_section.find_all("dl", class_="row")
        faculty = str(contents[0].dd.text).strip()
        field_credit = contents[2].find_all("dd")
        field = str(field_credit[0].text).strip()
        credit = str(field_credit[1].text).strip()

        sort_code = str(contents[1].find_all("dd")[0].text)

        field_infos.append(FieldInfoBuilder(faculty,field,credit))

    syllabus_infos = main.find('div', class_="syllabus-info").find_all("dl", class_="row")

    schedules, staffs, methods = [[] for i in range(3)]
    style, lang, place, giga = ["" for i in range(4)]

    for syllabus_info in syllabus_infos:
        name_info = str(syllabus_info.dt.text).strip()
        if name_info == "開講年度・学期":
            year_semester = syllabus_info.dd.text.strip()
        elif name_info == "曜日・時限":
            day_periods = str(syllabus_info.dd.text).split(",")
            schedules = []
            if not len(day_periods) == 2:
                schedules.append(LectureScheduleBuilder("",""))
                continue

            for day_period in day_periods:
                d_p_split = day_period.split()
                schedules.append(LectureScheduleBuilder(str(d_p_split[0]).strip(), str(d_p_split[1]).strip()))
        elif name_info == "授業教員名":
            staffs_str = syllabus_info.dd.text.split(",")
            staffs_str = [str(s).replace('\u3000', ' ').strip() for s in staffs_str]
            staffs = []
            for staff_str in staffs_str:
                staffs.append(StaffBuilder(staff_str))
        elif name_info == "実施形態":
            style = str(syllabus_info.dd.text).strip()
        elif name_info == "授業で使う言語":
            lang = str(syllabus_info.dd.text).strip()
        elif name_info == "開講場所":
            place = str(syllabus_info.dd.text).strip()
        elif name_info == "授業形態":
            class_method_strs = str(syllabus_info.dd.text).split(",")
            methods = []
            for c_m_str in class_method_strs:
                methods.append(ClassStyleBuilder(str(c_m_str).strip()))
        elif name_info == "GIGAサティフィケート対象":
            giga = str(syllabus_info.dd.text).strip()

    about = str(main.find('dl', class_="detail-info").dd.p.text)
    about = re.sub("<br.+/>", "", about)
    about = about.replace("<br>", "\n").replace("\"", "").strip()

    subject = SubjectInfoBuilder(sort_code,title,style,lang,year_semester,place,giga,about)

    return DbInfos(subject, field_infos, schedules, staffs, methods)