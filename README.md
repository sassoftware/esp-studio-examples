# SAS Event Stream Processing Studio Examples

## Overview

This repository provides XML code examples that use SAS Event Stream Processing to process real-time streaming data. Project code is written to run in [SAS Event Stream Processing Studio](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/titlepage.htm). Use these examples with SAS Event Stream Processing 2020.1 and later, unless stated otherwise. For examples that run with earlier releases of SAS Event Stream Processing, visit [the SAS Event Stream Processing Code Examples download page](https://tds.sas.com/downloads/package.htm?pid=2421).

## Using the Examples

The directory for each example contains all the files that you need to run the project. Some examples are accompanied with a README or documentation in the SAS Help Center, with steps about how to use those specific examples. For any other examples, follow these general steps: 

1. Save the contents of the directory for a specific example to a convenient location on your computer.

2. Open SAS Event Stream Processing Studio and sign in with your credentials. For more information, see [Accessing SAS Event Stream Processing Studio](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p1p3kijcqed0tin1o1u6h4vlkeeu.htm). 

3. When you are using an edge server, you must manually start an ESP server. For more information, see [Add or Edit an ESP Server to run on an Edge Server](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n1sii3zbhqqsa2n1x003olcoahoy.htm). If you are using a Kubernetes cluster, an ESP server is created automatically on the cluster and you are not required to manually start it.

4. Import the project to SAS Event Stream Processing Studio. For more information, see [Import a Project](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n0qhr0p800gs68n18wbp96pu7txq.htm).

5. Open the project in SAS Event Stream Processing Studio Modeler and examine its contents. For more information, see [Using SAS Event Processing Studio Modeler](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n0bk8u840zhjd8n0z4c0fkei0a36.htm). 

6. Use test mode on each project to verify that it operates as intended. For more information, see [Running a Test](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p1xzbzbnvpspodn1h2jkzo9m9t7d.htm). 

**Note:** When you first enter the test mode you do not see data streaming through the model. This is expected behavior unless publisher connectors have been configured. In step 7, you publish events from the project's CSV file and data streams through the project.

7. When you run a project in test mode, in most cases you can publish events from the project's corresponding CSV file by clicking the Publish button. This enables you to send events to a Source window without configuring a publisher connector. The CSV file can reside in a convenient location on your computer without having to upload it to a Kubernetes persistent volume. For more information, see [Publish Events from a CSV file](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/p124n2fohetwqzn109gsdel6o1cj.htm). Alternatively, you can configure publisher connectors prior to running the project in test mode. For more information, see [Configure a File and Socket Connector](https://go.documentation.sas.com/doc/en/espcdc/default/espstudio/n0esv2n0cbbpgcn1r281krr1iv6q.htm#n0y87cwr7q5vo6n1qlfcey182vt6).

***Important:*** When connector groups are used (for example, in the `geofence` and `sailing` examples), it is not appropriate to publish events from the project's CSV file when in test mode. Instead, it is recommended that you configure publisher connectors to the relevant CSV file and connector groups in SAS Event Processing Modeller. Follow the instructions for each specific example.

**Note:** For projects that contain multiple Source windows, you *must* publish events for each Source window separately. You cannot publish events to multiple Source windows simultaneously.

## Directory Contents

### GettingStarted
The [GettingStarted](/GettingStarted) directory contains a set of projects to help you get started quickly. Window code contains a description that describes its purpose.

| Example | Description |
| ------ | ------ |
| [aggregate](/GettingStarted/aggregate) | Apply aggregation functions to a group of stock market trades.<br>When new events arrive in the Aggregate window, they are placed into aggregate groups. After a new event enters the event stream, the aggregation functions are called. The functions then modify the aggregation groups accordingly. Aggregate field calculation functions or expressions that are registered to the Aggregate window must appear in non-key fields, which in this project are `totalQuant` and `maxPrice`. |
| [compute](/GettingStarted/compute) | Use a Compute window to match people from the city of Apex.<br>You can use Compute windows to project input fields from one event to a new event and to augment this event with fields that result from a calculation. |
| [fitstat](/GettingStarted/fitstat) | Use the FitStat (fit statistics) algorithm.<br>The goodness-of-fit of a statistical model describes how well a model fits a set of data. The measures summarize the difference between observed values and predicted values of the model under consideration.  |
| [join](/GettingStarted/join) | Join stock market trades with the corresponding traders. <br>A Join window receives events from a left input window and a right input window. It produces a single output stream of joined events. Joined events are created according to a join type and join conditions.|
| [splitter](/GettingStarted/splitter) | Use a splitter.<br>You can use expressions to define window-output splitter-slot calculations (for example, you can use an expression to evaluate where to send a generated event). In this project, the splitter works with user-defined functions to calculate the slot number to decide which Copy window the event goes to. |

### Basic

The [Basic](/Basic) directory contains projects that demonstrate how to use a few windows. See also [GettingStarted](/GettingStarted).

| Example | Description |
| ------ | ------ |
| [lua_compute](/Basic/lua_compute) | Use Lua code to modify user data.<br>The Lua window in this example is used as an alternative to a Compute window. <br>**Note:** Use this example with SAS Event Stream Processing 2021.2.1 and later.|
| [lua_connector](/Basic/lua_connector) | Use a Lua connector.<br>This example contains a Source window with a Lua connector that reads RSS feeds from scientific sites and publishes them into the project. <br>**Note:** Use this example with SAS Event Stream Processing 2022.10 and later.|
| [lua_parse](/Basic/lua_parse) | Use Lua code to parse JSON data and generate multiple events.<br>This example contains two projects. The Lua window in these projects is used as an alternative to a Functional window. The Basic Example Project contains step-by-step instructions about how to run the project. The Advanced Example Project is for demonstration purposes. <br>**Note:** Use these examples with SAS Event Stream Processing 2022.10 and later.|
| [lua_state](/Basic/lua_state) | Use Lua code to maintain and use event state to generate events.<br>The Lua window in this project generates events every time a new stock symbol price exceeds the current maximum price for that stock symbol. <br>**Note:** Use these examples with SAS Event Stream Processing 2022.10 and later.|
| [pattern_empty_index](/Basic/pattern_empty_index) | Identify increases in a stock's price within a specific time interval.<br>The Pattern window uses Lua code to define events of interest (EOI) to be matched. <br>**Note:** Use this example with SAS Event Stream Processing 2022.1.2 and later.|
| [removestate](/Basic/removestate) | Transition a model from stateful to stateless.<br>This example demonstrates how to facilitate the transition of a stateful part of a model to a stateless part of a model.|
| [union](/Basic/union) | Merge three event streams of stock market trades together.<br> A Union window unites two or more event streams using a strict policy or a loose policy.|

### Advanced

The [Advanced](/Advanced) directory contains projects that demonstrate the use of a larger number of windows together, or that are otherwise more complex than examples in the [Basic](/Basic) or [GettingStarted](/GettingStarted) directories.

| Example | Description |
| ------ | ------ |
| [activitytracker](/Advanced/activitytracker) | Use a job template to deploy a project to an edge server.<br>This example processes GPS data from activity tracker devices worn by players in a football match. The example demonstrates how you can publish a project in SAS Event Stream Processing Studio to make it available in SAS Event Stream Manager, and then use a job template to deploy the project to an edge server. |
| [geofence](/Advanced/geofence) |Display a list of wanted vehicles found near critical infrastructure sites.<br>This example uses Join, Geofence, and Filter windows to match wanted vehicles that are in close proximity to critical infrastructure sites.|
| [lua_snippet](/Advanced/lua_snippet) |Use a Lua snippet.<br>This example simulates health-care data streaming into a model and detects measurements that fall outside a specified range. A Lua snippet in the project subscribes to windows, stores values, and reads a JSON file. Lua connectors are also used to generate and inject data. <br>**Note:** Use this example with SAS Event Stream Processing 2023.04 and later.|
| [onnx_object_detection](/Advanced/onnx_object_detection) | Use an ONNX model to detect objects.<br>This example demonstrates how to use a project to reference an open-source ONNX model, in order to detect objects in still images. <br>**Note:** Use this example with SAS Event Stream Processing 2021.2.2 and later.|
| [sailing](/Advanced/sailing) | Visualize data obtained from a set of boats.<br>This example identifies two geographical areas of interest. One area is an exclusion zone that the boats identified are not permitted to enter. The other is an area where a speed restriction has been applied.|
| [slot_exp_xml](/Advanced/slot_exp_xml) | Split events across output slots.<br>The Compute window in this example determines which output slot or slots should be used for each stock market event. Three Copy windows connect to the Compute window using different output slots.|
| [trades](/Advanced/trades) | Identify large trades in stock market transactions.<br>This project identifies large securities transactions and the traders who were involved in those trades.|
| [transpose_long](/Advanced/transpose_long) | Transpose data from an aircraft, in long mode.<br>This project conceptualizes an event as a row that consists of multiple columns. You can use a Transpose window to interchange an event's rows as columns, and columns as rows. You will process information about the pitch, yaw, roll, and velocity of an aircraft in flight.|
| [transpose_wide](/Advanced/transpose_wide) | Transpose data from an aircraft, in wide mode.<br>This project conceptualizes an event as a row that consists of multiple columns. You can use a Transpose window to interchange an event's rows as columns, and columns as rows. You will process information about the pitch, yaw, roll, and velocity of an aircraft in flight.|

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
| [analytics_kmeans](/Analytics/analytics_kmeans) | Use k-means clustering.<br> K-means clustering is often used in data mining. The algorithm assigns data points to their nearest cluster centroid. Each cluster centroid is then recomputed based on the average of the cluster's data points. In k-means clustering, an input event is augmented with a cluster number. This indicates the cluster that the observation falls into.|
| [analytics_lagmonitoring](/Analytics/analytics_lagmonitoring) | Use the Lag Monitoring (LagMonitor) algorithm.<br>The Lag Monitoring algorithm computes the cross-correlation between a target time series and one or more additional time series. Results contain the selected lags and computed cross-correlation values that correspond to minimum, maximum, and maximum absolute value cross-correlations for each of the variables. <!--The project contains a single continuous query that consists of the following: 1. A Source window that receives the data to be analyzed. 2. A Calculate window that performs the LagMonitor calculation.--> |
|[analytics_linearregression](/Analytics/analytics_linearregression) | Use online linear regression on streaming data.<br> This project has an insert-only input stream that consists of the following: 1. An ID that acts as the streams key. 2. A y coordinate of data. 3. 784 x coordinates. <!--The project has a single continuous query with a Source window that receives the data to be scored. 2. a Train window that generates and periodically updates the linear regression model. 3. a Score window that performs online scoring.-->  |
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

## Identifying Suitable Examples

### Examples with Practical Use Cases

The following examples in the [Advanced](/Advanced) directory contain practical use cases.

- activitytracker
- geofence
- onnx_object_detection
- sailing
- trades

### Examples that Contain Lua Code

The following examples demonstrate how you can use Lua code in projects.
- lua_compute
- lua_connector
- lua_parse
- lua_snippet
- lua_state
- geofence
- pattern_empty_index
- trades

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
