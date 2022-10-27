# trades
The trades-lua.xml file contains, among other windows, a Lua-based Filter window. You can use the trades-lua.xml file with SAS Event Stream Processing 2022.10 and later. When you pass data into the Source window called Trades, you must specify the following date format: `%d/%b/%Y:%H:%M:%S`. SAS Help Center contains step-by-step instructions about how to create the project from scratch and how to execute it. For more information, see [Processing Trades](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=espstudio&docsetTarget=n1ch2p6gl5sy7yn1isntwpryfx93.htm).

The trades-eel.xml file contains a Filter window that uses an Expression Engine Language (EEL) expression. You can use the trades-eel.xml file with SAS Event Stream Processing 2020.1 and later. However, beginning in SAS Event Stream Processing 2022.10, it is recommended not to use EEL in Filter windows. The use of EEL in Filter windows is legacy functionality. The trades-eel.xml file is provided for use with earlier versions of SAS Event Stream Processing, which do not contain functionality for Lua-based Filter windows. When you pass data into the Source window called Trades, you must specify the following date format: `%d/%b/%Y:%H:%M:%S`. SAS Help Center contains step-by-step instructions about how to create the project from scratch and how to execute it. For more information, see [Processing Trades](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=v_028&docsetId=espstudio&docsetTarget=n1ch2p6gl5sy7yn1isntwpryfx93.htm).