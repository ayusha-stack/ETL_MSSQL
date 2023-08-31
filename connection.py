import os
import pyodbc
from dotenv import load_dotenv

def create_connection():
    # Load environment variables from .env file
    load_dotenv()

    # Get database connection details from environment variables
    db_server = os.getenv("DB_SERVER")
    db_database = os.getenv("DB_DATABASE")
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_driver = os.getenv("DB_DRIVER")

    # Build the database connection string
    connection_string = (
        f"DRIVER={{{db_driver}}};"
        f"SERVER={db_server};"
        f"DATABASE={db_database};"
        f"UID={db_username};"
        f"PWD={db_password};"
    )

    try:
        connection = pyodbc.connect(connection_string)
        print("Database connection successful!")
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        raise

def main():
    # Create a database connection
    connection = create_connection()

    # Use the connection for your database operations

    # Close the connection when done
    connection.close()

if __name__ == "__main__":
    main()
