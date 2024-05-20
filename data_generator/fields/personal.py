import numpy as np
from sqlalchemy.sql import text

from data_generator.utils import measure_func_time, generate_email_list
from data_generator import db


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
    else:
        return data

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
