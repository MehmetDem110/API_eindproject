from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    locations = relationship("Location", back_populates="user")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    locations = relationship("Location", back_populates="item")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    statecode = Column(String)

    # Foreign keys
    user_id = Column(Integer, ForeignKey("users.id"))  # Add this line
    item_id = Column(Integer, ForeignKey("items.id"))  # Add this line

    user = relationship("User", back_populates="locations")
    item = relationship("Item", back_populates="locations")