"""
Show how to set key-value pairs.
Show how to get value for key.
"""

import redis

r = redis.Redis()

r.set('name', 'Homer')

print(r.get('name'))
# b'Homer'
