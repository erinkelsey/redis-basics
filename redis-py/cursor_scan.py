"""
Show how to use cursor and scan to iterate through keys.
Show how to use pipelines, where you can group commands
together, so they are sent to DB all at once.  This can
reduce network cost and latency.
"""

import redis

# connect and reset db
r = redis.Redis("localhost")
r.flushdb()

# seed data for db
pipe = r.pipeline()
for i in range(30):
    key = f"check:{i}"
    value = f"hello:{i}"
    pipe.set(key, value)

pipe.execute()


# scan keys in db
cursor = 0
while True:
    cursor, value = r.scan(cursor, match="check*")
    print(f'cursor: {cursor}\nvalue: {value}')
    if cursor == 0:
        break

# example output
# cursor: 14
# value: [b'check:15', b'check:4', b'check:16', b'check:19', b'check:12', b'check:0', b'check:10', b'check:9', b'check:18', b'check:25']
# cursor: 19
# value: [b'check:28', b'check:22', b'check:5', b'check:3', b'check:24', b'check:21', b'check:20', b'check:17', b'check:29', b'check:13']
# cursor: 31
# value: [b'check:23', b'check:14', b'check:26', b'check:11', b'check:8', b'check:27', b'check:7', b'check:6', b'check:1', b'check:2']
# cursor: 0
# value: []

# close connection
r.close()
