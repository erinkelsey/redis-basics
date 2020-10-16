# HyperLogLog

HyperLogLog provides a probabilistic alternative to Sets.

HyperLogLog keeps a counter of items that is incremented when new items are added that have not been previously added.

Provides a very low error rate when estimating the unique items (cardinality) of a set.

## Commands

### Create and/or Add

    > pfadd [key] [element] [element ...]

### Get Unique Elements

    > pfcount [key]

### Merge HyperLogLogs

    > pfmerge [dest_key] [source_key] [source_key ...]
