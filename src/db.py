from typing import List

import psycopg2
from prefect import task
from prefect.logging import get_run_logger

from config import AppConfig
from config import read_config


@task(name="Ensure pipeline databases")
def prepare_pipeline_databases(conf: AppConfig, db_names_list: List[str]):
    """
    Creates given databases if they don't exist
    """
    logger = get_run_logger()

    for db_name in db_names_list:

        try:
            # Fetch conf
            postgres_db_uri = conf.database.construct_db_uri("postgres")

            # Connect to 'postgres' db to check if db exists
            con = psycopg2.connect(postgres_db_uri)
            con.autocommit = True
            cursor = con.cursor()
            cursor.execute(f"SELECT EXISTS(SELECT 1 FROM pg_database WHERE datname='{db_name}')")
            is_exist = cursor.fetchone()[0]

            # Create db
            if not is_exist:
                cursor.execute(f"CREATE DATABASE {db_name}")
                logger.info(f"Database {db_name} created and is ready for use.")

            cursor.close()
            con.close()

        except Exception:
            logger.exception(f"Error preparing database for {db_name}")
            raise

    logger.info(f"All databases are available.")


if __name__ == "__main__":
    db_names_list=["test_1","test_2"]

    # Fetch config
    conf = read_config()

    prepare_pipeline_databases(conf=conf, db_names_list=db_names_list)