import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")
DB_PATH = os.getenv("DB_PATH", "data/dev.db")