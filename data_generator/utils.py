import random

import pandas as pd
from anyascii import anyascii
from data_generator import db
from flask import request
from functools import wraps
from pathlib import Path
import time


def measure_func_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        x = func(*args, **kwargs)
        koniec = time.time()
        print(func.__name__, "wykonywała się", koniec - start, "sekund")
        return x
    return wrapper


def read_sql(table_name: str) -> pd.DataFrame:
    sql_engine = db.engine
    sql = {
        'first_name': 'first_names',
        'last_name': 'last_names',
        'job_title': 'job_titles',
        'location': 'locations'
    }
    try:
        df = pd.read_sql_table(sql[table_name], sql_engine)
    except Exception as exc:
        print("Unexpected error: {}".format(exc))
    else:
        return df


def get_schema_args(supp_fields: list) -> list:
    fields = request.args.get('fields')
    if fields:
        return [field for field in fields.split(',') if field in supp_fields]


def get_size():
    size = request.args.get('size')
    if size:
        return int(size)


def generate_email_list(fn_list, ln_list):
    data_path = Path(__name__).resolve().parent / 'data' / 'email.txt'
    with open(data_path, 'r') as file:
        email_domain = file.read().splitlines()
    email_list = [f'{anyascii(fn_list[i][0].lower())}.{anyascii(ln_list[i].lower())}@{random.choice(email_domain)}'
                  for i in range(len(fn_list))]

    return email_list
