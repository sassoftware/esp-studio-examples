# Event Sorter

Use a Event Sorter custom window to sort incoming events by a time field that defines when the events were created, as opposed to when they are available to the event stream.

In this example, data from the International Space Station (ISS) data is read from a file. This data has been intentionally sorted in reverse order to show the effectiveness of the custom window. The ISS time field is written in human readable format. The second window, which is a Lua window, is used to convert the human readable time into Linux epoch time. This field is used as the sort field. The last window is the custom window, which performs the sorting. The Event Sorter custom window is written in Lua.

For more information about how to explore and test this project, see [Using the Examples](https://github.com/sassoftware/esp-studio-examples#using-the-examples).

For more information about the Event Sorter custom window, see [Event Sorter Custom Window](https://github.com/sassoftware/esp-studio-custom-windows/tree/main/Lua%20Event%20Sorting)
