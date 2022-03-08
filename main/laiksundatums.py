import datetime

print(datetime.datetime.now())

print(datetime.datetime(2020,7,12))

"""
%A - diena
%d - meneša diena
%j - diena gada
%B - mēnesis
"""
import json

a = datetime.datetime.now()
perv_laiks = a.isoformat()
json_a = json.dumps(perv_laiks)
print(json_a)