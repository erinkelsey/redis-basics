"""
Shows how to save dates (must be converted to string), and how 
to add a Set.
"""

import redis
import datetime

r = redis.Redis()

stoday = datetime.date.today().isoformat()
visitors = {"homer", "bart", "marge"}

# convert date into string
# pass in a pointer to the values
r.sadd(stoday, *visitors)

# get all of the set values
values = r.smembers(stoday)

print(values)
# {b'bart', b'marge', b'homer'}

# get cardinality
card = r.scard(stoday)
print(card)
# 3
