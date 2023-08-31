import os
import pyodbc
from dotenv import load_dotenv
from connection import create_connection  # Import the create_connection function from your connection file

def execute_sql_file(file_path, cursor):
    with open(file_path, 'r') as file:
        sql_code = file.read()
        cursor.execute(sql_code)
        cursor.connection.commit()
def main():
    # Create a database connection
    connection = create_connection()

    # Replace with the actual file paths
    create_table_file = r'raw\table1.sql'
    insert_data_file = r'raw\table1.sql'


    cursor = connection.cursor()

    # Execute SQL files
    execute_sql_file(create_table_file, cursor)
    execute_sql_file(insert_data_file, cursor)

    # Close the connection when done
    connection.close()

if __name__ == "__main__":
    main()
