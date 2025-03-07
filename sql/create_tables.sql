CREATE TABLE hired_employees (
    id INT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    col_datetime DATETIME NOT NULL,
    department_id INT,
    job_id INT
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    department VARCHAR(255) NOT NULL
);

CREATE TABLE jobs (
    id INT PRIMARY KEY,
    job VARCHAR(255) NOT NULL
);
