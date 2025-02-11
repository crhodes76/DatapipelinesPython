class PipelineConfig:
    def __init__(self, source_file: str, table_name: str, destination: str, server: str, database: str, username: str, password: str):
        self.source_file = source_file
        self.table_name = table_name
        self.destination = destination
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def get_sqlalchemy_connection_string(self) -> str:
        import urllib
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}'
        params = urllib.parse.quote_plus(connection_string)
        return f'mssql+pyodbc:///?odbc_connect={params}'
