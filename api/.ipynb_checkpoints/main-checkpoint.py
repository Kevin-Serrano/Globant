{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6f2f379-502f-4c18-b0fc-db19c27521fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI, HTTPException\n",
    "from pydantic import BaseModel\n",
    "from typing import List, Optional\n",
    "import pyodbc\n",
    "import pandas as pd\n",
    "#from database import get_db_connection\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "# Modelo de datos\n",
    "class Employee(BaseModel):\n",
    "    id: int\n",
    "    full_name: str\n",
    "    col_datetime: str\n",
    "    department_id: Optional[int] = None\n",
    "    job_id: Optional[int] = None\n",
    "\n",
    "# Endpoint para insertar empleados\n",
    "@app.post(\"/add_employees/\")\n",
    "def add_employees(employees: List[Employee]):\n",
    "    conn = get_db_connection()\n",
    "    cursor = conn.cursor()\n",
    "    for emp in employees:\n",
    "        cursor.execute(\n",
    "            \"INSERT INTO dbo.hired_employees (id, full_name, col_datetime, department_id, job_id) VALUES (?, ?, ?, ?, ?)\",\n",
    "            emp.id, emp.full_name, emp.col_datetime, emp.department_id, emp.job_id\n",
    "        )\n",
    "    conn.commit()\n",
    "    return {\"message\": \"Empleados insertados exitosamente\"}\n",
    "\n",
    "# Endpoint para obtener empleados\n",
    "@app.get(\"/employees/\")\n",
    "def get_employees():\n",
    "    conn = get_db_connection()\n",
    "    cursor = conn.cursor()\n",
    "    cursor.execute(\"SELECT id, full_name, col_datetime, department_id, job_id FROM dbo.hired_employees\")\n",
    "    employees = cursor.fetchall()\n",
    "    return {\"employees\": employees}\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
