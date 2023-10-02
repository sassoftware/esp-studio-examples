# Detecting Objects by Using an ONNX Model (Tiny YOLO Version 7)
## Overview
This example demonstrates how to use a project to reference an open-source ONNX model, in order to detect objects in a video.

---
**NOTE:**
Use this example with SAS Event Stream Processing 2023.09 and later.

---

## Source Data and Other Files
- PeopleWalking.mp4 is the video that is used as input for this example. 
- model.xml is the project associated with this example.
- input_preproc.py, tensor_utils.py, and utils.py are Python modules for changing the images into a format that is suitable for the ONNX model and for changing the images back into a format that is suitable for SAS Event Stream Processing. show.py contains Python code to visualize the detections that the model has made. 
- yolov7-tiny_640x640.onnx, yolov7-tiny_640x640.py, and Yolov7_decoder.py are an open source ONNX model and associated Python modules for detecting objects in images or videos.

For more information about the source of the above files, see [Source of the Model and Video Files](#source-of-the-model-and-video-files).

## Prerequisites

### Check System Prerequisites

Check that the following system prerequisites are met. For more information, contact your system administrator.

- A supported version of ONNX Runtime has been deployed. For more information, see [Working with ONNX Models](https://go.documentation.sas.com/doc/en/espcdc/default/espan/p0b1zsgwrsirbln1typkfoz428y9.htm).
- A persistent volume is available. In a Kubernetes environment, using ONNX models requires that when SAS Event Stream Processing is deployed, it is configured to access persistent volumes. This configuration involves applying overlays. For more information, see [Managing Persistent Volumes (PVs)](https://go.documentation.sas.com/doc/en/espcdc/default/espex/n19tbdmek5u0rdn1f31lktl95r27.htm#n1liey9g57i1ntn19mkd4pnpt7pd).

The example is configured to use CUDA (Compute Unified Device Architecture) as the execution provider. For more information, see [Understanding Execution Providers](https://go.documentation.sas.com/doc/en/espcdc/default/espan/n04g09la3oqh59n0zls2jzllfgyf.htm). If CUDA is not available, you could adjust the w_reader window to change the execution provider to CPU.

This example is not intended for use with an ESP server that is running on an edge server.

## Workflow
The following figure shows the diagram of the project:

![Diagram of the project](img/onnx_example_object_detection.png "Diagram of the project")

- w_data is a Source window. This is where individual frames from the input video enter the project.
- w_pre_process is a Calculate window. The Python code referenced by this window converts the frames into tensors, so that the data can be processed by the ONNX model. A tensor is an n-dimensional array that contains the same type of data. The Python code referenced by this window can also perform other conversion tasks such as changing image size and image orientation. In general, a project that references an ONNX model is likely to require pre-processing of data before that data is ready to be scored.
- w_reader is a Model Reader window. This window reads the ONNX model and passes it to the w_score window.
- w_score is a Score window. This window executes the ONNX model when data passes through the window. The input data is in tensor format. The data is scored: that is, objects are detected in images and labels are assigned to the objects. The output from this window includes a second set of tensors.
- w_post_process is a Calculate window. The Python code referenced by this window converts the model output (tensor format) into easier formats, so that the outputs can be handled by subsequent windows. Also, this window draws the bounding boxes of the detected objects. In general, a project that references an ONNX model is likely to require post-processing of data after scoring has taken place.
- w_parse_labels is a Functional window. This window splits a comma-separated string that contains labels into separate events, so that each event contains one label. The labels relate to objects that were detected in images.
- w_count objects is an Aggregate window. This window counts the labels.

### w_data

Explore the settings for this window:
1. Open the project in SAS Event Stream Processing Studio and select the w_data window.
2. Click the w_data window.
3. In the right pane, expand **State and Event Type**.<br/>The window is stateless and the index type is `pi_EMPTY`. That is, the window acts as a pass-through for all incoming events. The `pi_EMPTY` index does not store events.<br/>The window is set to accept only Insert events.
4. To examine the window's output schema, on the right toolbar, click ![Output Schema](img/output-schema-icon.png "Output Schema"). Observe the following fields: 
   - `id`: Each image that the window receives is assigned an ID, and this field holds information about the ID. This is a key field. 
   - `image`: This field holds the video frames.
5. Click ![Properties](img/show-properties-icon.png "Properties"). 
6. Expand **Input Data (Publisher) Connectors**.
7. Double-click the `video_publisher` Video Capture connector.<br/>The Connector Configuration window appears.<br/>The **Filename** field shows that the window reads incoming events from the PeopleWalking.mp4 file. The **Publishformat** field is set to `jpeg`, meaning that the frames from the video are published in JPEG encoding.
8. Click **All properties**. Observe that the **publishrate** field is set to 10, meaning that 10 frames per second are published to the project. The **resize_x** and **resize_y** fields are set to 960 and 540 respectively, to define the resolution of the frames that are published. 
9. Click **Cancel** to close the All Properties window.
10.	Click **Cancel** to close the Connector Configuration window.

---
**NOTE:**
The input data provided in this example is to be used only with this project. Using or altering this data beyond the example for any other purpose is prohibited.

---

You can replace the PeopleWalking.mp4 file with your own video file, RTSP (Real-Time Streaming Protocol) stream, or another input stream. When the PeopleWalking.mp4 file is used, the example detects a variety of objects, such as persons, traffic lights, cars, buses, and handbags.

### w_pre_process

Explore the settings for this window:
1. Click the w_pre_process window.
2. In the right pane, expand **Settings**.<br/>This window uses a user-specified calculation. That is, an online algorithm is not used.
3. In the **Handlers** section, double-click the `w_data` handler.<br/>The Input Handler window appears. Input handlers process incoming event streams in your project. The handler type is `SAS Micro Analytic Service`. The `tensorProcess` module is selected. The `tensorProcess` module (which is defined at the project level) contains two functions: `preprocess` and `postprocess`. The `preprocess` function is selected; this means that the `preprocess` function is used the handle data that comes in from the w_data window.
4. Click **Cancel**.

### tensorProcess Module

In general, a project that references an ONNX model is likely to require pre-processing of data before the data is ready to be scored, and post-processing of the data that has been scored. In this example, the Python code that performs this pre-processing and post-processing is referenced from the `tensorProcess` module.

Explore the tensorProcess Module:
1. Click ![Project](img/project-properties-button.png "Project") on the toolbar. Project-level properties are displayed in the right pane.
2. Expand **SAS Micro Analytic Service Modules**.
3. Double-click the `tensorProcess` row in the table.<br/>The SAS Micro Analytic Service Module window appears. A SAS Micro Analytic Service module is a named block of code that you execute within a SAS Event Stream Processing project. The **Embedded code** field contains the Python code that is referenced from the w_pre_process and w_post_process windows.
4. Click **Cancel**.

### Project’s User-Defined Properties

Expand **User-Defined Properties**. The user-defined property that is referenced in the Python code (`CREATE_ANNOTATED_IMAGE`) is defined here.

### w_reader

Explore the settings for this window:
1. Click the w_reader window.
2. In the right pane, expand **Settings**.
   - The yolov7-tiny_640x640.onnx file is the model that is used to detect objects in the input images.<br/>You could replace this model with another model. However, changing the model would require you to also adjust other files in this example, including the Python code.
   - The selected execution provider is CUDA, which means that hardware acceleration is used. </br>SAS Event Stream Processing Studio does not detect which execution providers have been deployed. Contact your system administrator for more information about which execution providers are available to you.

### w_score 

Explore the settings for this window:
1. Click the w_score window.
2. In the right pane, expand **Settings**. The **Model source** field is set to `Offline`, which allows the **Model type** field to be set to `ONNX`. The ONNX model is not specified here: the model is selected in the w_reader window and passed to the w_score window.
3. Click ![Output Schema](img/output-schema-icon.png "Output Schema") to display the window’s schema. The schema differs from the schema of the w_source window in that the schema for the w_score window also contains a field called `tensor1_out`, with a field type of `blob`. The data for this field contains the scored events. In addition, there is a field called `image_shape`, which was calculated in the w_pre_process window and contains the image resolution in tensor format. Some ONNX models require this field as an additional input, but this field is not used for the Tiny YOLO version 7 model. 
4. Click ![Properties](img/show-properties-icon.png "Properties").
5. Expand **Input Map**. The input map specifies the properties of the data to be scored. That is, input data is mapped to the variables that the ONNX model is expecting.
6. Expand **Output Map**. The output map specifies the properties of the data that has been scored. The `tensor1_out` field that is specified in the schema appears here.

### w_post_process

Explore the settings for this window:
1. Click the w_post_process window.
2. In the right pane, expand **Settings**.<br/>This window uses a user-specified calculation. That is, an online algorithm is not used.
3. In the **Handlers** section, double-click the `w_score` handler.<br/>The Input Handler window appears. Input handlers process incoming event streams in your project. The handler type is `SAS Micro Analytic Service`. The `tensorProcess` module is selected. The `tensorProcess` module (which is defined at the project level) contains two functions: `preprocess` and `postprocess`. The `postprocess` function is selected; this means that the `postprocess` function is used the handle data that comes in from the w_source window.
4. Click **Cancel**.

### w_parse_labels

Explore the settings for this window:
1. Click the w_parse_labels window.
2. In the right pane, expand **Event Generation**.
3. In the Event loops table, double-click the `Loop` event loop.<br/>The Event Loop window appears. The **Regular expression** field has the following content: `([^,]+)` This regular expression splits a comma-separated string that contains labels into separate events, so that each event contains one label. The labels relate to objects that are detected in images. For example, an incoming event that contains the string `person,person,car,person` is split into four events: the first and the second event contain the label `person`, the third event contains the label `car`, and the fourth event contains the label `person`. The purpose of splitting the events is to enable the subsequent w_count_objects window to count the labels.
4. Scroll down to view the Functions table. The table contains two rows:<br/>![Event loop functions](img/onnx_example_event_loop_functions.png "Event loop functions")<br/>When you run the project in test mode later, the output from the w_parse_labels window includes columns that relate to the `label` and `subid` functions:
    - `label`: the values of the labels that were split from the comma-separated string.
    - `subid`: an additional event number (a “sub-ID”) for each event that was split from the comma-separated string. That is, each event contains information about the original ID (which associates that label with the other labels that came from the same comma-separated string) and the sub-ID. For example, for the original string `person,person,car,person`, the first instance of `person` gets a sub-ID of 0, the second instance of `person` gets a sub-ID of 1, `car` gets a sub-ID of 2, and the last instance of `person` gets a sub-ID of 3.
5. Click **Cancel**.

### w_count_objects   

Explore the settings for this window:
1. Click the w_count_objects window.
2. In the right pane, click ![Output Schema](img/output-schema-icon.png "Output Schema"). w_count_objects is an Aggregate window, and the aggregation is based on the `label` field (the key field). The `counter` field specifies that the ESP_aCountNonNull aggregation function is used. That is, the w_count_objects window counts the number of times when the `label` field is not null.

## Test the Project and View the Results

As discussed in the [w_data](#w_data) section, the w_data window includes a publisher connector that is configured to read incoming events from a video file.

When you enter test mode in SAS Event Stream Processing Studio, complete the following steps:
1.	In the left pane, clear the check boxes for all windows except the w_parse_labels and w_count_objects windows. 
2.	Select **Configure and Run Test**.

    <!-- ![Configure and Run Test ](img/configure_and_run_test.png "Configure and Run Test ") -->
    <img alt="Configure and Run Test" src="img/configure_and_run_test.png"  width="148" height="75">

3.	In the Load and Start Project in Cluster window, click **Edit deployment settings**.
4.	In the Deployment Settings window, adjust the settings as shown in the following image:

    <!-- ![Deployment settings](img/deployment_settings.png "Deployment settings ") -->
    <img alt="Deployment settings" src="img/deployment_settings.png"  width="50%" height="50%">

5.	Click **OK** to close the Deployment Settings window.
6.	Click **OK** to close the Load and Start Project in Cluster window.

The results for each window appear in separate tabs in test mode. 

If it takes a long time for events to appear in test mode, contact your system administrator to check whether the minimum GPU node count is set to at least 1 in the cluster.



- The **w_parse_labels** tab shows the objects that were detected in the video frames. Each video frame can be seen as an image. The id column shows the ID of the image. The subid column shows the ID that was assigned to each object that was detected in the image. The label column shows the label assigned to object that was detected.
- The **w_count_objects** tab shows the total number of objects that were detected in all frames combined. 
 
To view test results for other windows, select different windows in the left pane and run the test again.

- The **w_data** tab shows that the Source window has received Insert events that contain video frames. This tab also shows the event IDs that have been assigned to the images. 
- The **w_pre_process** tab shows, in addition to previously discussed fields, the tensors that have been created by the pre-processing Python code.
- The **w_reader** tab does not show any data. This is expected behavior. The w_reader window passes the ONNX model to the w_score reader. When a Model Reader window is handling an ONNX model, a model event is not published.
- The **w_score** tab shows, in addition to previously discussed fields, the tensors that contain the scored events.
- The **w_post_process** tab shows the following fields, in addition to previously discussed fields:
    - The model_name column shows the ONNX model’s name.
    - The model_type column shows the ONNX model’s type.
    - The n_objects column shows the number of objects that were detected in the frame.
    - The coords column shows coordinates for the bounding box. If multiple objects are detected, the coordinates for the bounding box for each object are shown, one after another.
    - The coords_type column shows the coordinate type. The coordinate type for the yolov7-tiny_640x640.onnx model is `yolo`. The show.py script also supports other common coordinate types for object detection, like `coco` and `rect`. 
    - The scores column shows the confidence scores for each object that was detected. A number that is close to 1 indicates a high level of confidence about the object’s identification, whereas a number that is close to 0 indicates a low level of confidence.

## Next Steps

### Tracking Objects
After an ONNX model is used to detect objects, tracking the detected objects over time can be a useful next step. For example, you could follow a person between multiple frames. For more information, see [Using Object Tracker Windows](https://go.documentation.sas.com/doc/en/espcdc/v_037/espcreatewindows/p0jsgd7e0fa40ln16wxod1qpj9d2.htm).

### Using a Geofence
Geofences are virtual perimeters and can be used, for example, to trigger alerts when persons are detected in prohibited areas or when cars are parked in the wrong spot. For more information, see [Using Geofence Windows](https://go.documentation.sas.com/doc/en/espcdc/v_037/espcreatewindows/p0xru6q01dkxknn1t8gqo2q4zfu6.htm).

### Visualizing Objects in Grafana
If you are using SAS Event Stream Processing in Microsoft Azure, the detected objects can be visualized by using Grafana. Import the [grafana.json](grafana.json) to Grafana. 

---
**NOTE:**
This dashboard uses the [Base64 Image/Video/Audio/PDF](https://grafana.com/grafana/plugins/volkovlabs-image-panel/) plug-in for Grafana.

---

The dashboard includes the following panel:

<img alt="Grafana dashboard" src="img/grafana.png"  width="50%" height="50%">

## Source of the Model and Video Files

Some of the files in this example are reused from the SAS Software GitHub repository https://github.com/sassoftware/iot-sas-esp-onnx-runtime or have been adapted from files in that repository. 

### ONNX Model Source
Model Family: YOLOv7<br>
Model Name: 80 classes object detection<br>	
File Name: yolov7-tiny_640x640.onnx<br>
Provider: https://github.com/PINTO0309/<br>	
License: GNU version 3<br>
Source URL: https://github.com/PINTO0309/PINTO_model_zoo/tree/main/307_YOLOv7

### Video Credits and Copyright

| File Name     | Original Names                        | Copyright                 | s                                                        |
| ------------- | ------------------------------------ | ------------------------- | ------------------------------------------------------------ |
| PeopleWalking.mp4 | K13614_18989_1820284_2018Q3BrollSonya6500_day1_C0031.mp4 and K13624_18989_1820284_2018Q3BrollCard4_day1_9013.mp4 | © 2021 SAS Institute Inc. All Rights Reserved. | To be used only in the context of this Demo. |


### Video and Image Restrictions
The videos and images provided in this example are to be used only with the project provided. Using or altering these videos and images beyond the example for any other purpose is prohibited.

