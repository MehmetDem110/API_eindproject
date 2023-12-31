from sqlalchemy.orm import Session
import models
import schemas

def get_snacks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Snack).offset(skip).limit(limit).all()

def get_snack(db: Session, snack_id: int):
    return db.query(models.Snack).filter(models.Snack.id == snack_id).first()

def create_snack(db: Session, snack: schemas.SnackCreate):
    hashed_password = auth.get_password_hash(snack.password)
    db_snack = models.Snack(name=snack.name, description=snack.description)
    db.add(db_snack)
    db.commit()
    db.refresh(db_snack)
    return db_snack

def update_snack(db: Session, snack_id: int, snack: schemas.SnackUpdate):
    db_snack = db.query(models.Snack).filter(models.Snack.id == snack_id).first()
    if db_snack:
        db_snack.name = snack.name
        db_snack.description = snack.description
        db.commit()
        db.refresh(db_snack)
    return db_snack

def delete_snack(db: Session, snack_id: int):
    db_snack = db.query(models.Snack).filter(models.Snack.id == snack_id).first()
    if db_snack:
        db.delete(db_snack)
        db.commit()
    return db_snack

def search_snacks_by_name(db: Session, query: str):
    return db.query(models.Snack).filter(models.Snack.name.ilike(f"%{query}%")).all()
