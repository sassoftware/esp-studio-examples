# Importing the Grafana Dashboard

Before you import the dashboard, you need to update the `grafana.json` file for your environment:

1. Download the `grafana.json` file to your system.
2. Update any placeholders in the dashboard file. Depending on your data source, follow the appropriate steps:
- If you are using an internal discovery service, replace all instances of `%NAMESPACE%` with the Kubernetes namespace where SAS Event Stream Processing and Grafana are running. You can do this manually or through your command line interface (CLI).
    - For PowerShell, use the following command: 
      ```
      (Get-Content grafana.json) -replace '%NAMESPACE%', 'your-namespace' | Set-Content grafana.json
      ```
    - For bash, use the following command: 
      ```
      sed -i 's/%NAMESPACE%/your-namespace/g' grafana.json
      ```
- If you are using an external discovery service URL, replace all instances of `%DOMAIN%` with the domain name where your ESP Project is running. You can do this manually or through your CLI.
    - For PowerShell, use the following command: 
      ```
      (Get-Content grafana.json) -replace '%DOMAIN%', 'my.server.com' | Set-Content grafana.json
      ```
    - For bash, use the following command: 
      ```
      sed -i 's/%DOMAIN%/my.server.com/g' grafana.json
      ```

After you have updated your `grafana.json` file, you must import the dashboard into Grafana:

1. In Grafana, select **Dashboards** from the navigation bar.
2. Click **New**.
3. From the drop-down list, select **Import**.
4. Click **Upload dashboard JSON file** and select your updated `grafana.json` file.
5. Click **Import**.
