from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal, engine, Base
import crud
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import auth

models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/snacks/", response_model=list[schemas.Snack])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_snack(db, skip=skip, limit=limit)
    return users

@app.get("/snacks/me", response_model=schemas.Snack)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user