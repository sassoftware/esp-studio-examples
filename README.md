
# SAS Event Stream Processing Studio Examples

## Overview

This repository provides XML code examples that use SAS Event Stream Processing to process real-time streaming data. Project code is written to run in [SAS Event Stream Processing Studio](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/titlepage.htm). Use these examples with SAS Event Stream Processing 2020.1 and later, unless stated otherwise. 

To obtain XML code examples that run with earlier releases of SAS Event Stream Processing, visit [the SAS Event Stream Processing Code Examples download page](https://tds.sas.com/downloads/package.htm?pid=2421).

## Using the Examples

### Installing Examples Directly from SAS Event Stream Processing Studio

Beginning with SAS Event Stream Processing 2023.09, you can install some examples directly from SAS Event Stream Processing Studio: 

1. In SAS Event Stream Processing Studio, do one the following:
   - On the **Projects** page, click **View example projects**.
   - On any page, click ![Help](img/icon-helpmenu.png "Output Schema") and select **Examples**.
2. In the SAS Event Stream Processing Examples window, select an example with the **Install example** button in the right pane.
3. Click **Install example**. A project package ZIP file is imported from the relevant example's directory in this GitHub. The project XML file in the project package has connectors that point to input files in the product package. As a result, you do not need to configure connectors. 
4. Run the imported example in test mode. For more information, see [Running a Test](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p1xzbzbnvpspodn1h2jkzo9m9t7d.htm). 

For more information about how the example works, return to the SAS Event Stream Processing Examples window, select the example and click **View README in GitHub**. Beginning in SAS Event Stream Processing 2024.08, when you have installed an example, you can also access its README file from the **Project Package** pane. When you are viewing an example project in SAS Event Stream Processing Studio, you can also select each window in turn in the workspace to read brief descriptions of those windows in the right pane.

When the **Install example** button is not available but the example's directory contains a project package ZIP file, you can manually import the project package to SAS Event Stream Processing Studio, but only when you are using SAS Event Stream Processing 2023.09 or later. For more information, see [Import a Project](https://go.documentation.sas.com/doc/en/**espcdc/default/espstudio/n0qhr0p800gs68n18wbp96pu7txq.htm).

For more information about project packages in general, see [Project Package](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p0y6v0lhrr57zjn1c6de7k129uet.htm).

### Importing Examples Manually
There are some circumstances when you might need to import examples manually:
- You are using SAS Event Stream Processing 2023.08 or earlier.
- You are using SAS Event Stream Processing 2023.09 or later, but the functionality for project packages is not enabled in your environment.
- An example's directory does not include a project package ZIP file.

To import an example manually:
1. Save the contents of the example's directory to a convenient location on your computer.
2. Import the project XML file to SAS Event Stream Processing Studio. For more information, see [Import a Project](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n0qhr0p800gs68n18wbp96pu7txq.htm).
3. Open the project in SAS Event Stream Processing Studio and examine its contents. You can select each window in turn in the workspace to read brief descriptions of those windows in the right pane.
4. To pass events from input files into the project, do one of the following:
   - Configure connectors: Place the input files on the Kubernetes persistent volume and adjust any existing connectors to point to the location of the input files. If the project does not contain any connectors, you must add connectors yourself. For more information, see [Configure a File and Socket Connector](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n0esv2n0cbbpgcn1r281krr1iv6q.htm#n0y87cwr7q5vo6n1qlfcey182vt6).
   - Publish events directly from an input file: Deactivate any existing connectors. After you run the project in test mode (see step 5), use the **Publish** button to send events from the input files into Source windows. Using the **Publish** button enables you to send events into a running project without placing files on the Kubernetes persistent volume and without configuring connectors. For more information, see [Publish Events from a CSV file](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p124n2fohetwqzn109gsdel6o1cj.htm).
5. Run the project in test mode and view the test results. For more information, see [Running a Test](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p1xzbzbnvpspodn1h2jkzo9m9t7d.htm). 

**Note:** 
- You cannot use the **Publish** button to publish events to multiple Source windows simultaneously. For projects that contain multiple Source windows, you must publish events for each Source window separately. 
- When connector orchestration is used (for example, in the `geofence`, `join`, `sailing`, and `union` examples), it is not appropriate to use the **Publish** button. Instead, configure connectors for the project.

## Directory Contents

### End-to-end Examples

The [End-to-end Examples](/EndToEndExamples) directory contains projects {{description}}.

| Example | Description |
| ------ | ------ |
| [activitytracker](/EndToEndExamples/activitytracker) | Use a job template to deploy a project to an edge server.<br>This example processes GPS data from activity tracker devices worn by players in a football match. The example demonstrates how you can publish a project in SAS Event Stream Processing Studio to make it available in SAS Event Stream Manager, and then use a job template to deploy the project to an edge server. |
| [connectivity_analytics](/EndToEndExamples/connectivity_analytics) |Analyze telemetry data in telecom networks.<br>This example demonstrates how to use SAS Event Stream Processing to analyze telemetry data from a Connectivity Management Platform (CMP).|
| [matchlist_screening](/EndToEndExamples/matchlist_screening) | Perform fuzzy lookups on streaming data using SAS Data Quality.<br>This example demonstrates how SAS Event Stream Processing can perform fuzzy lookups on streaming data using SAS Data Quality. This project uses Expression Engine Language (EEL) to load the SAS Quality Knowledge Base (QKB).|
| [onnx_object_detection](/EndToEndExamples/onnx_object_detection) | Use an ONNX model to detect objects in an incoming video stream.<br>This example demonstrates how you can use an ONNX model to detect objects in an incoming video stream. Post-processing by a Python program converts scoring output to a more usable format. <br>**Note:** Use this example with SAS Event Stream Processing 2025.02 and later.|
| [onnx_pose_estimation](/EndToEndExamples/onnx_pose_estimation) | Use an ONNX model to detect keypoints of a person in an incoming video stream.<br>This example uses pose estimation, which is a computer vision technique for recognizing and categorizing the positions of a human body. This example builds on the onnx_object_detection example.<br>**Note:** Use this example with SAS Event Stream Processing 2025.02 and later.|
| [onnx_voice_transcription](/EndToEndExamples/onnx_voice_transcription) | Use an ONNX model to accurately transcribe audio. <br>This example uses post-processing by a Python program to convert the tokens that the model outputs into words.<br>**Note:** Use this example with SAS Event Stream Processing 2025.06 and later.|
| [sailing](/EndToEndExamples/sailing) | Visualize data obtained from a set of boats.<br>This example identifies two geographical areas of interest. One area is an exclusion zone that the boats identified are not permitted to enter. The other is an area where a speed restriction has been applied.|
| [trades](/EndToEndExamples/trades) | Identify large trades in stock market transactions.<br>This project identifies large securities transactions and the traders who were involved in those trades.|

### Input Streams

The [Input Streams](/InputStreams) directory contains projects {{description}}.

| Example | Description |
| ------ | ------ |
| [connector_orchestration](/InputStreams/connector_orchestration) | Use connector orchestration to manage multiple connectors in a project.<br>This example demonstrates connector orchestration. This is a feature that controls the sequence and state of connector execution. |
| [lua_connector](/InputStreams/lua_connector) | Use a Lua connector.<br>This example contains a Source window with a Lua connector that reads RSS feeds from scientific sites and publishes them into the project. <br>**Note:** Use this example with SAS Event Stream Processing 2023.04 and later.|
| [python_connector](/InputStreams/python_connector) | Use a Python connector.<br>This example contains a Source window with a Python connector that calls a JSON API to read Star Wars data and publish that data into the project every five seconds. <br>**Note:** Use this example with SAS Event Stream Processing 2023.12 and later.|
| [source](/InputStreams/source) | Using connectors in Source windows.<br>This example demonstrates how you can use connectors to feed data from a variety of data sources into Source windows. |

### Transformations

The [Transformations](/Transformations) directory contains projects {{description}}.

| Example | Description |
| ------ | ------ |
| [aggregate](/Transformations/aggregate) | Use the different types of aggregation functions supported by the Aggregate window.<br>This example demonstrates how to use the Aggregate window and the different types of aggregation functions that it supports. Aggregate windows enable you to add simple statistics such as sum, mean, and standard deviation to streaming data. Because these calculations are provided out of the box and implemented on streaming data, they are fast and match the rate of the incoming data.|
| [compute](/Transformations/compute) | Use a Compute window to match people from the city of Apex.<br>You can use Compute windows to project input fields from one event to a new event and to augment this event with fields that result from a calculation. |
| [copy](/Transformations/copy) | Use a Copy window and different retention methods.<br>This example demonstrates how Copy windows operate and the different types of retention that they support. |
| [filter](/Transformations/filter) | Use a Filter window.<br>This example demonstrates how Filter windows operate. |
| [join](/Transformations/join) | Use Join windows with different join types. <br>This example demonstrates different ways to use Join windows. Join windows enable you to combine streaming data from multiple sources based on specific join conditions.|
| [lua_compute](/Transformations/lua_compute) | Use Lua code to modify user data.<br>The Lua window in this example is used as an alternative to a Compute window. <br>**Note:** Use this example with SAS Event Stream Processing 2021.2.1 and later.|
| [lua_module](/Transformations/lua_module) | Use a Lua module.<br>This example demonstrates how you can define useful functions in a Lua module at project level and reference those functions from other Lua code in the project. <br>**Note:** Use this example with SAS Event Stream Processing 2023.12 and later.|
| [lua_parse](/Transformations/lua_parse) | Use Lua code to parse JSON data and generate multiple events.<br>This example contains two projects. The Lua window in these projects is used as an alternative to a Functional window. The Basic Example Project contains step-by-step instructions about how to run the project. The Advanced Example Project is for demonstration purposes. <br>**Note:** Use these examples with SAS Event Stream Processing 2022.10 and later.|
| [lua_snippet](/Transformations/lua_snippet) |Use a Lua snippet.<br>This example simulates health-care data streaming into a model and detects measurements that fall outside a specified range. A Lua snippet in the project subscribes to windows, stores values, and reads a JSON file. Lua connectors are also used to generate and inject data. <br>**Note:** Use this example with SAS Event Stream Processing 2023.04 and later.|
| [lua_state](/Transformations/lua_state) | Use Lua code to maintain and use event state to generate events.<br>The Lua window in this project generates events every time a new stock symbol price exceeds the current maximum price for that stock symbol. <br>**Note:** Use these examples with SAS Event Stream Processing 2022.10 and later.|
| [python_compute](/Transformations/python_compute) | Use Python code to modify user data.<br>The Python window in this example is used as an alternative to a Compute window. <br>**Note:** Use this example with SAS Event Stream Processing 2024.03 and later.|
| [python_module](/Transformations/python_module) | Use a Python module.<br>This example demonstrates how you can define useful functions in a Python module at project level and reference those functions from other Python code in the project. <br>**Note:** Use this example with SAS Event Stream Processing 2024.02 and later.|
| [python_snippet](/Transformations/python_snippet) | Use a Python snippet.<br>This example provides a simple demonstration of how to define a Python snippet and reference it. <br>**Note:** Use this example with SAS Event Stream Processing 2024.02 and later.|
| [removestate](/Transformations/removestate) | Transition a model from stateful to stateless.<br>This example demonstrates how to facilitate the transition of a stateful part of a model to a stateless part of a model.|
| [splitter](/Transformations/splitter) | Use a splitter.<br>You can use expressions to define window-output splitter-slot calculations (for example, you can use an expression to evaluate where to send a generated event). In this project, the splitter works with user-defined functions to calculate the slot number to decide which Copy window the event goes to. |
| [transpose_long](/Transformations/transpose_long) | Transpose data from an aircraft, in long mode.<br>This project conceptualizes an event as a row that consists of multiple columns. You can use a Transpose window to interchange an event's rows as columns, and columns as rows. You will process information about the pitch, yaw, roll, and velocity of an aircraft in flight.|
| [transpose_wide](/Transformations/transpose_wide) | Transpose data from an aircraft, in wide mode.<br>This project conceptualizes an event as a row that consists of multiple columns. You can use a Transpose window to interchange an event's rows as columns, and columns as rows. You will process information about the pitch, yaw, roll, and velocity of an aircraft in flight.|
| [union](/Transformations/union) | Merge three event streams of stock market trades together.<br> A Union window unites two or more event streams using a strict policy or a loose policy.|

### Utilities

The [Utilities](/Utilities) directory contains projects {{description}}.

| Example | Description |
| ------ | ------ |
| [counter](/Utilities/counter) | Use Counter windows to monitor throughput.<br>This example demonstrates how to use Counter windows to monitor throughput. |
| [forwarding](/Utilities/forwarding) | Use event forwarding.<br>This example demonstrates how event forwarding operates in Python windows. |
| [geofence](/Utilities/geofence) |Display a list of wanted vehicles found near critical infrastructure sites.<br>This example uses Join, Geofence, and Filter windows to match wanted vehicles that are in close proximity to critical infrastructure sites. <br>**Note:** Use this example with SAS Event Stream Processing 2024.01 and later.|
| [lua_pattern](/Utilities/lua_pattern) | Use Lua code to identify increases in a stock's price over time.<br>The Pattern window in this example uses Lua code to define events of interest (EOI) to be matched. <br>**Note:** Use this example with SAS Event Stream Processing 2024.03 and later.|
| [python_pattern](/Utilities/python_pattern) | Use Python code to identify decreases in a stock's price over time.<br>The Pattern window in this example uses Python code to define events of interest (EOI) to be matched. <br>**Note:** Use this example with SAS Event Stream Processing 2024.03 and later.|
| [state_db](/Utilities/state_db) | Use StateDB windows with Redis.<br>This example demonstrates how to use the StateDB Writer window and StateDB Reader window with the in-memory key–value database Redis.|

### Custom Windows

The [Custom Windows](/CustomWindows) directory contains projects that make use of user defined Custom Windows that can be found on the [Custom Windows GitHub](https://github.com/sassoftware/esp-studio-custom-windows/tree/main).

| Example | Description |
| ------ | ------ |
|[alert_suppression](/CustomWindows/alert_suppression) |Use the Alert Suppression Custom Window.<br>This project shows the basic usage of the Alert Suppression Custom Window to supress alerts based on an adjustable allowed frequency.<br>**Note:** Use this example with SAS Event Stream Processing 2025.05 and later. |
|[event_sorter](/CustomWindows/event_sorter) |Use the Event Sorter Custom Window.<br>This project shows the basic usage of the Event Sorter Custom Window to sort incoming events based on the time they were created opposed to when they were available to the event stream.<br>**Note:** Use this example with SAS Event Stream Processing 2025.05 and later. |
|[mathematical_operations](/CustomWindows/mathematical_operations) |Use the Mathematical Operations Custom Window.<br>This project shows the basic usage of the Mathematical Operations Custom Window to apply a selected mathematical operation to two numbers.<br>**Note:** Use this example with SAS Event Stream Processing 2025.05 and later. |

### Analytics

The [Analytics](/Analytics) directory contains projects that show how to use various algorithms that are packaged with SAS Event Stream Processing.

| Example | Description |
| ------ | ------ |
|[analytics_cepstrum](/Analytics/analytics_cepstrum) |Use the Cepstrum Transform (Cepstrum) algorithm.<br>A cepstrum results from taking the inverse Fourier transform of the logarithm of the estimated spectrum of a signal. This application is often used in speech analysis, specifically with voice detection.<!-- This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that uses the cepstrum algorithm to compute the cepstrum.--> |
|[analytics_changedetection](/Analytics/analytics_changedetection) | Use the Change Detection (ChangeDetection) algorithm.<br>With change detection, a stream of measures is monitored and an alert is raised when values deviate from what is expected. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives input data. 2. a Calculate window that runs the change detection algorithm on that data.--> |
|[analytics_correlation](/Analytics/analytics_correlation) | Use the streaming Pearson's correlation algorithm.<br>Pearson's correlation coefficient is the most common measure of how data correlate with one another. It shows the linear relationship between two sets of data. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that calculates the correlation between two variables from an incoming data stream and publishes the events in real time.--> |
|[analytics_dbscan](/Analytics/analytics_dbscan)| Use DBSCAN clustering.<br>It applies an insert-only input stream that consists of the following: 1. An ID that acts as the streams key. 2. An x coordinate of data. 3. A y coordinate of data. <!-- This project has a single continuous query with a Source window that receives the data to be scored, a Train window that generates and periodically updates the DBSCAN model, and a Score window that does the scoring. The model is controlled by the parameters specified in Train window. While the w_training Train window is fully parameterized, this example uses it to find which of two clusters the data points are closest to.--> |
|[analytics_distributionfitting](/Analytics/analytics_distributionfitting) | Use the Distribution Fitting algorithm.<br>The algorithm supports fitting a Weibull, Gamma, or Normal distribution to a variable in the incoming data stream. <!--The project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that fits a Weibull distribution to a variable from an incoming data stream and publishes the variable's functional parameters as results.-->|
|[analytics_fitstatistics](/Analytics/analytics_fitstatistics) | Use the FitStat (fit statistics) algorithm.<br>The goodness-of-fit of a statistical model describes how well a model fits a set of data. The measure summarizes the difference between observed values and predicted values of the model under consideration. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives scored data to be analyzed. 2. A Calculate window that calculates fit statistics and publishes the results.--> |
| [analytics_lagmonitoring](/Analytics/analytics_lagmonitoring) | Use the Lag Monitoring (LagMonitor) algorithm.<br>The Lag Monitoring algorithm computes the cross-correlation between a target time series and one or more additional time series. Results contain the selected lags and computed cross-correlation values that correspond to minimum, maximum, and maximum absolute value cross-correlations for each of the variables. <!--The project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that performs the LagMonitor calculation.--> |
|[analytics_logisticregression](/Analytics/analytics_logisticregression) | Use online logistic regression on streaming data.<br> This project has an insert-only input data stream that consists of the following: 1. An ID that acts as the stream's key. 2. A y coordinate of data. 3. 784 x coordinates. <!--The project has a single continuous query with 1. a Source window that receives data events to score 2. A Train window that generates and periodically updates the logistic regression model. 3. a Score window that performs the scoring.-->|
|[analytics_modelReader_digitalFilter](/Analytics/analytics_modelReader_digitalFilter) | Score data by using SODFIL.sasast.<br>This project shows how to use a Model Reader window to facilitate the scoring of an input data set using a pre-trained analytic store model. The analytic store model is SODFIL.sasast, which is a Digital Filter analytic store of Butterworth filter type. The analytic store was created using CAS. <!--This project contains a single continuous query that consists of the following: 1. A Source window, named Source1, that receives the input data set to be analyzed 2. A second Source window, named w_request, which receives a request event to load the ASTORE. 3. A Model Reader window, named w_reader, that receives request events that include the location and type of model, and publishes a model event that contains the ASTORE model to a Score window .4. A Score window, named Score1, which uses the model that it receives from the Model Reader window to perform scoring of the input data set.-->|
|[analytics_modelReader_RPCA](/Analytics/analytics_modelReader_RPCA) |Score data by using RPCA.sasast.<br>This project shows how to use a Model Reader window to facilitate the scoring of an input data set using a pre-trained analytic store model. The analytic store model is RPCA.sasast, which is a Robust Principal Components Analysis (RPCA) analytic store. The analytic store was created using CAS. <!--This project contains a single continuous query that consists of the following: 1. A Source window, called w_data, that receives the input data set to be analyzed. 2. A Model Reader window, called w_reader, which receives request events that include the location and type of an offline analytics store (ASTORE) model, and publishes a model event that contains the ASTORE to a score window. 3. A Score window, called w_score, which uses the model that it receives from the Model Reader window to perform scoring on the input data set.--> |
|[analytics_movingrelativerange](/Analytics/analytics_movingrelativerange) | Use the moving relative range (MRR) algorithm.<br>The moving relative range provides a measure of volatility for a nonstationary time series, where the mean and variance of the series changes over time. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to analyze. 2. A Calculate window that performs the moving relative range calculation.-->|
|[analytics_ROC](/Analytics/analytics_ROC) | Use the receiver operating curve characteristic (ROC) information algorithm.<br>ROC information shows the diagnostic ability of a classifier system as you vary its discrimination threshold. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that performs the ROC calculation.--> |
|[analytics_segmentedcorrelation](/Analytics/analytics_segmentedcorrelation) | Use the segmented correlation algorithm.<br>Segmented correlation is similar to autocorrelation. It specifies the correlation between the elements of a series and others from the same series that are separated from them by a specified interval. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that calculates the segmented correlation of a variable from an incoming data stream and publishes the results.-->|
|[analytics_STFT](/Analytics/analytics_STFT) | Use the Short-Time Fourier Transform (STFT) algorithm.<br>A Fourier transform decomposes a function of time into its underlying frequencies. The amplitude, offset, and rotation speed of every underlying cycle is returned by the function. STFT is commonly used to monitor the time-varying frequency content of a signal. It can be used in digital filters to detect anomalies in continuous streams of data. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that calculates STFTs on incoming data and publishes the results.--> |
|[analytics_streaminghistogram](/Analytics/analytics_streaminghistogram) | Use the streaming histogram algorithm.<br>The streaming histogram algorithm processes a stream of numerical data and puts it in bins to generate boundaries in order to create a histogram that fits the data. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to fit into a histogram. 2. A Calculate window that performs bucketing.--> |
|[analytics_subspacetracking](/Analytics/analytics_subspacetracking) | Use the Subspace Tracking (SST) algorithm.<br>When a data set contains a sequence of nx1 vectors: x(t), subspace tracking estimates the covariance matrix for each vector x(t) and then computes the first p principal eigenvectors of the covariance matrix. For each iteration at time t, the covariance matrix C(t) is obtained. SST can be applied to industrial data to detect outliers. Results can be used to identify potential errors before they occur. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the data to analyze. 2. A Calculate window that performs subspace tracking on the data.--> |
|[analytics_summary](/Analytics/analytics_summary) | Use the streaming summary statistics algorithm.<br>The algorithm is used in a Calculate window, which calculates univariate summary statistics for input variable data that it receives from a Source window. <!--The project contains a single continuous query comprised of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that computes summary statistics on incoming events and publishes the results.--> |
|[analytics_supportvectormachine](/Analytics/analytics_supportvectormachine) |Use a support vector machine.<br>Support vector machines are supervised learning models with associated algorithms. They apply classification and regression analysis on incoming data. You supply training examples and mark them as belonging to a category. A support vector machine builds a model that assigns new examples to that category. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives data events that stream the data to score. 2. A Train window that generates and periodically updates the vector machine model. 3. A Score window that performs the scoring.-->|
|[analytics_texttokenization](/Analytics/analytics_texttokenization) | Use a tokenization algorithm.<br>This project shows how to use the tokenization algorithm to perform text tokenization on streaming input. <!--The project contains a single continuous query that consists of the following: 1. A Source window that receives the text data to be analyzed. 2. A Calculate window that tokenizes the text in incoming data events and publishes the results.--> |
|[analytics_textvectorization](/Analytics/analytics_textvectorization) | Use the TextVectorization algorithm.<br>Vectorizing text creates maps from words or n-grams to vector space. A vector space is an algebraic model to represent text documents as vectors of identifiers (for example, index terms). <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives the text data to analyze. 2. A Calculate window that vectorizes text in incoming data events and publishes the results.--> |
|[analytics_TFIDF](/Analytics/analytics_TFIDF) | Use the Term Frequency - Inverse Document Frequency (TFIDF) algorithm.<br>TFIDF can be used as a weighing factor in text mining or general information searches. <!--This project contains a single continuous query that consists of the following: 1. A Source window that receives scored data from a Score window to be analyzed. 2. A Calculate window that runs the TFIDF algorithm.--> |
|[analytics_tSNE](/Analytics/analytics_tSNE) | Use the t-Distributed Stochastic Neighbor Embedding (t-SNE) algorithm.<br>The t-SNE algorithm is a machine learning algorithm for dimensionality reduction that is used to visualize high-dimensional data sets. <!--This project contains a single continuous query that consists of the following: 1. a Source window that receives data to be trained and scored. 2. a Train window that generates and periodically updates the t-SNE model 3. a Score window that performs the scoring.--> |
| [fitstat](/Analytics/fitstat) | Use the FitStat (fit statistics) algorithm.<br>The goodness-of-fit of a statistical model describes how well a model fits a set of data. The measures summarize the difference between observed values and predicted values of the model under consideration.  |
| [kmeans_clustering](/Analytics/kmeans_clustering) |This example demonstrates the use of k-means clustering on streaming data. It includes a Source window that ingests signal samples, and Train and Score windows that build the k-means model and assign each incoming event to its closest cluster in real time.|
| [linear_regression](/Analytics/linear_regression) |Build and update a linear regression model in real time.<br>This example demonstrates how to use SAS Event Stream Processing to build and continuously update a linear regression model on a high-dimensional stream of data in real time. |
| [short_time_fourier_transform](/Analytics/short_time_fourier_transform) | Perform short-time Fourier transform (STFT) on streaming data.<br>This example demonstrates how to perform short-time Fourier transform (STFT) analysis on streaming data.|

## Identifying Suitable Examples

### Examples with Practical Use Cases

The following examples contain practical use cases.
- activitytracker
- geofence
- onnx_object_detection
- onnx_pose_estimation
- onnx_voice_transcription
- sailing
- trades

### Examples that Contain Lua Code

The following examples demonstrate how you can use Lua code in projects.
- lua_compute
- lua_connector
- lua_module
- lua_parse
- lua_snippet
- lua_state
- lua_pattern
- trades
- sailing
- filter

### Examples that Contain Python Code

The following examples demonstrate how you can use Python code in projects.
- python_compute
- python_connector
- python_module
- python_pattern
- python_snippet
- geofence

### Examples That Use Computer Vision

The following examples use computer vision techniques.
- onnx_object_detection
- onnx_pose_estimation

### Examples that use Custom Windows

The following examples use custom windows.
- alert_suppression
- event_sorter
- mathematical_operations

<!--### What's New

**Optional**. If applicable to your project, list new features that users need to be aware of. This section might supplement the Changelog file from the repository and only highlight important changes.

### Prerequisites

**Optional**. Provide guidelines about any prerequisites for the setup of the user's environment. Prerequisites typically take the form of a list of required software that must be available. Each piece of software might require its own setup steps. Use lists and subtopics, as appropriate.

### Installation

**Required**. Provide step-by-step instructions to install your software project. Use subtopics and screenshots, as appropriate.  

## Getting Started

**Optional**. Instruct others about the initial tasks to get started using your project after they've installed it. This is a good place to include screenshots, animated GIFs, or short example videos.

### Running

**Optional**. Instruct others about the initial tasks to get started using your project after they've installed it. This is a good place to include screenshots, [asciinema](https://asciinema.org/) recordings, or short usage videos.

### Examples

**Optional**. Provide additional examples on how to use the software or point to further documentation. Make your project easy to learn and use!

### Troubleshooting

**Optional**. Provide workarounds and solutions to known problems. Organize troubleshooting information using subtopics, as appropriate.-->

## Contributing

We welcome your contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit contributions to this project. 

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

## Additional Resources

* [SAS Event Stream Processing Help Center](https://go.documentation.sas.com/doc/en/espcdc/default/espwlcm/home.htm)
* [SAS Event Stream Processing Learn and Support Page](https://support.sas.com/en/software/event-stream-processing-support.html)
