# Redis Commands

## Start and Stop Commands

### Start Redis Server

    $ redis-server

### Start Redis CLI

    $ redis-cli

Check that it is connected:

    > ping [message]

### Shutdown Redis Server

    > shutdown [NOSAVE | SAVE]

NOSAVE: Redis will not save data to disk
SAVE: Redis will save data to disk

## Basic Key Commands

### Set Key-Value Pair

    > set [key] [value]

### Get Value for Key

    > get [key]

### Show All Keys in DB

    > keys *

### Delete Key(s)

    > del [key1] ... [key2] [key3]

### Check if Key(s) Exist

    > exists [key1] ... [key2]

### Set Expiry for Key

Seconds:

    > set [key] [value] ex [seconds]

Milliseconds:

    > set [key] [value] ex [milliseconds]

Set expiry for existing key in seconds:

    > expire [key] [seconds]

Set expiry for existing key in milliseconds:

    > pexpire [key] [milliseconds]

### Check Time to Live (Until Key Expires)

Seconds:

    > ttl [key]

Milliseconds:

    > pttl [key]

NOTE: return value is -2 when key is expired, and can no longer use get command to retrieve value of key (it is deleted).

NOTE: return value is -1 when the key does not have an expiry date.

### Remove Expiry from Key

    > persist [key]

### Overwrite Key's Value

Overwrite key's value by assigning it to the key with set command:

    > set [key1] [value1]
    > set [key1] [value2]

### Get a Random Key from DB

    > randomkey

### Rename a Key

    > rename [key] [new_key]

NOTE: if there is already a key [new_key] then the value for [key] will now be the value for [new_key]

Rename a key, only if key does not exist:

    > renamenx [key] [new_key]

### Alter Last Access Time of Key(s)

    > touch [key1] ... [key2]

### Remove Key(s) Asynchronously

    > unlink [key1] ... [key2]

NOTE: this is good for deleting a large number of keys, since it won't affect performance, and it won't block the current thread.

### Type of Data Stored in Key

    > type [key]

### KEYS Command

Returns all keys matching pattern.

Supported glob-style patterns:

    - h?llo matches hello, hallo, hxllo
    - h*llo matches hllo, heeeello
    - h[ae]llo matches hello, hallo, but not hillo
    - h[^e]llo matches hallo, hbllo, but not hello
    - h[a-b]llo matches hallo and hbllo
    - *ll* matches hello, hallo, but not helo
    - h???? matches, hello, hallo, but not elloo

Command:

    > keys [pattern]

### Dump Key

Serialize and backup the value stored in key, in a Redis-specific format:

    > dump [key]

### Restore Key

    > restore [key] [ttl] [serialized-value] [REPLACE]

Use 0 for ttl, if not wanting it to expire.

Serialized-value is the value that is returned when key is dumped. Example: "\n\x17\x17\x00\x00\x00\x12\x00\x00\x00\x03\x00\”

Use REPLACE flag, if you want to overwrite the key, if it is currently in the db.
