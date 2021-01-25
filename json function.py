import json
dict='{"Name":"Avinash","Department":"CSIT","Language":"Python",' \
     '"Intrasted Field":"Data Analytics","salary":"500"}'

# json_file=json.dumps(dict)
# print(type(json_file))
# print(json_file)
json_file=json.loads(dict)
print(type(json_file))
print(json_file)


# import json
# import requests
# json_file=json.loads('https://www.greatlearning.in/academy')
#  requests_file=requests.get('https://api.covid19india.org/csv/latest/raw_data1.json')
# print(requests_file.text)
# requests_file=requests.get('https://www.greatlearning.in/academy')
# print(requests_file.text)
#  print(requests_file.status_code)