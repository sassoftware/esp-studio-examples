# Importing the Grafana Dashboard

Before you begin the process of importing the Grafana dashboard, make sure you have the following prerequisites:
- The SAS Event Stream Processing and Grafana services running on the same cluster.
- The SAS Event Stream Processing Data Source Plug-in for Grafana installed and configured. For more information, see [SAS Event Stream Processing Data Source Plug-in for Grafana](https://github.com/sassoftware/grafana-esp-plugin/blob/main/README.md#add-the-sas-event-stream-processing-data-source).
- A data source configured in Grafana for the SAS Event Stream Processing Studio application. For more information, see [Add the SAS Event Stream Processing Data Source](https://github.com/sassoftware/grafana-esp-plugin/blob/main/README.md#add-the-sas-event-stream-processing-data-source).
- The Example ESP Project has been installed onto the SAS Event Stream Processing Studio application and is running in test mode. For more information, see [Using the Examples](../README.md#using-the-examples).

Before you import the dashboard, you must update `grafana.json` for your environment because the ESP Server connection URL is different in each cluster.

1. Download the `grafana.json` file to your system.
2. Find the Kubernetes namespace where SAS Event Stream Processing and Grafana are running.
3. You can get the namespace from SAS Event Stream Processing Studio or from your command line interface (CLI).
   - In ESP Studio, open a project. In the toolbar, open the `ESP server` drop-down list. The namespace appears next to the Kubernetes Cluster icon.
   - In a CLI, use the following command:
   ```
   kubectl get deployment sas-event-stream-processing-studio-app -o jsonpath="{.metadata.namespace}"
   ```
4. Replace all instances of `%NAMESPACE%` with the Kubernetes namespace.
5. You can do this manually or through your command line interface (CLI).
    - For PowerShell, use the following command:
      ```
      (Get-Content grafana.json) -replace '%NAMESPACE%', 'your-namespace' | Set-Content grafana.json
      ```
    - For bash, use the following command:
      ```
      sed -i 's/%NAMESPACE%/your-namespace/g' grafana.json
      ```

After you have updated your `grafana.json` file, you must import the dashboard into Grafana:

1. In Grafana, select **Dashboards** from the navigation bar.
2. Click **New**.
3. From the drop-down list, select **Import**.
4. Click **Upload dashboard JSON file** and select your updated `grafana.json` file.
5. Enter a Name for the dashboard.
6. Select a Folder for the dashboard.
7. If required, change the Unique identifier (UID) by clicking the **Change uid** button and giving the dashboard a unique identifier.
8. From the SAS Event Stream Processing Datasource drop-down list, select the datasource that you configured with the SAS Event Stream Processing Studio application.
9. Click **Import**.

