import json
import menu_pb2
import os

with open("data_minified.json", "r") as f:
    data = json.load(f)

items = []
for item in data['menu']['items']:
    if item is None:
        wrapper = menu_pb2.MenuItemWrapper(is_null=True)
    else:
        menu_item = menu_pb2.MenuItem(
            id=item['id'],
            label=item.get('label', '')
        )
        wrapper = menu_pb2.MenuItemWrapper(is_null=False, item=menu_item)
    items.append(wrapper)

root = menu_pb2.RootData(
    menu=menu_pb2.Menu(
        header=data['menu']['header'],
        items=items
    )
)

with open("output.pb", "wb") as f:
    f.write(root.SerializeToString())

print(f"Protobuf:        {os.path.getsize('output.pb')} bytes")
print(f"JSON (minified): {os.path.getsize('data_minified.json')} bytes")


#==============For 100 data============================

data_100 = [data] * 100

# Serialize 100x
serialized_100 = b''
for d in data_100:
    items = []
    for item in d['menu']['items']:
        if item is None:
            wrapper = menu_pb2.MenuItemWrapper(is_null=True)
        else:
            menu_item = menu_pb2.MenuItem(
                id=item['id'],
                label=item.get('label', '')
            )
            wrapper = menu_pb2.MenuItemWrapper(is_null=False, item=menu_item)
        items.append(wrapper)

    root = menu_pb2.RootData(
        menu=menu_pb2.Menu(
            header=d['menu']['header'],
            items=items
        )
    )
    serialized_100 += root.SerializeToString()

with open("output_100.pb", "wb") as f:
    f.write(serialized_100)

print(f"Protobuf 100:    {os.path.getsize('output_100.pb')} bytes")