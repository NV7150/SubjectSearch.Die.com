import unittest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.setting import *
from models.subjectModels import *
from models.tagModels import *

from testParameterHelper import *
from testScrapper import *
from testDb import *
from testTools import *

if  (__name__=="__main__"):
    Base.metadata.create_all(bind=engine)
    unittest.main()
    delete_all_subjects()