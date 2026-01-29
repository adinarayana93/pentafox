from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    name: str = Field(..., pattern="^[A-Za-z ]+$")
    address: str
    salary: float = Field(gt=0)
    age: int = Field(gt=0)

class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True   # REQUIRED for Pydantic v2
