-- Empleados contratados por trimestre en 2021
SELECT 
    DATEPART(QUARTER, col_datetime) AS trimestre,
    COUNT(*) AS total_empleados
FROM dbo.hired_employees
WHERE YEAR(col_datetime) = 2021
GROUP BY DATEPART(QUARTER, col_datetime)
ORDER BY trimestre;

-- Departamentos con más contrataciones que el promedio
SELECT department_id, COUNT(*) AS total_contrataciones
FROM dbo.hired_employees
GROUP BY department_id
HAVING COUNT(*) > (SELECT AVG(total_contrataciones) FROM (
    SELECT COUNT(*) AS total_contrataciones FROM dbo.hired_employees GROUP BY department_id
) AS subquery);
