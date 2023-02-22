import json

data = '{"firstName": "Fethi", "lastName": "Cekinmez"}'

data_json_format = json.loads(data)

print(data_json_format["firstName"])

dictionary = {
    "firstName": "Fethi",
    "email": "fekinmez@gmail.com"
}

dictionary_json_format = json.dumps(dictionary)

print(dictionary)