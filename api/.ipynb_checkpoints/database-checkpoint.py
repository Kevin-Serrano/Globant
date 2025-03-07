{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31e89462-9be7-43cf-b4cd-a3dc00c4381d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyodbc\n",
    "\n",
    "def get_db_connection():\n",
    "    server = \"DESKTOP-8B57A0M\"\n",
    "    database = \"Test\"\n",
    "    conn_str = f\"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes\"\n",
    "    return pyodbc.connect(conn_str)\n"
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
