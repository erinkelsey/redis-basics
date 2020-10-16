# Publish and Subscribe

Allows for simple message buses to be created.

Allows Redis to act as a broker for multiple clients, providing a simple way to post and consume messages and events.

## How it Works

Senders (publishers) are not programmed to send their messages to specific receivers (subscribers).

Published messages are characterized into channels, without knowledge of who (if any) the subscribers are.

Subscribers express interest in one or more channels, and only receive messages that are of interest, without knowledge of who (if any) the publishers are.

Messages will only be received by subscribers if they have subscribed to the channel before the message was sent by publishers.

## Commands

### Publish Message

    > publish [channel] [message]

NOTE: returns 0 if there are no subscribers to channel, else returns the number of subscribers message received.

### Subscribe to Channel

    > subscribe [channel] [channel ...]

Unsubscribe:

    > unsubscribe [channel] [channel ...]

Pattern subscription:

    > psubscribe [pattern] [pattern ...]

### Check subscribers

    > pubsub [subcommand] [[argument] [argument ...]

Check number of subscribers to channel:

    > pubsub numsub [channel]

NOTE: this will not detect pattern subscription subscribers

Check number of pattern subscribers:

    > pubsub numpat
