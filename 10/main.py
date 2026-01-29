from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees", response_model=schemas.EmployeeOut)
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    employee = models.Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


@app.get("/employees")
def get_employees(
    skip: int = 0,
    limit: int = 10,
    name: str = "",
    db: Session = Depends(get_db)
):
    query = db.query(models.Employee)
    if name:
        query = query.filter(models.Employee.name.contains(name))
    return query.offset(skip).limit(limit).all()


@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in emp.dict().items():
        setattr(employee, key, value)

    db.commit()
    return {"message": "Employee updated successfully"}


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()
    return {"message": "Employee deleted successfully"}

@app.get("/")
def home():
    return {"message": "Employee CRUD API is running"}
