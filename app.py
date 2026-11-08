import config
import sys
from repositories import LocalSQLiteRepository

def manage_data():
    if config.APP_ENV == "development":
        repo = LocalSQLiteRepository(db_path=config.DB_PATH)
        sys.exit("TEST COMPLETE")
    else:
        sys.exit("Data management is currently only allowed in development environment.")
    


if __name__ == "__main__":
    manage_data()
