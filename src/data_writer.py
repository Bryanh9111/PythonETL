from sqlalchemy import create_engine, inspect, Table, Column, String, MetaData
from sqlalchemy.exc import SQLAlchemyError
from config.db_config import DB_CONFIG

def create_connection_string():
    return f"mssql+pyodbc://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['server']}/{DB_CONFIG['database']}?driver={DB_CONFIG['driver']}"

def table_exists(engine, table_name):
    inspector = inspect(engine)
    return inspector.has_table(table_name)

def get_existing_columns(engine, table_name):
    inspector = inspect(engine)
    return [column['name'] for column in inspector.get_columns(table_name)]

def add_new_columns(engine, table_name, new_columns):
    metadata = MetaData()
    table = Table(table_name, metadata, autoload_with=engine)
    for column_name in new_columns:
        new_column = Column(column_name, String, nullable=True)
        try:
            # Dynamically add new columns
            with engine.connect() as conn:
                conn.execute(table.append_column(new_column))
            print(f"Added column '{column_name}' to table '{table_name}'.")
        except SQLAlchemyError as e:
            print(f"Error adding column '{column_name}': {e}")

def write_to_db(df, table_name):
    connection_string = create_connection_string()
    engine = create_engine(connection_string)
    
    # Check if the table already exists
    if table_exists(engine, table_name):
        # Get existing columns in the table
        existing_columns = get_existing_columns(engine, table_name)
        
        # Find columns in df that are not in the existing table
        new_columns = [col for col in df.columns if col not in existing_columns]
        
        if new_columns:
            add_new_columns(engine, table_name, new_columns)
    
    else:
        # If the table doesn't exist, create it
        metadata = MetaData()
        columns_definitions = [Column(col, String, nullable=True) for col in df.columns]
        table = Table(table_name, metadata, *columns_definitions)
        try:
            metadata.create_all(engine)
            print(f"Table '{table_name}' created successfully with columns: {df.columns}")
        except SQLAlchemyError as e:
            print(f"Error occurred while creating table: {e}")
    
    # Insert data - Always append to the existing data
    df.to_sql(table_name, con=engine, if_exists='append', index=False)

