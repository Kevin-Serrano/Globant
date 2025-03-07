{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e83a551-71f2-47c5-a60c-ce3152d88c83",
   "metadata": {},
   "outputs": [],
   "source": [
    "CREATE TABLE hired_employees (\n",
    "    id INT PRIMARY KEY,\n",
    "    full_name VARCHAR(255) NOT NULL,\n",
    "    col_datetime DATETIME NOT NULL,\n",
    "    department_id INT,\n",
    "    job_id INT\n",
    ");\n",
    "\n",
    "CREATE TABLE departments (\n",
    "    id INT PRIMARY KEY,\n",
    "    department VARCHAR(255) NOT NULL\n",
    ");\n",
    "\n",
    "CREATE TABLE jobs (\n",
    "    id INT PRIMARY KEY,\n",
    "    job VARCHAR(255) NOT NULL\n",
    ");\n"
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
