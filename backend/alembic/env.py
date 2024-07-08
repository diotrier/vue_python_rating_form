from __future__ import with_statement
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import AsyncEngine
from alembic import context
from app.models import Base

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_online():
    configuration = config.get_section(config.config_ini_section)
    connectable = AsyncEngine(
        engine_from_config(
            configuration,
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
            future=True,
        )
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=None,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
