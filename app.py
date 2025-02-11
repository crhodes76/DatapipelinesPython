from pipeline import run_pipeline
import urllib
import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    """Prompt the user for input using a GUI window."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    source = simpledialog.askstring("Input", "Enter the path of the input file:")
    table_name = simpledialog.askstring("Input", "Enter the table name to create:")

    return source, table_name

if __name__ == "__main__":
    source, table_name = get_user_input()
    destination = "customer_100_output.csv"
    server = 'localhost'
    database = 'PythonDatabase'
    username = 'power_user'
    password = 'password1234'

    # Connection string for pyodbc
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    # Convert to SQLAlchemy-compatible connection string
    params = urllib.parse.quote_plus(connection_string)
    sqlalchemy_connection_string = f'mssql+pyodbc:///?odbc_connect={params}'

    run_pipeline(source, destination, sqlalchemy_connection_string, table_name)
