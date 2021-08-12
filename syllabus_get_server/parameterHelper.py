import re

from models.enums import *

dict_faculty = {
    "総合政策・環境情報学部" : Faculty.UNDERGRADUATE,
    "政策・メディア研究科": Faculty.MASTER
}

def check_enum(t, s):
    return s in [v.value for k, v in t.__members__.items()]

def to_faculty(s):
    s = s.strip()
    if check_enum(Faculty, s):
        return Faculty(s)

# dict_subject_type_ug = {
#     "研究プロジェクト科目": SubjectType.RESEARCH_PROJECT,
#     "基盤科目-総合講座科目": SubjectType.GENERAL,
#     "基盤科目-言語コミュニケーション科目": SubjectType.LANG_COM,
#     "先端科目-総合政策系": SubjectType.POLICY_MAN,
#     "基盤科目-共通科目": SubjectType.SHARED,
#     "基盤科目-データサイエンス科目-データサイエンス１": SubjectType.DS1,
#     "基盤科目-データサイエンス科目-データサイエンス２": SubjectType.DS2,
#     "基盤科目-情報技術基礎科目": SubjectType.IT_BASE,
#     "基盤科目-ウェルネス科目": SubjectType.WELLNESS,
#     "先端科目-環境情報系": SubjectType.INFO_ENV,
#     "他学部等設置科目": SubjectType.GUEST,
#     "特設科目": SubjectType.SPECIAL,
#     "自由科目": SubjectType.FREE
# }
#
# dict_subject_type_ma = {
#     "自由科目": SubjectType.MA_FREE,
#     "プログラム科目-併設科目": SubjectType.MA_DOUBLE,
#     "研究支援科目−概念科目": SubjectType.MA_ABS,
#     "研究支援科目−先端研究科目": SubjectType.MA_FRONT,
#     "プログラム科目": SubjectType.MA_PROGRAM,
#     "プロジェクト科目": SubjectType.MA_PROJECT,
#     "特設科目": SubjectType.MA_SPECIAL
# }

def to_subject_type(s: str):
    s = s.split("-")[-1].strip()

    if check_enum(SubjectType, s):
        return SubjectType(s)

    return SubjectType.OTHER

def to_year_semester(s: str):
    split_s = s.split()

    if not len(split_s) == 2:
        return (0, Semester.OTHER)

    try:
        year = int(split_s[0].strip())
    except:
        return (0, Semester.OTHER)

    r_semester = split_s[1].strip()
    if "春" in r_semester:
        semester = Semester.SPRING
    elif "秋" in r_semester:
        semester = Semester.FALL
    else:
        semester = Semester.OTHER

    return (year, semester)

def to_credit(s: str):
    s  = re.sub('[^0-9]', '', s)
    if len(s) <= 0:
        return -1
    return int(s.strip())

def to_lang(s: str):
    s  = s.strip()
    if check_enum(Lang, s):
        return Lang(s)
    return Lang.UNDEFINED if len(s) == 0 else Lang.OTHER

def to_method(s: str):
    s = s.strip()
    if check_enum(ClassMethod, s):
        return ClassMethod(s)
    return ClassMethod.OTHER

def to_place(s: str):
    s = s.strip()
    if check_enum(Place, s):
        return Place(s)
    return Place.UNKNOWN

def form_subject_name(s: str):
    term = Term.FULL

    if "【" in s:
        split_s = s.split("【")

        if "前" in split_s[1] or "後" in split_s[1]:
            term = Term.FIRST if "前" in split_s[1] else Term.LATTER
            s = split_s[0]

    s = s.strip()
    return (s, term)

def to_giga(s: str):
    if not "対象" in s:
        return False
    return not("非" in s)

def to_day(s: str):
    s = s.strip()
    if check_enum(Day, s):
        return Day(s)
    return Day.OTHER

def to_period(s: str):
    s = re.sub('[^0-9]', '', s)
    if len(s) == 0:
        return Period.OTHER
    n = int(s)
    if check_enum(Period, n):
        return Period(n)
    return Period.OTHER

def to_style(s: str):
    s = s.strip()

    if check_enum(ClassStyle, s):
        return ClassStyle(s)

    return ClassStyle.OTHER