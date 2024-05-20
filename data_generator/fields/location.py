import numpy as np
from sqlalchemy.sql import text

from data_generator.utils import measure_func_time
from data_generator import db


@measure_func_time
def location_fields(set_field: list, size: int):

    response = db.session.execute(text('SELECT city, voivodeship from locations;'))
    cities = []
    voivodeships = []
    for elem in response.all():
        cities.append(elem[0])
        voivodeships.append(elem[1])

    index_list = np.random.choice(list(range(len(cities))), size=size, replace=True)

    data = {}
    if 'city' in set_field:
        data['city'] = [cities[i] for i in index_list]
    if 'voivodeship' in set_field:
        data['voivodeship'] = [voivodeships[i] for i in index_list]
    return data
