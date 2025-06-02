import json

# Define the data as a Python dictionary
data = {
    'name': 'Bob',
    'age': '25',
    'city': 'Los Angeles'
}

# Write data to a JSON file
with open('output.json', 'w') as f:
    json.dump(data, f)

with open('output.json') as f:
    output_data = json.load(f)
    print(output_data)

output_data['job'] = 'Engineer'

with open('modified_output.json','w') as f:
    json.dump(output_data, f)


with open('modified_output.json','r') as f:
    data = json.load(f)
    print(data)