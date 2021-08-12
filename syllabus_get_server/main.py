import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from models.setting import Base, engine
import models.subjectModels
import models.tagModels

from syllabus_get_server.scraper import *
from syllabus_get_server.dbRecorder import *

def main():
    print("executing syllabus_get_server...", flush=True)
    Base.metadata.create_all(bind=engine)
    infos = scrap_all()
    record_db(infos)

if (__name__  == "__main__"):
    main()
