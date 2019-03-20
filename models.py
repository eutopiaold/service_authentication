from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

from db_connection_info import connection_string

engine = create_engine(connection_string, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# necessary for querying
Base.query = db_session.query_property()

class User(Base):
    __table_args__ = {'schema' : 'auth'}
    __tablename__ = 'user'

    uid = Column(String, primary_key=True)
    full_name = Column(String)
    call_name = Column(String)
    email = Column(String)
    password = Column(String)

class Session(Base):
    __table_args__ = {'schema' : 'auth'}
    __tablename__ = 'session'

    uid = Column(String, primary_key=True)
    token = Column(String)
    created = Column(TIMESTAMP)
    timeout = Column(Interval)
