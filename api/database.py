import pyodbc

def get_db_connection():
    server = "DESKTOP-8B57A0M"  # Reemplázalo con tu servidor
    database = "Test"
    conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    return pyodbc.connect(conn_str)
