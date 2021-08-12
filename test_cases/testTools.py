from models.setting import *
from models.subjectModels import *
from models.tagModels import *

def delete_all_subjects():
    session.query(Subject).delete()
    session.query(Staff).delete()
    session.query(StaffCorresp).delete()
    session.query(LectureSchedule).delete()
    session.query(ClassStyles).delete()
    session.query(FieldInfo).delete()
    session.query(TagCorresp).delete()

    session.commit()
