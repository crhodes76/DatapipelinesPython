import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError

def read_data(source: str) -> pd.DataFrame:
    """Read data from a source."""
    return pd.read_csv(source)

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Process the data."""
    # Example processing: remove rows with missing values
    return df.dropna()

def write_data(df: pd.DataFrame, destination: str):
    """Write data to a destination."""
    df.to_csv(destination, index=False)
    
def check_create_table_permission(engine) -> bool:
    """Check if the user has permission to create a table."""
    try:
        with engine.connect() as connection:
            connection.execute(text("CREATE TABLE PermissionCheck (id INT)"))
            connection.execute(text("DROP TABLE PermissionCheck"))
        return True
    except ProgrammingError:
        return False

def create_table(engine, table_name: str, df: pd.DataFrame):
    """Create a new table in the database."""
    if check_create_table_permission(engine):
        df.head(0).to_sql(table_name, engine, index=False, if_exists='replace')
    else:
        print(f"Permission denied: Cannot create table '{table_name}' in the database.")
        

def insert_data(engine, table_name: str, df: pd.DataFrame):
    """Insert data into the table."""
    df.to_sql(table_name, engine, index=False, if_exists='append')
    
