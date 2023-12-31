from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Adjust the path for the database file
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///sqlitedb/sqlitedata.db"  # Remove the leading dot in the path

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()