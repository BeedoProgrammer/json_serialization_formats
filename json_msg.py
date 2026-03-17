import json
import msgpack
import os

# Load json file
with open("data.json", "r") as f:
    data = json.load(f)

# Pack to MessagePack bytes
packed_msg = msgpack.packb(data) 

# Save minified JSON (for size comparison only), no spaces
with open("data_minified.json", "w") as f:
    json.dump(data, f, separators=(',', ':'))

# Save packed data
with open("output.msgpack", "wb") as f:
    f.write(packed_msg)

# Compare sizes
print(f"MessagePack:     {os.path.getsize('output.msgpack')} bytes")
print(f"JSON (minified): {os.path.getsize('data_minified.json')} bytes")