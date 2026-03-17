import json
import os
import sys
sys.path.insert(0, 'gen-py')

from menu import ttypes

with open("data_minified.json", "r") as f:
    data = json.load(f)

items = []
for item in data['menu']['items']:
    if item is None:
        pass  # skip nulls, thrift list can't hold them
    else:
        menu_item = ttypes.MenuItem(
            id=item['id'],
            label=item.get('label', None)
        )
        items.append(menu_item)

menu = ttypes.Menu(
    header=data['menu']['header'],
    items=items
)

root = ttypes.RootData(menu=menu)

# Serialize
from thrift.TSerialization import serialize
serialized = serialize(root)

with open("output.thrift", "wb") as f:
    f.write(serialized)

print(f"Thrift:          {os.path.getsize('output.thrift')} bytes")
print(f"JSON (minified): {os.path.getsize('data_minified.json')} bytes")