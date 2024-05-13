import pandas as pd
from pathlib import Path
from sqlalchemy.sql import text

from data_generator import app, db


def load_csv_data(file_name: str) -> pd.DataFrame:
    csv_path = Path(__file__).resolve().parent.parent / 'sample_data' / file_name
    df = pd.read_csv(csv_path, sep=';', index_col=False)
    # df.reset_index(drop=True, inplace=True)
    return df


@app.cli.group()
def db_manage():
    """Database management commands"""
    pass


@db_manage.command()
def add_data():
    """Add sample_data to database"""

    sql_engine = db.engine
    try:
        data_csv = load_csv_data('first_name.csv')
        data_csv['gender'] = data_csv['gender'].astype('category')
        data_csv.to_sql('first_names', sql_engine, if_exists='append', index=False)

        data_csv = load_csv_data('last_name.csv')
        data_csv.to_sql('last_names', sql_engine, if_exists='append', index=False)

        data_csv = load_csv_data('job_title.csv')
        data_csv.to_sql('job_titles', sql_engine, if_exists='append', index=False)

        data_csv = load_csv_data('location.csv')
        data_csv.to_sql('locations', sql_engine, if_exists='append', index=False)

        print('Data has been successfully added to database')
    except ValueError as vx:
        print(vx)
    except Exception as exc:
        print("Unexpected error: {}".format(exc))


@db_manage.command()
def remove_data():
    """Remove all sample_data from the database"""
    try:
        db.session.execute(text('TRUNCATE TABLE first_names;'))
        db.session.execute(text('TRUNCATE TABLE last_names;'))

        db.session.commit()
        print('Data has been successfully removed from database')
    except Exception as exc:
        print("Unexpected error: {}".format(exc))
