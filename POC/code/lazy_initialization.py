import time

class DatabaseConnection:
    def __init__(self, db_url):
        self.db_url = db_url
        self._connection = None

    @property
    def connection(self):
        if self._connection is None:
            print(f"Connecting to the database at {self.db_url}...")
            self._connection = self._create_connection()  # Simulating DB connection
        return self._connection

    def _create_connection(self):
        # Simulating an expensive database connection setup
        time.sleep(2)  # Simulate a delay in establishing a connection
        return f"Connection established to {self.db_url}"

# Usage
db = DatabaseConnection("localhost:5432/mydb")

# First access, will trigger the connection setup
print(db.connection)

# Second access, will return the cached connection
print(db.connection) 
