import json
from jsonschema import validate, ValidationError

with open("user.json") as file:
    new = json.load(file)

with open("schema.json") as file2:
    schemaNew = json.load(file2)

try:
    validate(instance=new , schema=schemaNew)
    print("user profle is valid")
    
except:
    print("user profile is not valid")