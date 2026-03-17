import json
import os
import sys
from thrift.TSerialization import serialize

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
serialized = serialize(root)

with open("output.thrift", "wb") as f:
    f.write(serialized)

print(f"Thrift:          {os.path.getsize('output.thrift')} bytes")
print(f"JSON (minified): {os.path.getsize('data_minified.json')} bytes")



#==============For 100 data============================


data_100 = [data] * 100

# Serialize 100x
serialized_100 = b''
for d in data_100:
    items = []
    for item in d['menu']['items']:
        if item is None:
            pass
        else:
            menu_item = ttypes.MenuItem(
                id=item['id'],
                label=item.get('label', None)
            )
            items.append(menu_item)

    menu = ttypes.Menu(
        header=d['menu']['header'],
        items=items
    )
    root = ttypes.RootData(menu=menu)
    serialized_100 += serialize(root)

with open("output_100.thrift", "wb") as f:
    f.write(serialized_100)

print(f"Thrift 100:      {os.path.getsize('output_100.thrift')} bytes")