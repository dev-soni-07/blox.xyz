import json
from decimal import Decimal

def parse_json(json_string):
    try:
        result = json.loads(json_string, parse_float=Decimal, parse_int=Decimal)
        return result
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {str(e)}"

json_string = '{"name": "Dev Soni", "age": 20, "balance": 10000.50}'
print("Valid JSON example:")
result = parse_json(json_string)
print(result)

invalid_json_string = '{"name": "Dev Soni", "age": 20, "balance": 10000.50'
print("\nInvalid JSON example:")
result = parse_json(invalid_json_string)
print(result)