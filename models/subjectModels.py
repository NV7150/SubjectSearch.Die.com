from models.setting import Base
from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models.enums import *

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sort_id = Column(String(64))
    subject_name = Column(String(128), nullable=False)
    method = Column(Enum(ClassMethod))
    lang = Column(Enum(Lang))
    year = Column(Integer)
    semester = Column(Enum(Semester))
    place = Column(Enum(Place))
    is_giga = Column(Boolean)
    term = Column(Enum(Term))
    about = Column(String(4096))
    is_unavailable = Column(Boolean, default=False)

    staffs_arr = relationship("StaffCorresp", backref="subjects")
    lecture_schedule = relationship("LectureSchedule", backref="subjects")
    styles = relationship("ClassStyles", backref="subjects")
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

class ClassStyles(Base):
    __tablename__= 'styles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    style = Column(Enum(ClassStyle), nullable=False)

class FieldInfo(Base):
    __tablename__= 'fieldInfos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    target = Column(Enum(Faculty))
    type = Column(Enum(SubjectType))
    credit = Column(Integer)

class TagCorresp(Base):
    __tablename__= 'tagCorresps'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_id = Column(Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE"))
    tag_id = Column(Integer, ForeignKey("tags.id", onupdate="CASCADE", ondelete="CASCADE"))
