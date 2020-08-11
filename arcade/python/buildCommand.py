import json

def set_default(obj):
    if type(obj) == str:
        return ""
    if type(obj) == int or type(obj) == float:
        return 0
    if type(obj) == list:
        return []
    for k, v in obj.items():
        print(k, v)
        obj[k] = set_default(v)
    return obj

def buildCommand(jsonFile):
    data = json.loads(jsonFile)
    data = set_default(data)
    return json.dumps(data)
