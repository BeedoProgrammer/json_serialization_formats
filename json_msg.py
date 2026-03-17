import json
import msgpack
import os

# Load json file
with open("data.json", "r") as f:
    data = json.load(f)

data_100 = [data] * 100

# Pack to MessagePack bytes
packed_msg = msgpack.packb(data)
packed_msg_100 = msgpack.packb(data_100) 

# Save minified JSON (for size comparison only), no spaces
with open("data_minified.json", "w") as f:
    json.dump(data, f, separators=(',', ':'))

# Save minified JSON 100x
with open("data_minified_100.json", "w") as f:
    json.dump(data_100, f, separators=(',', ':'))

# Save packed data
with open("output.msgpack", "wb") as f:
    f.write(packed_msg)

with open("output_100.msgpack", "wb") as f:
    f.write(packed_msg_100)

# Compare sizes
print(f"MessagePack:     {os.path.getsize('output.msgpack')} bytes")
print(f"MessagePack 100:     {os.path.getsize('output_100.msgpack')} bytes")
print(f"JSON 100 (minified): {os.path.getsize('data_minified_100.json')} bytes")
print(f"JSON (minified): {os.path.getsize('data_minified.json')} bytes")