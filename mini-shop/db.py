"""
Connect to Redis DB on localhost, and seed the database
with products, using a pipeline.
"""

import redis

r = redis.Redis()

products = {
    "shirt:1": {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 5,
        "num_purchased": 0,
    },
    "shirt:2": {
        "color": "blue",
        "price": 29.99,
        "style": "baggy",
        "quantity": 6,
        "num_purchased": 0,
    },
    "shirt:3": {
        "color": "pink",
        "price": 15.99,
        "style": "tank",
        "quantity": 2,
        "num_purchased": 0,
    }
}

print(products)

# refresh db -> don't use in prod!!
r.flushdb()

# store all products into a hash in Redis
# each shirt is it's own hash, with key of id
pipe = r.pipeline()
for id, product in products.items():
    for field, value in product.items():
        pipe.hset(id, field, value)

pipe.execute()

# check that it worked in Redis CLI
# > hgetall shirt:1

# close connection to db
r.close()
