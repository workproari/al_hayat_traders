
import os
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from dotenv import load_dotenv

from backend.app.core.db_session import Base, engine


# Load environment variables from the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env", override=True)

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Register SQLAlchemy model metadata for future autogeneration.
target_metadata = Base.metadata

# Read the database URL from .env.
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError(
        "DATABASE_URL is missing. Check the project's .env file."
    )

# Configure Alembic at runtime without saving credentials in alembic.ini.
config.set_main_option(
    "sqlalchemy.url",
    database_url.replace("%", "%%"),
)


def run_migrations_offline() -> None:
    """Configure migrations without opening a database connection."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations through the existing SQLAlchemy engine."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
