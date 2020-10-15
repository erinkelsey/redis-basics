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

Redis sets are unordered collection of strings.

### Create and/or Add Member

    > sadd [key] [member] [member ...]

### Get Member(s)

View all members:

    > smembers [key]

Get random member:

    > srandmember [key]

### Check if Member Exists

    > sismember [key] [member]

NOTE: returns 1 if member exists, else returns 0.

### Number of Members

    > scard [key]

### Move Member to another Set

    > smove [source_key] [destination_key] [member]

### Remove Members

Remove a number of members randomly:

    > spop [key] [count]

NOTE: count is the number of members to remove. The removed items will be returned.

Remove specific member(s):

    > srem [key] [member] [member ...]

### Operations on Set

Difference of Set:

The difference if two sets, written A - B, is the set of all elements of A that are not elements of B.

    > sdiff [key1] [key2 ...]

Store output in another key:

    > sdiffstore [new_key] [key1] [key2]

Intersection of Set:

Intersection of two sets A and B is the set of all elements that both A and B have in common.

    > sinter [key1] [key2 ...]

Store output in another key:

    > sinterstore [new_key] [key1] [key2 ...]

Union of Sets:

The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. All elements are unique.

    > sunion [key1] [key2 ...]

Store output in another key:

    > sunionstore [new_key] [key1] [key2 ...]

## Sorted Sets

Sorted Sets are similar to a mix between a Set and a Hash.

Like Sets, Sorted Sets are composed of unique, non-repeating string elements.

Sorted Sets elements are ordered based on a score.

Every element in a Sorted Set is associated with a floating point value called the score (which is similar to a Hash, since every element is mapped to a value).

### Create and/or Add

    > zadd [key] [score] [member] [score member ...]

Only add member if doesn't already exist:

    > zadd [key] NX [score] [member] [score member ...]

Only update existing member(s):

    > zadd [key] XX [score] [member] [score member ...]

Return number of member changed:

    > zadd [key] CH [score] [member] [score member ...]

### Get Member(s)

    > zrange [key] [start] [stop] [WITHSCORES]

Get members in reverse:

    > zrevrange [key] [start] [stop] [WITHSCORES]

Get the score of member:

    > zscore [key] [member]

Get rank (position) of member in set:

    > zrank [key] [member]

Get reverse rank (position) of member in set:

    > zrevrank [key] [member]

Get members by score:

    > zrangebyscore [key] [min_score] [max_score] [WITHSCORES] [LIMIT offset count]

### Get Members Lexicographically

Get members by range lexicographically:

    > zrangebylex [key] [string] [string ...]

Get all members by range lexicographically:

    > zrangebylex [key] - +

NOTE: use [ to include and ( to exclude

Get members in reverse lexicographically:

    > zrevrangebylex [key] [string] [string ...]

Count members in lexicographic range:

    > zlexcount [key] [string] [string ...]

### Increment Score of Member(s)

    > zadd [key] INCR [increment_score_by] [member] [member ...]

OR

    > zincrby [key] [increment_score_by] [member]

### Check Length (Cardinality)

    > zcard [key]

### Remove Member(s)

    > zrem [key] [member] [member ...]

Pop a certain number of element(s) with highest scores:

    > zpopmax [key] [count]

Pop a certain number of element(s) with lowest scores:

    > zpopmin [key] [count]

Remove members lexicographically:

    > zremrangebylex [key] [min] [max]

Remove members by rank:

    > zremrangebyrank [key] [min] [max]

Remove members by score:

    > zremrangebyscore [key] [min] [max]

### Count Members by Score

    > zcount [key] [score_start] [score_stop]

Include any score:

    > zcount [key] -inf +inf

### Operations on Sorted Sets

Weights:

- a multiplication factor for Sorted Set's score
- the score of every element in every Sorted Set is multiplied by the weight, before being passed to the aggregation function
- default is 1

Aggregate:

- specify how the results of an intersection are aggregated
- three options: SUM, MIN, MAX
- default is SUM -> score of an element is summed across the inputs where it exists
- MIN or MAX -> resulting set will contain either the minimum or maximum score for a value

Intersection:

    > zinterstore [new_key] [key1] [key2 ...] [WEIGHTS weight] [AGGREGATE SUM|MIN|MAX]

Union:

    > zunionstore [new_key] [key1] [key2 ...] [WEIGHTS weight] [AGGREGATE SUM|MIN|MAX]
