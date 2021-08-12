from typing import List
from sqlalchemy.orm import *

from models.setting import session
from models.subjectModels import *
from models.tagModels import *
from .analyzeInfos import *

def record_db(infos: List[DbInfos]):
    print("recording to db...", flush=True)

    print("set models unavailable....", flush=True)
    flag_unavailable(session)

    print("recording infos...", flush=True)
    for info in infos:
        legacy: Subject = Subject.query.filter(Subject.subject_name==info.subject.subject_name).first()
        if legacy:
            delete_all_relations(session, legacy.id)
            info.update_model(legacy,session)
            legacy.is_unavailable = False
        else:
            info.init_new(session)

        session.commit()

    print("done", flush=True)

def delete_all_relations(session, id):
    session.query(FieldInfo).filter(FieldInfo.subject_id==id).delete()
    session.query(LectureSchedule).filter(LectureSchedule.subject_id==id).delete()
    session.query(TagCorresp).filter(TagCorresp.subject_id==id).delete()
    session.query(StaffCorresp).filter(StaffCorresp.subject_id==id).delete()
    session.query(ClassStyles).filter(ClassStyles.subject_id==id).delete()

def flag_unavailable(session):
    subjects = session.query(Subject).all()
    for subject in subjects:
        subject.is_unavailable  = True