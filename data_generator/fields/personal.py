import numpy as np
from sqlalchemy.sql import text

from data_generator.utils import read_sql, measure_func_time, generate_email_list
from data_generator import db


@measure_func_time
def personal_fields2(fields: list, size: int) -> dict:

    if fields:
        data = {'gender': list(np.random.choice(np.array(['M', 'K']), size, True))}

    if 'email' in fields:
        if 'first_name' not in fields:
            fields.append('first_name')
        if 'last_name' not in fields:
            fields.append('last_name')

    for column in fields:
        if column in ['gender', 'email']:
            continue
        try:
            df = read_sql(column)
            men_column = df.query('gender == "M"')[column].tolist()
            women_column = df.query('gender == "K"')[column].tolist()
            column_list = [np.random.choice(men_column) if data['gender'][i] == 'M'
                           else np.random.choice(women_column) for i in range(size)]
            data[column] = column_list
        except Exception as exc:
            print("Unexpected error: {}".format(exc))

    if 'email' in fields:
        data['email'] = generate_email_list(data['first_name'], data['last_name'])

    return data



@measure_func_time
def personal_fields(fields: list, size: int) -> dict:
    tables = {
        'first_name': 'first_names',
        'last_name': 'last_names',
        'job_title': 'job_titles',
        'location': 'locations'
    }
    data = {}

    if fields:
        data = {'gender': list(np.random.choice(np.array(['M', 'K']), size, True))}

    if 'email' in fields:
        if 'first_name' not in fields:
            fields.append('first_name')
        if 'last_name' not in fields:
            fields.append('last_name')

    for column in fields:
        if column in ['gender', 'email']:
            continue
        try:
            field_list = []
            gender_list = []
            response = db.session.execute(text(f'SELECT * from {tables[column]};'))
            for elem in response.all():
                field_list.append(elem[1])
                gender_list.append(elem[2])
            men = [field_list[i] for i in range(len(field_list)) if gender_list[i] == 'M']
            women = [field_list[i] for i in range(len(field_list)) if gender_list[i] == 'K']

            data[column] = [np.random.choice(men)
                            if data['gender'][i] == 'M'
                            else np.random.choice(women)
                            for i in range(size)]
        except Exception as exc:
            print("Unexpected error: {}".format(exc))

    if 'email' in fields:
        data['email'] = generate_email_list(data['first_name'], data['last_name'])

    return data


@measure_func_time
def personal_fields3(fields: list, size: int) -> dict:
    tables = {
        'first_name': 'first_names',
        'last_name': 'last_names',
        'job_title': 'job_titles',
        'location': 'locations'
    }
    data = {}

    if fields:
        data = {'gender': list(np.random.choice(np.array(['M', 'K']), size, True))}

    if 'email' in fields:
        if 'first_name' not in fields:
            fields.append('first_name')
        if 'last_name' not in fields:
            fields.append('last_name')

    for column in fields:
        if column in ['gender', 'email']:
            continue
        try:
            response = db.session.execute(text(f'SELECT * from {tables[column]};')).all()
            # response -> list of tuples
            men = [response[i][1] for i in range(len(response)) if response[i][2] == 'M']
            women = [response[i][1] for i in range(len(response)) if response[i][2] == 'K']

            data[column] = [np.random.choice(men)
                            if data['gender'][i] == 'M'
                            else np.random.choice(women)
                            for i in range(size)]
        except Exception as exc:
            print("Unexpected error: {}".format(exc))

    if 'email' in fields:
        data['email'] = generate_email_list(data['first_name'], data['last_name'])

    return data
