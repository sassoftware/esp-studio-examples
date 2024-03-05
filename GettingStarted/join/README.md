# join

Join stock market trades with the corresponding traders.

A Join window receives events from a left input window and a right input window. It produces a single output stream of joined events. Joined events are created according to a user-specified join type and user-defined join conditions. 

For more information about how to explore and test this project, see [Using the Examples](https://github.com/sassoftware/esp-studio-examples#using-the-examples). 

If you do not use the **Install example** button in SAS Event Stream Processing Studio, note that this project includes connector orchestration and as a result, it is recommended that you do not use the **Publish** button in SAS Event Stream Processing Studio's test mode to publish events from CSV files to the Source windows. Instead, edit the file paths in the publisher connectors in the sourceWindow_01 and sourceWindow_02 windows so that they refer to the location in your system where you placed the CSV files. For more information, see [SAS Help Center: Configure a File and Socket Connector](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n0esv2n0cbbpgcn1r281krr1iv6q.htm#n0y87cwr7q5vo6n1qlfcey182vt6).

Tip: The SAS Help Center topic [Join Example](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=esmuse&docsetTarget=p1fvkzlm2erh7fn1r8t6ljgvyxr7.htm) explains how to use SAS Event Stream Manager to deploy this project to a Kubernetes cluster, as opposed to running the example in test mode in SAS Event Stream Processing Studio.
