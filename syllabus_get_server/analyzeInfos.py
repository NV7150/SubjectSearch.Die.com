from typing import List
from sqlalchemy.orm import *

from .parameterHelper import *
from models.subjectModels import *


class FieldInfoBuilder:
    def __init__(self, r_faculty, r_field, r_credit):
        self.faculty = to_faculty(r_faculty)
        self.field  = to_subject_type(r_field)
        self.credit  = to_credit(r_credit)

    def to_model(self):
        model = FieldInfo()

        model = self.copy_model(model)

        return model

    def copy_model(self, model: FieldInfo):
        model.credit = self.credit
        model.type = self.field
        model.target = self.faculty
        return model


class SubjectInfoBuilder:
    def __init__(self, sort_id, subject_name, r_method, r_lang, r_year_semester, r_place, r_giga, about):
        self.sort_id = sort_id
        (self.subject_name, self.term) = form_subject_name(subject_name)
        self.about = about
        self.method = to_method(r_method)
        self.place = to_place(r_place)
        self.lang = to_lang(r_lang)
        (self.year, self.semester) = to_year_semester(r_year_semester)
        self.is_giga = to_giga(r_giga)

    def to_model(self):
        model = Subject()

        model = self.copy_model(model)

        return model

    def copy_model(self, model):
        model.method = self.method
        model.subject_name = self.subject_name
        model.about = self.about
        model.sort_id = self.sort_id
        model.term = self.term
        model.place = self.place
        model.is_giga = self.is_giga
        model.lang = self.lang
        model.year = self.year
        model.semester = self.semester

        return model


class LectureScheduleBuilder:
    def __init__(self, r_day, r_period):
        self.day = to_day(r_day)
        self.period = to_period(r_period)

    def to_model(self):
        model = LectureSchedule()

        model = self.copy_model(model)

        return model

    def copy_model(self, model: LectureSchedule):
        model.day = self.day
        model.period = self.period
        return model

class ClassStyleBuilder:
    def __init__(self, r_style):
        self.style = to_style(r_style)

    def to_model(self):
        model = ClassStyles()

        return self.copy_model(model)

    def copy_model(self, model: ClassStyles):
        model.style = self.style
        return model

class StaffBuilder:
    def __init__(self, r_staff):
        self.staff_name = r_staff

    def to_model(self, session):
        staff_model = session.query(Staff).filter(Staff.name == self.staff_name).first()

        if staff_model:
            return StaffCorresp(staff_id=staff_model.id)

        model = Staff()

        model = self.copy_model(model)
        session.add(model)

        corresp = StaffCorresp(staff_id=model.id)

        return corresp

    def copy_model(self, model: Staff):
        model.name = self.staff_name
        return model

class DbInfos:
    def __init__(self
                 , subject: SubjectInfoBuilder
                 , field_infos: List[FieldInfoBuilder]
                 , schedules: List[LectureScheduleBuilder]
                 , staff_infos: List[StaffBuilder]
                 , style: List[ClassStyleBuilder]):
        self.subject = subject
        self.fieldInfos = field_infos
        self.schedules = schedules
        self.staff_infos = staff_infos
        self.styles = style

    def init_new(self, session):
        subject = self.subject.to_model()
        session.add(subject)

        for field in self.fieldInfos:
            f_model = field.to_model()
            f_model.subject_id = subject.id
            session.add(f_model)

        self.update_model(subject, session)

    def update_model(self, subject: Subject, session: Session):
        for schedule in self.schedules:
            s_model = schedule.to_model()
            s_model.subject_id = subject.id
            session.add(s_model)

        for method in self.styles:
            m_model = method.to_model()
            m_model.subject_id = subject.id
            session.add(m_model)

        for staff in self.staff_infos:
            corresp = staff.to_model(session)
            corresp.subject_id = subject.id
            session.add(corresp)




