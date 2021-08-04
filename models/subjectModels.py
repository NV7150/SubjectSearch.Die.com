import enum

from models.setting import Base
from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class SubjectType(enum.Enum):
    RESEARCH_PROJECT = "研究プロジェクト科目"
    GENERAL = "総合講座科目"
    LANG_COM = "言語コミュニケーション科目"
    POLICY_MAN  = "先端科目総合科目系"
    SHARED = "共通科目"
    DS1 = "データサイエンス科目1"
    DS2 = "データサイエンス科目2"
    WELLNESS = "ウェルネス科目"
    INFO_ENV = "先端科目環境情報系"
    GUEST = "他学部等設置科目"
    SPECIAL = "特設科目"
    FREE = "自由科目"

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

class Style(enum.Enum):
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

class ClassMethod(enum.Enum):
    GROUP_WORK = "グループワーク"
    LECTURE = "講義"
    REMOTE = "遠隔あり"
    PRACTICE = "実習・演習"

class TargetStudent(enum.Enum):
    UNDERGRADUATE = "環境情報学部・総合政策学部"
    MASTER = "政策・メディア研究科"

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sort_id = Column(String(64))
    subject_name = Column(String(128), nullable=False)
    style = Column(Enum(Style))
    lang = Column(Enum(Lang))
    year = Column(Integer)
    semester = Column(Enum(Semester))
    place = Column(Enum(Place))
    is_giga = Column(Boolean)
    about = Column(String(1024))

    staffs_arr = relationship("StaffCorresp", backref="subjects")
    lecture_schedule = relationship("LectureSchedule", backref="subjects")
    methods = relationship("ClassMethods", backref="subjects")
    field_info = relationship("FieldInfo", backref="subjects")
    tags_arr = relationship("TagCorresp", backref="subjects")

class Staff(Base):
    __tablename__ = 'staffs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    subjects_arr = relationship("StaffCorresp", backref="staffs")

class StaffCorresp(Base):
    __tablename__= 'staffCorresps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    staff_id = Column(Integer, ForeignKey("staffs.id", onupdate="CASCADE", ondelete="CASCADE"))

class LectureSchedule(Base):
    __tablename__= 'schedules'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    day = Column(Enum(Day))
    period = Column(Enum(Period))

class ClassMethods(Base):
    __tablename__= 'methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    method = Column(Enum(ClassMethod), nullable=False)

class FieldInfo(Base):
    __tablename__= 'fieldInfos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    target = Column(Enum(TargetStudent), nullable=False)
    type = Column(Enum(SubjectType), nullable=False)
    credit = Column(Integer, nullable=False)

class TagCorresp(Base):
    __tablename__= 'tagCorresps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    tag_id = Column(Integer, ForeignKey("tags.id", onupdate="CASCADE", ondelete="CASCADE"))
