from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine, Base
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/snacks/", response_model=schemas.Snack)
def create_snack(snack: schemas.SnackCreate, db: Session = Depends(get_db)):
    return crud.create_snack(db=db, snack=snack)

@app.get("/snacks/", response_model=list[schemas.Snack])
def read_snacks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    snacks = crud.get_snacks(db, skip=skip, limit=limit)
    return snacks

@app.get("/snacks/{snack_id}", response_model=schemas.Snack)
def read_snack(snack_id: int, db: Session = Depends(get_db)):
    db_snack = crud.get_snack(db, snack_id=snack_id)
    if db_snack is None:
        raise HTTPException(status_code=404, detail="Snack not found")
    return db_snack

@app.put("/snacks/{snack_id}", response_model=schemas.Snack)
def update_snack(snack_id: int, snack: schemas.SnackUpdate, db: Session = Depends(get_db)):
    updated_snack = crud.update_snack(db, snack_id, snack)
    if updated_snack is None:
        raise HTTPException(status_code=404, detail="Snack not found")
    return updated_snack

@app.delete("/snacks/{snack_id}", response_model=schemas.Snack)
def delete_snack(snack_id: int, db: Session = Depends(get_db)):
    deleted_snack = crud.delete_snack(db, snack_id)
    if deleted_snack is None:
        raise HTTPException(status_code=404, detail="Snack not found")
    return deleted_snack

@app.get("/snacks/search/", response_model=list[schemas.Snack])
def search_snacks(query: str = None, db: Session = Depends(get_db)):
    if query is None or query.strip() == "":
        raise HTTPException(status_code=400, detail="Query parameter 'query' is required")
    snacks = crud.search_snacks_by_name(db, query)
    return snacks
