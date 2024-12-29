Components overview | Langflow Documentation[Skip to main content](#__docusaurus_skipToContent_fallback)[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)Search...CTRLK[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)

* [Welcome to Langflow](/)
* [Get Started](/get-started-installation)
* [Starter Projects](/starter-projects-basic-prompting)
* [Tutorials](/tutorials-blog-writer)
* [Workspace](/workspace-overview)
* [Components](/components-overview)
  + [Components overview](/components-overview)
  + [Agents](/components-agents)
  + [Data](/components-data)
  + [Embeddings](/components-embedding-models)
  + [Helpers](/components-helpers)
  + [Inputs and outputs](/components-io)
  + [Loaders](/components-loaders)
  + [Logic](/components-logic)
  + [Memories](/components-memories)
  + [Models](/components-models)
  + [Prompts](/components-prompts)
  + [Tools](/components-tools)
  + [Vector stores](/components-vector-stores)
  + [Create custom components](/components-custom-components)
* [Agents](/agents-overview)
* [Configuration](/configuration-api-keys)
* [Guides](/guides-chat-memory)
* [Deployment](/deployment-docker)
* [Integrations](/integrations-assemblyai)
* [Contributing](/contributing-community)
* [API Reference](/api)


* Components
* Components overview
On this page

Components overview
===================

A component is a single building block within a flow with inputs, outputs, functions, and parameters that define its functionality. A single component is like a class within a larger application.

To add a component to a flow, drag it from the **Component** menu to the **Workspace**.

Learn more about components and how they work on this page.

Component menu[​](#component-menu)
----------------------------------

Each component is unique, but all have a menu bar at the top that looks something like this.

![](/img/openai-model-component.png)

Use these controls to do the following:

* **Code** — Modify the component's Python code and save your changes.
* **Controls** — Adjust all component parameters.
* **Freeze Path** — After a component runs, lock its previous output state to prevent it from re-running.

Click **All** to see additional options for a component.

To view a component’s output and logs, click the **Visibility** icon.

To run a single component, click ▶️ **Play**. A ✅**Check** indicates that the component ran successfully.

Component ports[​](#component-ports)
------------------------------------

Handles () on the side of a component indicate the types of inputs and outputs that can be connected at that port. Hover over a handle to see connection details.

![](/img/prompt-component.png)
### Component port data type colors[​](#component-port-data-type-colors)

The following table lists the handle colors and their corresponding data types:

| Data Type | Handle Color | Hex Code |
| --- | --- | --- |
| BaseLanguageModel | Fuchsia | #c026d3 |
| Data | Red | #dc2626 |
| Document | Lime | #65a30d |
| Embeddings | Emerald | #10b981 |
| LanguageModel | Fuchsia | #c026d3 |
| Message | Indigo | #4f46e5 |
| Prompt | Violet | #7c3aed |
| str | Indigo | #4F46E5 |
| Text | Indigo | #4F46E5 |
| unknown | Gray | #9CA3AF |

Freeze Path[​](#freeze-path)
----------------------------

After a component runs, **Freeze Path** locks the component's previous output state to prevent it from re-running.

If you’re expecting consistent output from a component and don’t need to re-run it, click **Freeze Path**.

Enabling **Freeze Path** freezes all components downstream of the selected component.

Additional component options[​](#additional-component-options)
--------------------------------------------------------------

Click **All** to see additional options for a component.

To modify a component's name or description, double-click in the **Name** or **Description** fields. Component descriptions accept markdown syntax.

### Component shortcuts[​](#component-shortcuts)

The following keyboard shortcuts are available when a component is selected.

| Menu Item | Mac Shortcut | Description |
| --- | --- | --- |
| Code | ⌘ + C | Opens the code editor for the component. |
| Advanced | ⌘ + A | Opens advanced settings for the component. |
| Save | ⌘ + S | Saves the current state of the component to Saved components in the sidebar. |
| Duplicate | ⌘ + D | Creates a duplicate of the component. |
| Copy | ⌘ + C | Copies the selected component. Paste it in the workspace with ⌘ + V. |
| Docs | ⌘ + D | Opens related documentation. |
| Minimize | ⌘ + Q | Minimizes the current component. |
| Freeze | ⌘ + F | Freezes the current component state. |
| Freeze Path | ⌘ + F | Freezes the current component state and all upstream components. |
| Download | ⌘ + D | Downloads the current component as a JSON file. |
| Delete | ⌘ + ⌫ | Deletes the component. |

Group components in the workspace[​](#group-components-in-the-workspace)
------------------------------------------------------------------------

Multiple components can be grouped into a single component for reuse. This is useful when combining large flows into single components (like RAG with a vector database, for example) and saving space.

1. Hold **Shift** and drag to select components.
2. Select **Group**.
3. The components merge into a single component.
4. Double-click the name and description to change them.
5. Save your grouped component to in the sidebar for later use.

Component version[​](#component-version)
----------------------------------------

A component's state is stored in a database, while sidebar components are like starter templates. As soon as you drag a component from the sidebar to the workspace, the two components are no longer in parity.

The component will keep the version number it was initialized to the workspace with. Click the **Update Component** icon (exclamation mark) to bring the component up to the `latest` version. This will change the code of the component in place so you can validate that the component was updated by checking its Python code before and after updating it.

[PreviousPlayground](/workspace-playground)[NextAgents](/components-agents)

* [Component menu](#component-menu)
* [Component ports](#component-ports)
  + [Component port data type colors](#component-port-data-type-colors)
* [Freeze Path](#freeze-path)
* [Additional component options](#additional-component-options)
  + [Component shortcuts](#component-shortcuts)
* [Group components in the workspace](#group-components-in-the-workspace)
* [Component version](#component-version)

Hi, how can I help you?

![](/img/langflow-icon-black-transparent.svg)![](https://www.facebook.com/tr?id=853345499983657&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1482048748489568&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1172982080582122&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=896532212496788&ev=PageView&noscript=1)