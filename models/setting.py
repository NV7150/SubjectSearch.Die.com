from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f"postgresql://user:apbLJvZkNiE7HF5ALj3tgunR3Yx4BwYc@db:5432/db")
Base = declarative_base()
