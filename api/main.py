from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import pyodbc
import pandas as pd
from database import get_db_connection

app = FastAPI()

# Modelo de datos
class Employee(BaseModel):
    id: int
    full_name: str
    col_datetime: str
    department_id: Optional[int] = None
    job_id: Optional[int] = None

# Endpoint para insertar empleados
@app.post("/add_employees/")
def add_employees(employees: List[Employee]):
    conn = get_db_connection()
    cursor = conn.cursor()
    for emp in employees:
        cursor.execute(
            "INSERT INTO dbo.hired_employees (id, full_name, col_datetime, department_id, job_id) VALUES (?, ?, ?, ?, ?)",
            emp.id, emp.full_name, emp.col_datetime, emp.department_id, emp.job_id
        )
    conn.commit()
    return {"message": "Empleados insertados exitosamente"}

# Endpoint para obtener empleados
@app.get("/employees/")
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, full_name, col_datetime, department_id, job_id FROM dbo.hired_employees")
    employees = [{"id": row[0], "full_name": row[1], "col_datetime": row[2], "department_id": row[3], "job_id": row[4]} for row in cursor.fetchall()]
    return {"employees": employees}
