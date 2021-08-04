from sqlalchemy import *
from sqlalchemy.orm import *
import os
from sqlalchemy.ext.declarative import declarative_base

path = f"postgresql://" \
       + os.environ["POSTGRES_USER"] + ":" \
       + os.environ["PGPASSWORD"] +"@db:5432/" + os.environ["POSTGRES_DB"]

engine = create_engine(path)
Base = declarative_base()
