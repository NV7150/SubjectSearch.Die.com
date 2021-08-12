import unittest
import glob

from models.subjectModels import *
from models.setting import *
from models.tagModels import *
from syllabus_get_server.scraper import *
from syllabus_get_server.dbRecorder import *

from testTools import *

class TestRecordDb(unittest.TestCase):
    def test_db_session(self):
        model = Staff()
        model.name = "テスト教員"
        session.add(model)
        session.commit()

        all_staffs = session.query(Staff).all()
        self.assertEqual(len(all_staffs), 1)
        session.commit()

        delete_all_subjects()

    def test_db_record(self):
        test_pathes = glob.glob(os.path.dirname(__file__) + "/testPage/testPage*.html")

        for path in test_pathes:
            with open(path) as f:
                html = f.read()

            info = analyze_page(html)

            record_db([info])

            all_subjects = session.query(Subject).all()

            self.assertEqual(len(all_subjects), 1)

            delete_all_subjects()

    def test_init_new(self):
        test_pathes = glob.glob(os.path.dirname(__file__) + "/testPage/testPage*.html")

        for path in test_pathes:
            with open(path) as f:
                html = f.read()

            info = analyze_page(html)

            info.init_new(session)
            session.commit()

            self.assertEqual(len(session.query(Subject).all()), 1)

            delete_all_subjects()