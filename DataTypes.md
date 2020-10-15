# Redis Data Types

## Strings

### Append

    > append [existing_key] [value_to_append]

### Substring

    > getrange [key] [start_index] [end_index]

Can use negative numbers to signify end of string:

    > getrange [key] 0 -2

NOTE: The above will get all of the chars from the string except the last one. Using -1 would be the whole string.

### Set Substring of Value

    > setrange [key] [offset] [substring_value]

Example:

    > set k1 "Hello World"
    > setrange k1 6 Redis
    > get k1
    "Hello Redis"

### Length

    > strlen [key]

## Numbers

All numbers are returned as strings with get command, however you can perform operations on them.

Set the value to an integer:

    > set [key] 1

Set the value to a float:

    > set [key] 1.0

### Increment Integers

Increment by 1:

    > incr [key]

Example:

    > set score 1
    > incr score
    > incr score
    > get score
    "3"

Increment by specific number:

    > incrby [key] [num]

NOTE: num can only be an integer

### Decrement Integers

Decrement by 1:

    > decr [key]

Decrement by specific number:

    > decrby [key] [num]

NOTE: num can only be an integer

### Increment Floats

    > incrbyfloat [key] [num]

NOTE: num can be either an integer or float

## Lists

Redis lists are implemented as Linked Lists.

Accessing elements by index are very fast in lists implemented with an Array, and not so fast in lists implemented by Linked Lists.

### Create and/or Add Elements

Add element from left (append to head):

    > lpush [key] [value] [value ...]

Add element from right (append to end):

    > rpush [key] [value] [value ...]

NOTE: use lpushx and rpushx to only insert element(s) if the list already exists

### Set Element at Index

    > lset [key] [index] [value]

### Insert Element at Index

    > linsert [key] [BEFORE | AFTER] [pivot] [value]

Use BEFORE to insert before pivot element, and AFTER to insert after. The pivot is the actual element value to insert before/after, not an index.

### Show List Elements

    > lrange [key] [start] [stop]

Show whole list:

    > lrange [key] 0 -1

### Get Element at Index

    > lindex [key] [index]

### Remove Single Element

Pops off the last element in the list:

    > rpop [key]

Pops off the first element in the list:

    > lpop [key]

NOTE: the popped off element will be returned

### Remove Multiple Elements

    > lrem [key] [count] [value]

Rules:

- count > 0: remove count number of elements which are equal to value, moving from head to tail
- count < 0: remove count number of elements which are equal to value, moving from tail to head
- count == 0: remove all elements equal to value

### Trim List

Returns a list with only the elements between start and stop:

    > ltrim [key] [start] [stop]

### Length

    > llen [key]

## Hashes

Redis Hashes are maps between string fields and string values, and are mainly used to represent objects.

### Set

    > hset [key] [field] [value]

Set multiple fields:

    > hmset [key] [field] [value] [field value ...]

Set field only if it does not exist:

    > hsetnx [key] [field] [new_value]

### Get

Get value from single field:

    > hget [key] [field]

Get values from multiple fields:

    > hmget [key] [field] [field2 ...]

Get all fields and values:

    > hgetall [key]

Get all values from fields:

    > hvals [key]

Get all fields from key:

    > hkeys [key]

### Check if Field Exists in Hash

    > hexists [key] [field]

NOTE: 1 is returned if field exists, else returns 0

### Length

Num of fields in hash:

    > hlen [key]

Get string length of field value:

    > hstrlen [key] [field]

### Delete Field

    > hdel [key] [field]

### Increment Field Value

Integers:

    > hincrby [key] [field] [num]

Floats:

    > hincrbyfloat [key] [field] [num]

NOTE: field can be integer or float for hincrbyfloat

## Sets
