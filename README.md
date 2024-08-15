### Summary of Current Features

Designed to handle daily data processing tasks involving `.csv` and `.xlsx` files that are placed into a specific directory. The project includes the following key features:

#### 1. **Dynamic Table Creation and Alteration**
- **Combine Headers**: The script dynamically combines headers from multiple files (e.g., `file1.csv` and `file2.csv`) to determine the full set of columns required for the corresponding database table.
- **Table Creation**: If a table does not exist in the SQL Server database, it is created with the combined headers as columns.
- **Table Alteration**: If new columns are detected in the daily files that were not previously in the table, the script automatically alters the table to add these new columns.

#### 2. **Daily Data Ingestion**
- **File Processing**: The script is designed to run daily, processing new files that are added to the directory. It reads data from these files and prepares them for insertion into the database.
- **Appending Data**: The script appends the new data to the existing records in the database tables. It ensures that data from each file is added without overwriting any previous data.

#### 3. **Error Handling and Logging**
- **Logging**: The script logs all major actions, including data reading, table creation, table alteration, and data insertion. Errors encountered during the process are also logged for review.
- **Error Handling**: The script includes error handling to manage issues that may arise during database operations, such as SQL errors or data format inconsistencies.

#### 4. **Automation**
- **Scheduled Execution**: The script is designed to be scheduled using tools like Windows Task Scheduler or Cron jobs on Linux/Mac. This allows for automated daily execution without manual intervention.
- **File Management**: The script processes the files in a specified directory, ensuring that any new files added daily are included in the data ingestion process.

### Use Case
- **File1 & File2**: These files share a subset of columns, with `file2` potentially having more columns than `file1`. The script ensures that both files are ingested into the same table, handling missing columns from `file1` by filling them with `NULL`.
- **File3 & File4**: Similarly, these files are ingested into another table, with the same dynamic handling of columns.

This setup is particularly useful for scenarios where data structures may evolve over time, and the database needs to adapt dynamically to accommodate new data fields. The automation ensures that the system can run reliably without manual oversight.