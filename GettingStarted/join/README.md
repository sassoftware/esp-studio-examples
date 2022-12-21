# join

Join stock market trades with the corresponding traders.

A Join window receives events from a left input window and a right input window. It produces a single output stream of joined events. Joined events are created according to a user-specified join type and user-defined join conditions. 

As this project contains multiple Source windows, when you use the Publish button in test mode, you must publish events for each Source window separately. You cannot publish events to multiple Source windows simultaneously. 

For more information about how to explore and test this project, see [Using the Examples](https://github.com/sassoftware/esp-studio-examples#using-the-examples). 

Tip: The SAS Help Center topic [Join Example](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=esmuse&docsetTarget=p1fvkzlm2erh7fn1r8t6ljgvyxr7.htm) explains how to use SAS Event Stream Manager to deploy this project to a Kubernetes cluster, as opposed to running the example in test mode in SAS Event Stream Processing Studio. In these instructions, you configure an input data connector rather than publish events in test mode.
