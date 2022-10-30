import json

import requests


class Client(object):
    def __init__(self, d, bench_type, metric, batch_id, batch_unit, batch_size,analysis_parameter):
        self.d = d
        self.bench_type = bench_type
        self.metric = metric
        self.batch_id = batch_id
        self.batch_unit = batch_unit
        self.batch_size = batch_size
        self.analysis_parameter = analysis_parameter


def serialize(Client):
    return {"id": Client.d,
            "bench_type": Client.bench_type,
            "metric": Client.metric,
            "batch_id": Client.batch_id,
            "batch_unit": Client.batch_unit,
            "batch_size": Client.batch_size,
            "analysis_parameter":Client.analysis_parameter
            }



d = input('Enter Request For Workload (RFW) ID:')
bench_type_name = input(
    'Enter one of the following:\n 1. DVD\n 2.NDBench\n')
batch_type = input("Enter batch type \n1.testing \n 2.training \n")
metric = input('choose one of the metrics from the following:\n'
               '1. CPUUtilization_Average\n 2. NetworkIn_Average\n 3. NetworkOut_Average\n'
               ' 4. MemoryUtilization_Average\n')
batch_id = input('Enter the Batch Id (from which batch you want the data to start from) in integer: ')
batch_unit = input('Enter the number of samples you want in one batch in integer: ')
batch_size = input('Enter the number of batches to be returned in integer: ')
analysis_parameter = input('Enter the analysis you want : \n''1. 10p\n''2. 50p \n''3. 95p\n' '4. 99p\n''4. avg\n''5. std \n''6. max\n''7. min\n ')

bench_type = bench_type_name+"-"+batch_type
req_data = Client(d, bench_type, metric, batch_id, batch_unit, batch_size, analysis_parameter)

json_req = json.dumps(req_data, default=serialize)
response = requests.get("http://127.0.0.1:5000/get_batches?", json=serialize(req_data))

# response = requests.get("http://35.183.44.180:5000/get_batches?", json=serialize(req_data))



if response.status_code == 200:
    print(" rfw_id: ", response.json()['rfw_id'])
    print(" last_batch_id: ", response.json()['last_batch_id'])
    print(" Samples Requested: ", response.json()['samples'])
    print(" analysis: ", response.json()['analysis'])



