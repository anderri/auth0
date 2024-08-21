import json

def nested_dict(flat_dict):
    result = {}
    for key, value in flat_dict.items():
        keys = key.split('.')
        d = result
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value
    return result

# Read the flat JSON objects from the file
with open('input.json', 'r') as file:
    flat_json_objects = [json.loads(line) for line in file]

# Convert each flat object to a nested one
nested_json_objects = [nested_dict(flat_obj) for flat_obj in flat_json_objects]

# Write the nested JSON objects to a new file as an array
with open('output.json', 'w') as file:
    json.dump(nested_json_objects, file, indent=2)
