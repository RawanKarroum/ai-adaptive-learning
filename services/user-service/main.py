from fastapi import FastAPI, Depends
from models import User
from sqlalchemy.orm import Session
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create-user")
def create_user(email: str, password:str, role: str, db: Session = Depends(get_db)):
    new_user = User(email=email, password=password, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user.email}