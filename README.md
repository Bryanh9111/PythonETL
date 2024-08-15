### Python ETL Project - Daily Data Ingestion and Dynamic Schema Handling

#### Project Overview
This Python project is designed to handle the daily ingestion of `.csv` and `.xlsx` files into a SQL Server database. The project includes features for dynamic table creation, schema modification, and data appending, making it ideal for evolving data structures and automated data processing.

#### Key Features

1. **Dynamic Table Creation and Alteration**:
   - Automatically creates tables in the SQL Server database based on the combined headers from multiple files.
   - If a new file contains additional columns not present in the existing table, the script dynamically alters the table to add the new columns.

2. **Daily Data Ingestion**:
   - Processes new files added to a specified directory daily and appends the data to the corresponding database tables.
   - Handles files with different schemas by ensuring missing columns are filled with `NULL` values where necessary.

3. **Error Handling and Logging**:
   - Logs all major actions, including data reading, table creation, schema alteration, and data insertion.
   - Provides error logging for any issues encountered during database operations.

4. **Automation-Ready**:
   - Designed for automated daily execution using tools like Windows Task Scheduler or Cron jobs on Linux/Mac.
   - Ensures the database is continuously updated with the latest data without manual intervention.

#### Project Structure

```
PythonDemo/
│
├── env/                  # Virtual environment directory (ignored in Git)
├── config/               # Configuration files for DB and file paths
│   ├── db_config.py
│   └── file_config.py
├── logs/                 # Log files
│   └── app.log
├── src/                  # Source code for the ETL process
│   ├── __init__.py
│   ├── data_reader.py
│   ├── data_writer.py
│   └── main.py
├── requirements.txt      # List of dependencies
├── .gitignore            # Files and directories to ignore in Git
└── README.md             # Project documentation
```

#### Usage Instructions

1. **Setup the Environment**:
   - Create a virtual environment and install the required dependencies:
     ```sh
     python -m venv env
     source env/bin/activate  # On Windows: .\env\Scripts\activate
     pip install -r requirements.txt
     ```

2. **Configure Database and File Paths**:
   - Update `config/db_config.py` with your SQL Server connection details.
   - Update `config/file_config.py` with the directory path for your data files and the table mappings.

3. **Run the Script**:
   - Run the script to process the files and update the database:
     ```sh
     python -m src.main
     ```

4. **Automate the Process**:
   - Schedule the script to run daily using a task scheduler (e.g., Windows Task Scheduler or Cron jobs).