import numpy as np
import pandas as pd

from data_generator.utils import read_sql, measure_func_time, generate_email_list


@measure_func_time
def personal_fields(set_field: set, size: int) -> pd.DataFrame:
    df_main = pd.DataFrame(columns=set_field)

    if set_field:
        set_field = list(set_field)
        df_main = pd.DataFrame(columns=set_field)
        gender_list = np.random.choice(np.array(['M', 'K']), size, True)
        df_main['gender'] = gender_list

    for column in set_field:
        if column in ['gender', 'email']:
            continue
        df = read_sql(column)
        gender_list = list(gender_list)
        men_column = df.query('gender == "M"')[column].tolist()
        women_column = df.query('gender == "K"')[column].tolist()

        column_list = [np.random.choice(men_column) if gender_list[i] == 'M'
                       else np.random.choice(women_column) for i in range(size)]
        df_main[column] = column_list
    if 'gender' not in set_field:
        df_main.drop(['gender'], axis=1)
    if 'email' in set_field:
        first_n, last_n = (df_main['first_name'], df_main['last_name'])
        email_list = generate_email_list(first_n, last_n)
        df_main['email'] = email_list

    return df_main
