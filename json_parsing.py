import json

string_as_json_format = '{"answer": "Hello, World!"}'
obj = json.loads(string_as_json_format)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"There is no key {key} in JSON")