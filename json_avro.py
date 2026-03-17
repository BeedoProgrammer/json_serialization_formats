import json
import fastavro
import os

# Load json file
with open("data_minified.json", "r") as f:
    data = json.load(f)

schema = {
    "type": "record",
    "name": "RootData",
    "fields": [
        {
            "name": "menu",
            "type": {
                "type": "record",
                "name": "Menu",
                "fields": [
                    {"name": "header", "type": "string"},
                    {
                        "name": "items",
                        "type": {
                            "type": "array",
                            "items": [
                                "null",  # Allows the standalone nulls in your array
                                {
                                    "type": "record",
                                    "name": "MenuItem",
                                    "fields": [
                                        {"name": "id", "type": "string"},
                                        # Use None instead of null for Python syntax
                                        {"name": "label", "type": ["null", "string"], "default": None} 
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}

data_100 = [data] * 100

# Parse the schema using fastavro
parsed_schema = fastavro.parse_schema(schema)

# Write to an Avro file
with open("output.avro", "wb") as f:
    # Avro always writes a list of records, [data]
    fastavro.writer(f, parsed_schema, [data])

# Write 100x avro file
with open("output_100.avro", "wb") as f:
    fastavro.writer(f, parsed_schema, data_100)

print(f"Avro 100:        {os.path.getsize('output_100.avro')} bytes")
print(f"Avro:            {os.path.getsize('output.avro')} bytes")
print(f"JSON (minified): {os.path.getsize('data_minified.json')} bytes")