import logging

import redis

r = redis.Redis()
logging.basicConfig()


class OutOfStockError(Exception):
    """
    Raised when product is out of stock.

    Args:
        Exception: expection for product out of stock
    """


def get_keys(pattern, position=0):
    """
    Returns all of the keys that match pattern.

    Args:
        pattern (string): pattern to match keys to.
        position (int, optional): position to start scan. Defaults to 0.

    Returns:
        [bytes]: list of the keys that matched pattern, as bytes
    """
    products = []
    while True:
        position, value = r.scan(cursor=position, match=pattern)
        products += value
        if position == 0:
            break

    return products


def buy_item(product_id):
    """
    Buy a product. Decreases the quantity of product, and increases
    the num_purchased of product.

    Args:
        product_id (string): key for the product
    """
    pipe = r.pipeline()

    while True:  # retry if there is an error
        try:
            pipe.watch(product_id)  # watch item

            num_left = r.hget(product_id, "quantity")

            if num_left > b"0":
                pipe.multi()  # start transaction
                pipe.hincrby(product_id, "quantity", -1)
                pipe.hincrby(product_id, "num_purchased", 1)
                pipe.execute()
                break  # success -> dont need to repeat
            else:
                pipe.unwatch()
                raise OutOfStockError(
                    f"Sorry {product_id} is out of stock."
                )
        except redis.WatchError:
            logging.warning("Error in watched product, retrying buy.")


# test above functions
shirts = get_keys("shirt:*")
print(shirts)

buy_item(shirts[0])
