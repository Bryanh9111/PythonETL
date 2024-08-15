import logging
from .data_reader import get_combined_headers, read_data_with_combined_headers
from .data_writer import write_to_db
from config.file_config import FILES, FILE_PATH

# Set up logging
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    # Group files by table
    tables = {}
    for file_config in FILES:
        table_name = file_config['table_name']
        if table_name not in tables:
            tables[table_name] = []
        tables[table_name].append(file_config['file_name'])
    
    for table_name, file_list in tables.items():
        try:
            # Get combined headers
            combined_headers = get_combined_headers(file_list)
            
            # Process each file and insert into the database
            for file_name in file_list:
                data = read_data_with_combined_headers(file_name, combined_headers)
                logging.info(f"Data read successfully from {file_name}")
                
                # Write data to database (with table creation or alteration)
                write_to_db(data, table_name)
                logging.info(f"Data written successfully to table {table_name}")

        except Exception as e:
            logging.error(f"An error occurred while processing table {table_name}: {e}")
            print(f"An error occurred while processing table {table_name}: {e}")

if __name__ == '__main__':
    main()
