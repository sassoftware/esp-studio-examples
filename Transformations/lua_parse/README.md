# Generate Events from JSON Using the Lua Window
## Overview
Within a Lua window of SAS Event Stream Processing, you write Lua code to programmatically generate events. The following examples show how to code a Lua window to parse a JSON string in order to generate multiple events from a single event stream.
- The [basic example project](#basic-example-project) is designed to show how event generation works. This example is included in the `lua_parse_simple<release>.zip` project package and can be installed directly from SAS Event Stream Processing Studio. For more information, see [Using the Examples](https://github.com/sassoftware/esp-studio-examples#using-the-examples).
- The [advanced example project](#advanced-example-project) is intended to provide a more realistic use case of event generation.
---
**NOTE:**
Use these examples with SAS Event Stream Processing 2022.10 and later.

---

## Basic Example Project

### Workflow
The following figure illustrates the complete flow of events through the SAS Event Stream Processing project.

![basic example workflow](img/basic_workflow.png "basic example workflow")

1. The Source window (source) receives the sample input data from a CSV file.
2. The JSON data embedded in the CSV file is streamed to the Lua window (createMulti).
3. The Lua window generates multiple events from the JSON data.

#### source
The source window is a Source window that streams data from the file [luaParseJsonSimple.csv](luaParseJsonSimple.csv). That file contains JSON data that is encapsulated within a CSV string.

---
**NOTE:**
The first two columns in the CSV file contain the opcodes for SAS Event Stream Processing.

---
The JSON data consists of sensor data for two devices. One of the devices has data from one sensor, and the other device has data from two sensors, as illustrated in the following figure. 

![basic example data structure](img/basicDataStructure.png "basic example data structure")

#### createMulti
The createMulti window is a Lua window. It contains Lua code that performs the following steps:


<table>
<tr>
<th>Step</th> <th>Lua Code Section</th>
</tr>
<tr>
<td> Creates an event ID for each event, beginning with the value 1. </td>
<td>


```
local   eventId = 1
```


</td>
</tr>
<tr>
<td> Places the parsed JSON data into a Lua table. </td>
<td>

  
```
function create(data,context)
  local   events = {}
  local   sensorinfo = esp_parseJsonFrom("sensorinfo")
```

  
</td>
</tr>
<tr>
<td> Extracts key-value pairs from the Lua table. </td>
<td>


```
for index,value in ipairs(sensorinfo)
   do
      local   e = {}

      e.id = tostring(eventId)
      e.device_id = value.device_id
      e.sensor_id = value.sensor_id
      e.value = value.value
      events[index] = e

      eventId = eventId + 1
   end
```


</td>
</tr>
<tr>
<td> Returns results as SAS Event Stream Processing events. </td>
<td>


```
    return(events) 
end
```


</td>
</tr>
</table>


To view project in its entirety and the Lua code in context, see the [luaParseJsonSimple.xml](luaParseJsonSimple.xml) file.


### Test the Project and View the Results

To see a demo of how to test this project and view the results, watch the following video:

https://user-images.githubusercontent.com/73890196/174394663-c5fa558f-abd0-4df4-8a8e-e60570e939bc.mp4


## Advanced Example Project
### Use Case
Typically, sensor data streams into SAS Event Stream Processing within a JSON opaque string that is streamed over a message broker such as RabbitMQ. You can set up a Lua window to parse the opaque string and use the data to generate events.

In this example, simulated sensor data from a train (speed, location, car ID, and date) within an opaque JSON string is received from RabbitMQ. The project transforms this data into multiple events. Specifically, the project does the following:

1. Configures a message broker to receive the JSON objects.
2. Sends the JSON object via ```opaquestring``` to a Lua window for processing.
3. Uses Lua code to parse the JSON string and generate multiple events.

### Prerequisite
To run this example project, you must configure a RabbitMQ message broker to work with the project in SAS Event Stream Processing Studio.

### Workflow
The following figure illustrates the complete flow of events through the SAS Event Stream Processing project.

![advanced example workflow](img/adv_workflow.png "advanced example workflow")

1. The first Source window (train_data) receives the sample input data from a CSV file.
2. RabbitMQ subscribes to train_data and converts it to a JSON opaque string.
3. The JSON opaque string enters the second Source window (pub_win).
4. The JSON string is streamed to the Lua window (parseJson).
5. The Lua window generates multiple events from the JSON string.

#### train_data
1. For demonstration purposes, sensor data input is simulated by uploading a CSV file to a Source window (train_data). The CSV data enters this Source window through a file and socket connector.  To view the CSV data, see the [trainData.csv](trainData.csv) file.
2. The message broker RabbitMQ connects to train_data using a subscriber connector. RabbitMQ transforms the CSV data into a JSON string.

The order in which connectors start is specified with connector groups. For more information about subscriber and publisher connectors, see [SAS Event Stream Processing: Overview to Connectors](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=espca&docsetTarget=p1nhdjrc9n0nnmn1fxqnyc0nihzz.htm).

#### pub_win
1. RabbitMQ publishes a JSON opaque string named "sensorinfo" to the pub_win Source window.
2. The JSON opaque string is streamed to the Lua window (parseJson).

#### parseJson
The parseJson window is a Lua window. It contains Lua code that performs the following steps:


<table>
<tr>
<th>Step</th> <th>Lua Code Section</th>
</tr>
<tr>
<td> Places the parsed JSON opaque string into a Lua table. </td>
<td>

  
```
function create(data,context)
  local   events = {}
  local   sensorinfo = esp_parseJsonFrom("sensorinfo")
```

  
</td>
</tr>
<tr>
<td> Extracts key-value pairs from the Lua table. </td>
<td>


```
local   index = 1
   for i1,v1 in ipairs(sensorinfo)
   do
     local   e = {}
   
     for i2,v2 in ipairs(v1)
     do
       for k,v in pairs(v2)
       do
         e[k] = v
       end
     end
     events[index] = e
     index = index + 1
    end
```


</td>
</tr>
<tr>
<td> Returns results as SAS Event Stream Processing events. </td>
<td>


```
    return(events) 
end
```


</td>
</tr>
</table>




To view the project in its entirety and see the Lua code in context, see the project file [luaParseJson.xml](luaParseJson.xml).

### Test the Project and View the Results
To see a demo of how to test this project and view the results, watch the following video:

https://user-images.githubusercontent.com/73890196/174398488-8572d107-8eeb-4861-af0a-1e8d47e4a038.mp4


### Next Steps
You can add windows to the project to further analyze the data. For example, you might add a Filter window to extract speeds above a certain value.

### Additional Resources
For more information, refer to the following resources:

- [SAS Help Center: Using Lua Windows](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=espcreatewindows&docsetTarget=p0yj92wgv3ssyyn1syatsh9l1t74.htm) 
- [SAS Help Center: Working with Lua Windows in SAS Event Stream Processing Studio](https://documentation.sas.com/?cdcId=espcdc&cdcVersion=default&docsetId=espstudio&docsetTarget=n1n3kx16nz64jfn1tzkgddvobeus.htm)
