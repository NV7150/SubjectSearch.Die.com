import unittest
import glob
import json
import os
from bs4 import BeautifulSoup

from syllabus_get_server.scraper import *

class ScrapTest(unittest.TestCase):
    def test_index_link(self):
        with open( os.path.dirname(__file__) + "/testPage/index_testcase") as f:
            def_urls = f.readlines()
        def_urls = [url.strip() for url in def_urls]
        with open(os.path.dirname(__file__)+ "/testPage/testIndexPage.html") as f:
            html = f.read()
        self.maxDiff = None
        self.assertCountEqual(def_urls, analyze_index_url(html))

    def test_scrapping(self):
        test_pathes = glob.glob(os.path.dirname(__file__) + "/testPage/testPage*.html")

        for path in test_pathes:
            with open(path) as f:
                test_page = analyze_page(f.read())

            txt_path = path.replace(".html", ".json")
            with open(txt_path) as f:
                ans = json.loads(f.read())

            self.assertEqual(test_page.subject.subject_name, ans["title"])
            self.assertEqual(test_page.subject.method.value, ans["method"])
            self.assertEqual(test_page.subject.lang.value, ans["lang"])
            self.assertEqual(test_page.subject.place.value, ans["place"])
            self.assertEqual(test_page.subject.term.value, ans["term"])
            self.assertEqual(test_page.subject.is_giga, ans["giga"])
            self.assertEqual(test_page.subject.about.replace("\n",""), ans["about"].replace("\n",""))
            self.assertEqual(test_page.subject.year, ans["year"])
            self.assertEqual(test_page.subject.semester.value, ans["semester"])
            self.assertEqual(test_page.subject.sort_id, ans["sort"])

            staffs = []
            for staff_info in test_page.staff_infos:
                staffs.append(staff_info.staff_name)
            self.assertCountEqual(staffs, ans["staffs"])

            styles = []
            for style in test_page.styles:
                styles.append(style.style.value)
            self.assertCountEqual(styles, ans["style"])

            schedules = []
            for schedule in test_page.schedules:
                schedules.append({"day": schedule.day.value, "period": schedule.period.value})
            self.assertEqual(schedules, ans["day_period"])

            fields = []
            for field in test_page.fieldInfos:
                fields.append({
                    "faculty": field.faculty.value,
                    "field": field.field.value,
                    "credit": field.credit
                })
            self.assertCountEqual(fields, ans["info"])