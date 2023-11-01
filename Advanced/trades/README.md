# Processing Trades

Identify large trades in stock market transactions.

This project identifies large securities transactions and the traders who were involved in those trades. SAS Help Center contains step-by-step instructions about how to create the project from scratch and how to execute it. For more information, see [Processing Trades](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=espstudio&docsetTarget=n1ch2p6gl5sy7yn1isntwpryfx93.htm).

---
**NOTE:**
Use this example with SAS Event Stream Processing 2022.10 and later. This example contains a Lua-based Filter window. Earlier releases of SAS Event Stream Processing do not support Lua-based Filter windows. 

---

If you do not use the **Install example** button in SAS Event Stream Processing Studio, note that if you use the **Publish** button to publish events from the `trades.csv` file into the Trades window, you must specify the following date format: `%d/%b/%Y:%H:%M:%S`. For more information, see [Publish Events from a CSV file](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p124n2fohetwqzn109gsdel6o1cj.htm).


