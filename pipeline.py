import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError
from database_functions import read_data, process_data, write_data, create_table, insert_data

def run_pipeline(source: str, destination: str, db_connection_string: str, table_name: str):
    """Run the data pipeline."""
    data = read_data(source)
    processed_data = process_data(data)
    write_data(processed_data, destination)
    
    engine = create_engine(db_connection_string)
    create_table(engine, table_name, processed_data)
    insert_data(engine, table_name, processed_data)
