# app/database.py
from sqlmodel import SQLModel, Field, create_engine, Session

class Rule(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    rule_string: str

sqlite_url = "sqlite:///./rule_engine.db"
engine = create_engine(sqlite_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)
