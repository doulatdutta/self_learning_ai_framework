import sqlite3

class Database:
    def __init__(self, db_file="data/database.db"):
        """
        Database class for handling SQLite database interactions.

        :param db_file: Path to the SQLite database file.
        """
        self.db_file = db_file
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, columns):
        """
        Creates a new table in the database.

        :param table_name: Name of the table.
        :param columns: A dictionary of column names and types (e.g., {"id": "INTEGER", "name": "TEXT"}).
        :return: None
        """
        column_definitions = ", ".join([f"{col} {col_type}" for col, col_type in columns.items()])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print(f"Table {table_name} created or already exists.")

    def insert_data(self, table_name, data):
        """
        Inserts data into a table.

        :param table_name: Name of the table.
        :param data: A dictionary of column-value pairs to insert (e.g., {"id": 1, "name": "John"}).
        :return: None
        """
        columns = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(insert_query, tuple(data.values()))
        self.connection.commit()
        print(f"Data inserted into {table_name}.")

    def query_data(self, table_name, columns="*", where_clause=None):
        """
        Queries data from a table.

        :param table_name: Name of the table.
        :param columns: Columns to select (default is '*').
        :param where_clause: Optional WHERE clause for filtering results.
        :return: List of results.
        """
        query = f"SELECT {columns} FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        """
        Closes the database connection.

        :return: None
        """
        self.connection.close()
