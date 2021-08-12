import enum

class Faculty(enum.Enum):
    UNDERGRADUATE = "総合政策・環境情報学部"
    MASTER = "政策・メディア研究科"

class SubjectType(enum.Enum):
    #学部
    #基盤科目
    GENERAL = "総合講座科目"
    LANG_COM = "言語コミュニケーション科目"
    SHARED = "共通科目"
    DS1 = "データサイエンス１"
    DS2 = "データサイエンス２"
    IT_BASE = "情報技術基礎科目"
    WELLNESS = "ウェルネス科目"

    #先端科目
    POLICY_MAN  = "総合政策系"
    INFO_ENV = "環境情報系"

    #その他
    RESEARCH_PROJECT = "研究プロジェクト科目"
    GUEST = "他学部等設置科目"

    #研究科
    #研究支援科目
    MA_ABS = "概念科目"
    MA_FRONT = "先端研究科目"

    #プログラム科目
    MA_PROGRAM = "プログラム科目"
    MA_DOUBLE = "併設科目"

    #その他
    MA_PROJECT = "プロジェクト科目"

    #共通
    SPECIAL = "特設科目"
    FREE = "自由科目"
    OTHER = "その他"

class Term(enum.Enum):
    FULL = "通期"
    FIRST = "前半"
    LATTER = "後半"
    OTHER = "その他"

class Day(enum.Enum):
    MON = '月'
    TUE = '火'
    WED = '水'
    THU = '木'
    FRI = '金'
    SAT = '土'
    OTHER = 'その他'

class ClassMethod(enum.Enum):
    ON_CAMPUS = 'オンキャンパス'
    LIVE = 'オンライン（ライブ）'
    ON_DEMAND = 'オンライン（オンデマンド）'
    OTHER = "その他"

class Lang(enum.Enum):
    JAPANESE = "日本語"
    ENGLISH = "英語"
    CHINESE = "中国語"
    KOREAN = "朝鮮語"
    MALAY_INDONESIAN = "マレーインドネシア語"
    SPANISH = "スペイン語"
    RUSSIAN = "ロシア語"
    ITALIAN = "イタリア語"
    FRENCH = "フランス語"
    ARABIC = "アラビア語"
    OTHER = "その他"
    UNDEFINED = ""

class Semester(enum.Enum):
    SPRING = "春"
    FALL = "秋"
    OTHER = "その他"

class Place(enum.Enum):
    SFC = "SFC"
    TTCK = "TTCK"
    OTHER = "その他"
    UNKNOWN = ""

class Period(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    OTHER = "その他"

class ClassStyle(enum.Enum):
    GROUP_WORK = "グループワーク"
    LECTURE = "講義"
    REMOTE = "遠隔あり"
    PRACTICE = "実習・演習"
    OTHER = ""