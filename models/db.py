# -*- coding: utf-8 -*-
# Implemented in case we want to use write back(To DB) approach later
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dataclasses import dataclass

from config import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USER
from log import logger
from contextlib import contextmanager

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=20, max_overflow=30)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        logger.error(f"[get_db] {err}")
    finally:
        db.close()


# call db connection without Dependency - for not route usage
@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        logger.error(f"[get_db_context] {err}")
    finally:
        db.close()
