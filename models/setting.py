from sqlalchemy import *
from sqlalchemy.orm import *
import os
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

path = f"postgresql://" \
       + os.environ["POSTGRES_USER"] + ":" \
       + os.environ["PGPASSWORD"] +"@db:5432/" + os.environ["POSTGRES_DB"]

engine = create_engine(path)
Base = declarative_base()

session_maker = sessionmaker(bind=engine, autoflush=False)
session = scoped_session(session_maker)
Base.query = session.query_property()

# @contextmanager
# def get_session():
#        session = Session()
#        try:
#               yield session
#               session.commit()
#        except:
#               session.rollback()
#        finally:
#               session.close()
