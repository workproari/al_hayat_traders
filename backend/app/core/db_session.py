import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is missing. Check your .env file.")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass


from sqlalchemy import text

if __name__ == "__main__":
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user;")
        )

        database_name, user_name = result.fetchone()

    print("SQLAlchemy connection successful.")
    print(f"Database: {database_name}")
    print(f"User: {user_name}")

