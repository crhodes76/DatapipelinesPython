from pipeline import run_pipeline
from models import PipelineConfig
import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    """Prompt the user for input using a GUI window."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    source_file = simpledialog.askstring("Input", "Enter the path of the input file:")
    table_name = simpledialog.askstring("Input", "Enter the table name to create:")

    return source_file, table_name

if __name__ == "__main__":
    source_file, table_name = get_user_input()
    destination = "customer_100_output.csv"
    server = 'localhost'
    database = 'PythonDatabase'
    username = 'power_user'
    password = 'password1234'

    config = PipelineConfig(source_file, table_name, destination, server, database, username, password)
    run_pipeline(config.source_file, config.destination, config.get_sqlalchemy_connection_string(), config.table_name)
