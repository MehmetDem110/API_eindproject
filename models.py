from sqlalchemy import Column, Integer, String
from database import Base

class Snack(Base):
    __tablename__ = "snacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)