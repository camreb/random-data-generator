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

    supported_fields = ['gender',
                        'first_name',
                        'last_name',
                        'job_title',
                        'email',
                        'city',
                        'voivodeship']

    fields = get_schema_args(supported_fields)
    size = get_size()

    data = personal_fields(fields, size)
    data.update(location_fields(fields, size))

    data_keys_to_del = [field_key for field_key in data.keys() if field_key not in fields]
    for key in data_keys_to_del:
        data.pop(key)

    data = pd.DataFrame(data).to_json(orient='records')
    data = loads(data)

    return jsonify({
        'success': True,
        'sample_data': data
    })
