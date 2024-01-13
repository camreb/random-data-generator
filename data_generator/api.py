import pandas as pd
from flask import jsonify
from json import loads

from data_generator import app
from data_generator.utils import measure_func_time, get_schema_args, get_size
from data_generator.fields.personal import personal_fields
from data_generator.fields.location import location_fields


@measure_func_time
@app.route('/api/personal', methods=['POST'])
def randomize_data():

    data_types = {
        'personal_fields': ['gender', 'first_name', 'last_name', 'job_title', 'email'],
        'location_fields': ['city', 'voivodeship']
    }

    supported_fields = set().union(*data_types.values())

    fields = get_schema_args(list(supported_fields))
    size = get_size()
    df_main = pd.DataFrame(columns=fields)

    exec_dic = {
        'personal_fields': personal_fields,
        'location_fields': location_fields
    }

    for d_type, d_type_fields in data_types.items():
        intersec_fields = set(fields).intersection(d_type_fields)
        if intersec_fields:
            df = exec_dic[d_type](list(intersec_fields), size)
            df_main[list(intersec_fields)] = df[list(intersec_fields)]

    data = df_main[fields].to_json(orient='records')
    data = loads(data)
    return jsonify({
        'success': True,
        'data': data
    })
