# Alert Suppression

Use a Alert Suppression custom window to suppress output event alerts based on the allowed frequency.

When an alert arrives, the Alert Suppression custom window checks whether it is the first alert in the suppression period. If it is the first alert, then the alert is passed on. If it is not the first alert, then the alert is removed or marked as suppressed, and the alert is saved to the log. The Alert Suppression custom window uses Lua code.

For more information about how to explore and test this project, see [Using the Examples](https://github.com/sassoftware/esp-studio-examples#using-the-examples).

For more information about the Alert Suppression custom window, see [Alert Suppression Custom Window](https://github.com/sassoftware/esp-studio-custom-windows/tree/main/Alert%20Suppression)
