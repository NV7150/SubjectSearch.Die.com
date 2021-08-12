import unittest

from syllabus_get_server.parameterHelper import *

class TestParamHelper(unittest.TestCase):
    def test_faculty(self):
        self.assertEqual(to_faculty("総合政策・環境情報学部"), Faculty.UNDERGRADUATE)
        self.assertEqual(to_faculty("政策・メディア研究科"), Faculty.MASTER)
        self.assertEqual(to_faculty("     政策・メディア研究科     \n"), Faculty.MASTER)

    def test_subject_type(self):
        self.assertEqual(to_subject_type("研究プロジェクト科目"), SubjectType.RESEARCH_PROJECT)
        self.assertEqual(to_subject_type("基盤科目-総合講座科目"), SubjectType.GENERAL)
        self.assertEqual(to_subject_type("基盤科目-言語コミュニケーション科目"), SubjectType.LANG_COM)
        self.assertEqual(to_subject_type("先端科目-総合政策系"), SubjectType.POLICY_MAN)
        self.assertEqual(to_subject_type("基盤科目-共通科目"), SubjectType.SHARED)
        self.assertEqual(to_subject_type("基盤科目-データサイエンス科目-データサイエンス１"), SubjectType.DS1)
        self.assertEqual(to_subject_type("基盤科目-データサイエンス科目-データサイエンス２"), SubjectType.DS2)
        self.assertEqual(to_subject_type("基盤科目-情報技術基礎科目"), SubjectType.IT_BASE)
        self.assertEqual(to_subject_type("基盤科目-ウェルネス科目"), SubjectType.WELLNESS)
        self.assertEqual(to_subject_type("先端科目-環境情報系"), SubjectType.INFO_ENV)
        self.assertEqual(to_subject_type("他学部等設置科目"), SubjectType.GUEST)
        self.assertEqual(to_subject_type("特設科目"), SubjectType.SPECIAL)
        self.assertEqual(to_subject_type("自由科目"), SubjectType.FREE)

        self.assertEqual(to_subject_type("プログラム科目-併設科目"), SubjectType.MA_DOUBLE)
        self.assertEqual(to_subject_type("研究支援科目-概念科目"), SubjectType.MA_ABS)
        self.assertEqual(to_subject_type("研究支援科目-先端研究科目"), SubjectType.MA_FRONT)
        self.assertEqual(to_subject_type("プログラム科目"), SubjectType.MA_PROGRAM)
        self.assertEqual(to_subject_type("プロジェクト科目"), SubjectType.MA_PROJECT)

        self.assertEqual(to_subject_type("      他学部等設置科目      \n"), SubjectType.GUEST)

    def test_year_semester(self):
        self.assertEqual(to_year_semester("2021 春学期"), (2021, Semester.SPRING))
        self.assertEqual(to_year_semester("2020 秋学期"), (2020, Semester.FALL))
        self.assertEqual(to_year_semester("あ　あ"), (0, Semester.OTHER))
        self.assertEqual(to_year_semester(""), (0, Semester.OTHER))
        self.assertEqual(to_year_semester("あ あ a a"), (0, Semester.OTHER))

    def test_credit(self):
        self.assertEqual(to_credit("2単位"), 2)
        self.assertEqual(to_credit("10単位"), 10)
        self.assertEqual(to_credit("0単位"), 0)
        self.assertEqual(to_credit("単位"), -1)
        self.assertEqual(to_credit("     2単位　　　\n"), 2)

    def test_lang(self):
        self.assertEqual(to_lang("日本語"), Lang.JAPANESE)
        self.assertEqual(to_lang("英語"), Lang.ENGLISH)
        self.assertEqual(to_lang("中国語"), Lang.CHINESE)
        self.assertEqual(to_lang("朝鮮語"), Lang.KOREAN)
        self.assertEqual(to_lang("マレーインドネシア語"), Lang.MALAY_INDONESIAN)
        self.assertEqual(to_lang("スペイン語"), Lang.SPANISH)
        self.assertEqual(to_lang("ロシア語"), Lang.RUSSIAN)
        self.assertEqual(to_lang("イタリア語"), Lang.ITALIAN)
        self.assertEqual(to_lang("フランス語"), Lang.FRENCH)
        self.assertEqual(to_lang("アラビア語"), Lang.ARABIC)
        self.assertEqual(to_lang("その他"), Lang.OTHER)
        self.assertEqual(to_lang(""), Lang.UNDEFINED)

        self.assertEqual(to_lang("スワヒリ語"), Lang.OTHER)
        self.assertEqual(to_lang("    日本語　　\n"), Lang.JAPANESE)

    def test_method(self):
        self.assertEqual(to_method("オンキャンパス"), ClassMethod.ON_CAMPUS)
        self.assertEqual(to_method("オンライン（ライブ）"), ClassMethod.LIVE)
        self.assertEqual(to_method("オンライン（オンデマンド）"), ClassMethod.ON_DEMAND)
        self.assertEqual(to_method("その他"), ClassMethod.OTHER)
        self.assertEqual(to_method(""), ClassMethod.OTHER)

        self.assertEqual(to_method("   オンライン（オンデマンド）    　　\n"), ClassMethod.ON_DEMAND)

    def test_place(self):
        self.assertEqual(to_place("SFC"), Place.SFC)
        self.assertEqual(to_place("TTCK"), Place.TTCK)
        self.assertEqual(to_place("その他"), Place.OTHER)
        self.assertEqual(to_place(""), Place.UNKNOWN)

        self.assertEqual(to_place("    SFC     　　\n"), Place.SFC)


    def test_subject_name(self):
        self.assertTupleEqual(form_subject_name("総合政策学 【学期前半】"), ("総合政策学", Term.FIRST))
        self.assertTupleEqual(form_subject_name("心身ウェルネス 【学期後半】(グループH：クラス23〜26)"), ("心身ウェルネス", Term.LATTER))
        self.assertTupleEqual(form_subject_name("スペイン語スキル A"), ("スペイン語スキル A", Term.FULL))

        self.assertTupleEqual(form_subject_name("    総合政策学 【学期前半】　　\n"), ("総合政策学", Term.FIRST))
        self.assertTupleEqual(form_subject_name("　　スペイン語スキル A　　　 \n"), ("スペイン語スキル A", Term.FULL))

    def test_giga(self):
        self.assertEqual(to_giga("対象"), True)
        self.assertEqual(to_giga("非対象"), False)

        self.assertEqual(to_giga(""), False)

    def test_day(self):
        self.assertEqual(to_day("月"),Day.MON)
        self.assertEqual(to_day("火"),Day.TUE)
        self.assertEqual(to_day("水"),Day.WED)
        self.assertEqual(to_day("木"),Day.THU)
        self.assertEqual(to_day("金"),Day.FRI)
        self.assertEqual(to_day("土"),Day.SAT)
        self.assertEqual(to_day("日"),Day.OTHER)
        self.assertEqual(to_day(""),Day.OTHER)
        self.assertEqual(to_day("    月     \n"),Day.MON)

    def test_period(self):
        self.assertEqual(to_period("1限"), Period.ONE)
        self.assertEqual(to_period("2限"), Period.TWO)
        self.assertEqual(to_period("3限"), Period.THREE)
        self.assertEqual(to_period("4限"), Period.FOUR)
        self.assertEqual(to_period("5限"), Period.FIVE)
        self.assertEqual(to_period("6限"), Period.SIX)
        self.assertEqual(to_period("7限"), Period.SEVEN)

        self.assertEqual(to_period("8限"), Period.OTHER)
        self.assertEqual(to_period(""), Period.OTHER)
        self.assertEqual(to_period("　　　1限     \n"), Period.ONE)

    def test_style(self):
        self.assertEqual(to_style("グループワーク"), ClassStyle.GROUP_WORK)
        self.assertEqual(to_style("講義"), ClassStyle.LECTURE)
        self.assertEqual(to_style("遠隔あり"), ClassStyle.REMOTE)
        self.assertEqual(to_style("実習・演習"), ClassStyle.PRACTICE)

        self.assertEqual(to_style(""), ClassStyle.OTHER)
        self.assertEqual(to_style("ああああああ"), ClassStyle.OTHER)

        self.assertEqual(to_style("　　　グループワーク    \n"), ClassStyle.GROUP_WORK)

