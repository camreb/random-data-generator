import numpy as np

from data_generator.utils import read_sql, measure_func_time, generate_email_list


@measure_func_time
def personal_fields(fields: list, size: int) -> dict:

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