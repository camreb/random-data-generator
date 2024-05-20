import numpy as np
from sqlalchemy.sql import text

from data_generator.utils import measure_func_time
from data_generator import db


@measure_func_time
def location_fields(fields: list, size: int):
    data = {}
    if not fields:
        return data

    response = db.session.execute(text('SELECT city, voivodeship from locations;'))
    cities = []
    voivodeships = []
    for elem in response.all():
        cities.append(elem[0])
        voivodeships.append(elem[1])

    index_list = np.random.choice(list(range(len(cities))), size=size, replace=True)

    if 'city' in fields:
        data['city'] = [cities[i] for i in index_list]
    if 'voivodeship' in fields:
        data['voivodeship'] = [voivodeships[i] for i in index_list]
    return data
