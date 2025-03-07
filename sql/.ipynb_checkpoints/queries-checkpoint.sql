{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8a8b300-357c-4b2e-a2f9-32ade06428f0",
   "metadata": {},
   "outputs": [],
   "source": [
    "-- Empleados contratados por trimestre en 2021\n",
    "SELECT \n",
    "    DATEPART(QUARTER, col_datetime) AS trimestre,\n",
    "    COUNT(*) AS total_empleados\n",
    "FROM dbo.hired_employees\n",
    "WHERE YEAR(col_datetime) = 2021\n",
    "GROUP BY DATEPART(QUARTER, col_datetime)\n",
    "ORDER BY trimestre;\n",
    "\n",
    "-- Departamentos con más contrataciones que el promedio\n",
    "SELECT department_id, COUNT(*) AS total_contrataciones\n",
    "FROM dbo.hired_employees\n",
    "GROUP BY department_id\n",
    "HAVING COUNT(*) > (SELECT AVG(total_contrataciones) FROM (\n",
    "    SELECT COUNT(*) AS total_contrataciones FROM dbo.hired_employees GROUP BY department_id\n",
    ") AS subquery);\n"
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
