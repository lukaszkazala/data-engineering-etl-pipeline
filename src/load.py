import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


def get_database_engine() -> Engine:
    """
    Create SQLAlchemy engine for PostgreSQL connection.

    Returns:
        Engine: SQLAlchemy database engine.
    """
    load_dotenv()

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set.")

    return create_engine(database_url)


def load_to_postgres(df: pd.DataFrame, table_name: str) -> None:
    """
    Load DataFrame into PostgreSQL table.

    Parameters:
        df (pd.DataFrame): DataFrame to load.
        table_name (str): Target table name in PostgreSQL.

    Returns:
        None
    """
    engine = get_database_engine()

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into table: {table_name}")