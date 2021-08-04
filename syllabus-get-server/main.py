from models.setting import Base, engine
import models.subjectModels
import models.tagModels

def main():
    Base.metadata.create_all(bind=engine)
    print("aaaaa")

if (__name__  == "__main__"):
    main()
