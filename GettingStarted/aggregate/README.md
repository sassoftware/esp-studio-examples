# aggregate

Apply aggregation functions to a group of stock market trades.

When new events arrive in the Aggregate window, they are placed into aggregate groups. After a new event enters the event stream, the aggregation functions are called. The functions then modify the aggregation groups accordingly. Aggregate field calculation functions or expressions that are registered to the Aggregate window must appear in non-key fields, which in this project are `totalQuant` and `maxPrice`.

For more information about how to explore and test this project, see [Using the Examples](https://github.com/sassoftware/esp-studio-examples#using-the-examples).
