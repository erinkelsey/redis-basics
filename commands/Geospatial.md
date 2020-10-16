# Geospatial

Geospatial: any data that is indicated by or related to a geographic location

Geospatial objects: pairs of longitude and latitude

Redis allows the ability to store, query and update huge amounts of geospatial objects with very low latency.

## How it Works

Redis uses a common strategy for managing geospatial objects; for each longitude and latitude pair, a GeoHash is computed.

GeoHash: 52-bit integer value; encodes positions in a short string of letters and digits

GeoHash is compact structure for storage, but allows for efficient queries to be performed.

GeoHash is a Sorted Set and is stored as the score, and the name of the point is used as the value of the member.

There are limits to the coordinates that can be indexed: areas very near to the poles are not indexable.

Valid longitudes: -180 to 180 degrees

Valid latitudes: -85.05112878 to 85.05112878 degrees

## Commands

### Add GeoSpatial Items

Adds the specified geospatial items (latitude, longitude, name) to the specified key. Data is stored into the key as a sorted set.

    > geoadd [key] [longitude] [latitude] [member] [longitude latitude member ...]

### Get Items from Sorted Set

    > zrange [key] 0 -1 WITHSCORES

### Get GeoHash

    > geohash [key] [member]

Use http://geohash.org/[geo_hash] to see if it works

### Get Latitude and Longitude

    > geopos [key] [member]

### Get Distance Between Two Members

    > geodist [key] [member1] [member2] [unit]

Unit can be miles (mi), kilometers (km), meters (m) or feet (ft). Default is meters.

### Get with GeoRadius

By coordinates:

    > georadius [key] [longitude] [latitude] [radius] [unit] [WITHCOORDS] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]

By member:

     > georadiusbymember [key] [longitude] [latitude] [radius] [unit] [WITHCOORDS] [WITHDIST] [WITHHASH] [COUNT count] [ASC|DESC] [STORE key] [STOREDIST key]
