# Importing the Grafana Dashboard

Before you import the dashboard, you need to update the `grafana.json` file for your environment.

## 1. Download the Dashboard File

- Download the `grafana.json` file to your system.

## 2. Update Placeholders in the Dashboard File

Depending on your datasource, follow the appropriate steps below.

### A. If Using an Internal Discovery Service

Replace all instances of `%NAMESPACE%` with the Kubernetes namespace where SAS Event Stream Processing and Grafana are running.

**How to Replace:**

- **Manually:** Open `grafana.json` in a text editor, find and replace all occurrences of `%NAMESPACE%` with your namespace.
- **Command Line:**
    - **Windows (PowerShell):**
      ```
      (Get-Content grafana.json) -replace '%NAMESPACE%', 'your-namespace' | Set-Content grafana.json
      ```
    - **Linux (bash):**
      ```
      sed -i 's/%NAMESPACE%/your-namespace/g' grafana.json
      ```

### B. If Using an External Discovery Service URL

Replace all instances of `%DOMAIN%` with the domain name where your ESP Project is running.

**How to Replace:**

- **Manually:** Open `grafana.json` in a text editor, find and replace all occurrences of `%DOMAIN%` with your domain.
- **Command Line:**
    - **Windows (PowerShell):**
      ```
      (Get-Content grafana.json) -replace '%DOMAIN%', 'my.server.com' | Set-Content grafana.json
      ```
    - **Linux (bash):**
      ```
      sed -i 's/%DOMAIN%/my.server.com/g' grafana.json
      ```

## 3. Import the Dashboard into Grafana

1. In Grafana, go to **Dashboards** from the navigation bar.
2. Click **New**.
3. Select **Import** from the dropdown list.
4. Click **Upload dashboard JSON file** and select your updated `grafana.json`.
5. Click **Import**.

---
**Summary:**  
Download the dashboard file, update the placeholders for your environment, and import it into Grafana.
