#This Code connect to mySQL database based on connection parameters in .env file and fetches data from the table entered by user
# Make sure to install mysql-connector-python package and python-dotenv package before running this code
# access .env file for database connection parameters like DB_HOST, DB_USER, DB_PASSWORD, DB_NAME and .venv file for virtual environment setup 

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()  
def connect_fetch_data(table_name):
    try:
        # Connect to the database using credentials from .env file
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            print("Connected to the database")
            cursor = connection.cursor()
            # Fetch data from the specified table
            cursor.execute(f"SELECT * FROM {table_name} limit 10")  # Limiting to 10 records for demonstration 
            records = cursor.fetchall()
            print(f"Data from {table_name}:")
            for row in records:
                print(row)
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
# Example usage:
if __name__ == "__main__":
    table_name = input("Enter the table name to fetch data from: ")
    connect_fetch_data(table_name) 
    
        