# Transactions

A transaction in Redis consists of a block of commands.

All the commands in a transaction are serialized and executed sequentially.

MULTI, EXEC, DISCARD and WATCH are the foundation of transactions in Redis.

Commands are executed as a single isolated operation, which means that a request issued by another client cannot be server in the middle of the execution of a transaction.

A transaction is atomic, which means that either all of the commands or none are processed.

There is no ability to rollback transactions in Redis.

## Start Transaction

    > multi

Then add all commands you want to run. Commands are moved into a queue.

## Execute Transaction

    > exec

Executes all commands in queue of multi.

## Discard Transaction

    > discard

## Watch

Provides check and set functionality, ie. monitor keys.

    > watch [key] [key ...]

Set watch before starting transaction. If try to modify a watched key in a transaction, it won't execute the command; the value will be unchanged.

After exec command is run, key will become unwatched.

Flush all watched keys:

    > unwatch
