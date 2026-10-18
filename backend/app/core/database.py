
import os

import psycopg
from dotenv import load_dotenv


load_dotenv(override=True)


def test_database_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL is missing. Check your .env file.")

    with psycopg.connect(database_url, connect_timeout=10) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user;")
            result = cursor.fetchone()

    print("Database connection successful.")
    print(f"Database: {result[0]}")
    print(f"User: {result[1]}")


if __name__ == "__main__":
    test_database_connection()
