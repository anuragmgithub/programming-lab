from dotenv import load_dotenv
import os 
from db.mysql_connector import MySQLConnector

load_dotenv()

def main():
    # Load environment variables
    host = os.getenv('DB_HOST', 'localhost')
    port = int(os.getenv('DB_PORT', 3306))
    user = os.getenv('DB_USER', 'root')
    password = os.getenv('DB_PASSWORD', '')
    database = os.getenv('DB_NAME', 'test_db')

    # Create a MySQLConnector instance
    db_connector = MySQLConnector(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    # Connect to the database
    db_connector.connect()

    # Close the connection
    db_connector.close()

    if __name__ == "__main__":
        main()