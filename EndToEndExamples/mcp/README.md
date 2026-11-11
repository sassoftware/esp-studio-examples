# Using ESP MCP to Expose Real-Time Analytics as AI Tools

## Why use ESP MCP with LLMs?

SAS Event Stream Processing (ESP) is designed to process streaming data in real time. This value can be enhanced when business users, analysts, and AI assistants can ask for live operational insights without needing to understand the underlying event stream, data model, or project logic.

Model Context Protocol (MCP) bridges that gap by allowing an ESP project expose project logic and operations as structured, discoverable capabilities:

- Tools for actions such as publishing data, querying state, or scoring models
- Prompts that package common tasks and expected inputs
- Apps that provide chatbots with a rich user interface

Through these primitives, ESP MCP enables an MCP client (such as an LLM) to combine:

- real-time streaming analytics,
- project logic that already exists in ESP,
- operational tools exposed in a consistent way,
- and a governed set of actions that can be invoked by an MCP client.

That is the value of ESP MCP: it allows AI systems to work with live data pipelines and decision logic, rather than substituting a generic chat interface for a real-time analytics engine.

This example uses the sailing use case to demonstrate that pattern in a practical way. It shows how a boat telemetry stream can be translated into MCP tools that an LLM can use to answer questions or trigger actions against the project.

## Use Case

This example is based on the sailing example, which identifies two geographic areas of interest:

- a dockyard exclusion zone that boats are not permitted to enter
- a marina where a speed restriction is applied

The project reads boat telemetry from CSV files and processes it through a sequence of windows that:

- ingest boat positions,
- unify and enrich events,
- evaluate whether a boat is inside the exclusion zone,
- detect speeding events,
- retain recent state and aggregate important outcomes.

The MCP layer adds an AI-friendly interface on top of that project. It exposes reusable operations for an MCP client such as Claude, ChatGPT, VS Code, or SAS Retrieval Agent Manager.

The project contains several preconfigured MCP tools:

- PublishAreaOfInterest: publishes a new area-of-interest event into the Areas_Of_Interest stream
- QueryExclusionZoneViolations: queries recent exclusion-zone data from the relevant window
- ObtainSpeedingEvents: filters retained boat data using area name and speed threshold and returns the results
- CheckBoatInExclusionZone: submits a boat position to a scoring flow and returns whether that point is inside the exclusion zone

The ESP project also includes Python snippet logic for these operations. The logic is not the focus here; the main point is that the same business logic that runs in the streaming model can also be surfaced to AI clients through MCP.

For a more detailed description of the underlying sailing workflow, see the [sailing example](../sailing/README.md).

## MCP concepts in ESP Studio

At a high level, ESP supports three common MCP primitives:

- Tools: actions that the MCP client can call to perform work in the ESP project
- Prompts: predefined instructions or task templates that package common user tasks
- Apps: reusable user interfaces or task flows surfaced to the MCP client

In this example, the primary focus is on tools. However, the same project can also be used as a foundation for prompts and apps in real deployments.

The key idea is that an LLM does not need to know how to operate the ESP project directly. The LLM only needs to know which MCP tools are available, what they do, and what inputs they expect.

### ESP Studio: adding MCP tools and apps

In ESP Studio, MCP settings are configured as part of the project definition, alongside the streaming model. The typical flow is:

1. Design the ESP project and define its windows and logic.
2. Configure one or more MCP tools to expose the project actions.
3. Optionally define MCP apps and prompts for common use cases.
4. Run the project so the ESP server's MCP endpoint is exposed.
5. Connect an MCP client to that endpoint.

The following placeholders indicate where screenshots should be added to help users understand this flow.

![Image placeholder: ESP Studio project with the MCP configuration panel open](img/placeholder_mcp_project_config.png)

Caption: ESP Studio showing the project-level MCP configuration. The image should highlight where tools and other MCP capabilities are configured.

![Image placeholder: ESP Studio MCP tools list with PublishAreaOfInterest, ObtainSpeedingEvents, CheckBoatInExclusionZone, and QueryExclusionZoneViolations](img/placeholder_mcp_tools.png)

Caption: The MCP tools list for the sailing example. The screenshot should show the tool names, their types, and the input or output mapping they use.

![Image placeholder: ESP Studio MCP app or prompt configuration](img/placeholder_mcp_apps_prompts.png)

Caption: Example of how apps or prompts are added to an ESP project. The screenshot should emphasize that tools are only one part of the MCP surface; apps and prompts are also supported.

## Where the MCP endpoint is exposed

When the project is running, the ESP server exposes an MCP endpoint at:

- /eventStreamProcessing/v2/mcp

The exact URL depends on how and where the project is deployed. In a local developer setup it can be a local machine endpoint. In a Kubernetes deployment it can be a cluster-exposed endpoint behind the SAS Event Stream Processing service route or an ingress path. In a production deployment, the full address typically looks like this:

- https://<host>/SASEventStreamProcessingServer/<server-prefix>/eventStreamProcessing/v2/mcp

For example:

- https://<host</SASEventStreamProcessingServer/sailing_with_mcp/eventStreamProcessing/v2/mcp

## Deployment strategies

The same ESP project can be exposed through different deployment patterns. The main distinction is whether the project is running on a local machine or in a Kubernetes-based environment.

### Option 1: ESP Project Container

This is the simplest way to test MCP locally. An ESP Project Container built around this MCP example project must be available.

Typical setup steps:

1. Start the ESP Project Container containing the MCP example project from the command line. As part of the start command, the 31415 port should be published to the host machine.
2. The ESP Project Container exposes the MCP endpoint at a local URL, i.e. http://localhost:31415/eventStreamProcessing/v2/mcp.
3. Point your MCP-capable client to the local MCP endpoint. The MCP client must be able to reach local URLs.

This setup works well for local development because:

- there is no port forwarding requirement,
- the client and server are on the same machine or the same secure local network

The ESP Project Container can also used in SAS Retrieval Agent Manager as part of a container tool template. Typical setup steps:

1. Create a new container tool template.
2. Supply the URL relating to the ESP Project Container.
3. Set the Port to 31415.
3. Set the Base Path to `eventStreamProcessing/v2/mcp`.
4. Add your ESP license file.
5. Set the ESPENV_LICENSE environment variable to the path of the license file.

### Option 2: Kubernetes deployment using Test Mode

For a Kubernetes deployment, the project typically runs in SAS Event Stream Processing in a cluster or a project container environment.

Typical setup steps:

1. Open SAS Event Stream Processing Studio and import or install the example project.
2. Use Studio or ESM to run the project in Test Mode.
3. Confirm the service route is available in the cluster's internal or external network.
4. Connect the MCP client to the service endpoint at /eventStreamProcessing/v2/mcp.

This deployment model is useful when the project is intended to be accessed by multiple clients.

Important: there is no requirement to use port forwarding for the MCP client to connect. However, if the cluster is protected by SSL, the MCP client must be able to trust the cluster's certificate authority or have the appropriate CA certificates installed.

## How to connect clients to the MCP endpoint

The process to connect to the MCP endpoint differs between clients, but in general the MCP client must point to the ESP MCP endpoint and authenticate as required by the deployment.

### Claude Desktop

Claude Desktop steps here

### ChatGPT

ChatGPT steps here

### SAS Retrieval Agent Manager (RAM)

SAS Retrieval Agent Manager is particularly relevant because it is designed for orchestrated, workflow-style agent use cases that can combine retrieval and tool execution.

Typical steps:

1. Ensure the ESP server has the `SAS_ESP_SERVER_BASE_URL` environment variable set to the correct base URL for the ESP server.
2. In SAS Retrieval Agent Manager, create a new MCP Tool Server and select the Remote MCP Server template.
3. Provide the URL to the ESP server's MCP endpoint, e.g. https://<host>/SASEventStreamProcessingServer/<server-prefix>/eventStreamProcessing/v2/mcp.
4. Set Transport to HTTP.
5. Let SAS Retrieval Agent Manager discover the tools exposed by the ESP project.

![Image placeholder: RAM tool discovery screen showing the ESP MCP server and discovered tools](img/placeholder_ram_discovery.png)

Caption: SAS Retrieval Agent Manager discovering the sailing example tools from the ESP MCP server.

![Image placeholder: RAM workflow with an action invoking ObtainSpeedingEvents or QueryExclusionZoneViolations](img/placeholder_ram_workflow.png)

Caption: RAM workflow example showing a prompt or tool call that invokes an ESP MCP tool as part of an agent process.

### VS Code

VSCode steps here

## Testing the connection

The easiest way to validate the MCP endpoint before connecting an LLM client is to use the MCP Inspector.

The Model Context Protocol documentation provides a useful inspector for testing server connections and tool exposure:

- https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector

This is valuable because it lets you validate:

- the endpoint is reachable,
- the server exposes the expected tools,
- the input and output schema are correct,
- and the MCP client can call the tools successfully.

The inspector also supports apps as well as tools in current MCP implementations, so it is a good practical validation utility for both.

## Project files

The project contains the following files:

- [model.xml](model.xml): the ESP project definition, including the configured MCP tools
- [boat1.csv](boat1.csv), [boat2.csv](boat2.csv), [boat3.csv](boat3.csv), [boat4.csv](boat4.csv): boat telemetry input streams
- [geoArea.csv](geoArea.csv): geographic areas-of-interest input
- [README.md](README.md): project documentation

## Additional resources

- [SAS Event Stream Processing Studio Examples](https://github.com/sassoftware/esp-studio-examples)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)
- [SAS Event Stream Processing documentation](https://documentation.sas.com/doc/en/espcdc/default/home.htm)
- [The sailing example](../sailing/README.md)
