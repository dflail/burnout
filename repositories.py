import os
import sqlite3


class LocalSQLiteRepository:

    def __init__(self, db_path: str = "data/dev.db"):
        self.db_path = db_path
        # Ensure the parent directory (e.g. 'data/') exists
        parent_dir = os.path.dirname(self.db_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        # Row factory lets you access columns by name (row['role']) instead of index (row[0])
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self, schema_path: str = "schema.sql"):
        """Reads schema.sql and creates the tables if they don't exist."""
        with open(schema_path, "r") as f:
            schema_sql = f.read()

        with self.get_connection() as conn:
            conn.executescript(schema_sql)