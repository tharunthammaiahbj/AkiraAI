Agents | Langflow Documentation[Skip to main content](#__docusaurus_skipToContent_fallback)[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)Search...CTRLK[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)

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
* Agents
On this page

Agent components in Langflow
============================

Agent components define the behavior and capabilities of AI agents in your flow.

Agents use LLMs as a reasoning engine to decide which of the connected tool components to use to solve a problem.

Tools in agentic functions are, essentially, functions that the agent can call to perform tasks or access external resources. A function is wrapped as a `Tool` object, with a common interface the agent understands. Agents become aware of tools through tool registration, where the agent is provided a list of available tools, typically at agent initialization. The `Tool` object's description tells the agent what the tool can do.

The agent then uses a connected LLM to reason through the problem to decide which tool is best for the job.

Use an agent in a flow[​](#use-an-agent-in-a-flow)
--------------------------------------------------

The [simple agent starter project](/starter-projects-simple-agent) uses an [agent component](#agent-component-agent-component) connected to URL and Calculator tools to answer a user's questions. The OpenAI LLM acts as a brain for the agent to decide which tool to use. Tools are connected to agent components at the **Tools** port.

![](/assets/images/starter-flow-simple-agent-6c6df85ce6d01bfafebe3e4247cefc83.png)

For a multi-agent example, see [Create a problem-solving agent](/agents-tool-calling-agent-component).

Agent component[​](#agent-component)
------------------------------------

This component creates an agent that can use tools to answer questions and perform tasks based on given instructions.

The component includes an LLM model integration, a system message prompt, and a **Tools** port to connect tools to extend its capabilities.

For more information on this component, see the [tool calling agent documentation](/agents-tool-calling-agent-component).

### Inputs[​](#inputs)

| Name | Type | Description |
| --- | --- | --- |
| agent\_llm | Dropdown | The provider of the language model that the agent will use to generate responses. |
| system\_prompt | String | Initial instructions and context provided to guide the agent's behavior. |
| tools | List | List of tools available for the agent to use. |
| input\_value | String | The input task or question for the agent to process. |
| add\_current\_date\_tool | Boolean | If true, adds a tool to the agent that returns the current date. |

### Outputs[​](#outputs)

| Name | Type | Description |
| --- | --- | --- |
| response | Message | The agent's response to the given input task. |

CSV Agent[​](#csv-agent)
------------------------

This component creates a CSV agent from a CSV file and LLM.

### Inputs[​](#inputs-1)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| path | File | Path to the CSV file |
| agent\_type | String | Type of agent to create (zero-shot-react-description, openai-functions, or openai-tools) |

### Outputs[​](#outputs-1)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | CSV agent instance |

CrewAI Agent[​](#crewai-agent)
------------------------------

This component represents an Agent of CrewAI, allowing for the creation of specialized AI agents with defined roles, goals, and capabilities within a crew.

For more information, see the [CrewAI documentation](https://docs.crewai.com/core-concepts/Agents/).

### Inputs[​](#inputs-2)

| Name | Display Name | Info |
| --- | --- | --- |
| role | Role | The role of the agent |
| goal | Goal | The objective of the agent |
| backstory | Backstory | The backstory of the agent |
| tools | Tools | Tools at agent's disposal |
| llm | Language Model | Language model that will run the agent |
| memory | Memory | Whether the agent should have memory or not |
| verbose | Verbose | Enables verbose output |
| allow\_delegation | Allow Delegation | Whether the agent is allowed to delegate tasks to other agents |
| allow\_code\_execution | Allow Code Execution | Whether the agent is allowed to execute code |
| kwargs | kwargs | Additional keyword arguments for the agent |

### Outputs[​](#outputs-2)

| Name | Display Name | Info |
| --- | --- | --- |
| output | Agent | The constructed CrewAI Agent object |

Hierarchical Crew[​](#hierarchical-crew)
----------------------------------------

This component represents a group of agents, managing how they should collaborate and the tasks they should perform in a hierarchical structure. This component allows for the creation of a crew with a manager overseeing the task execution.

For more information, see the [CrewAI documentation](https://docs.crewai.com/how-to/Hierarchical/).

### Inputs[​](#inputs-3)

| Name | Display Name | Info |
| --- | --- | --- |
| agents | Agents | List of Agent objects representing the crew members |
| tasks | Tasks | List of HierarchicalTask objects representing the tasks to be executed |
| manager\_llm | Manager LLM | Language model for the manager agent (optional) |
| manager\_agent | Manager Agent | Specific agent to act as the manager (optional) |
| verbose | Verbose | Enables verbose output for detailed logging |
| memory | Memory | Specifies the memory configuration for the crew |
| use\_cache | Use Cache | Enables caching of results |
| max\_rpm | Max RPM | Sets the maximum requests per minute |
| share\_crew | Share Crew | Determines if the crew information is shared among agents |
| function\_calling\_llm | Function Calling LLM | Specifies the language model for function calling |

### Outputs[​](#outputs-3)

| Name | Display Name | Info |
| --- | --- | --- |
| crew | Crew | The constructed Crew object with hierarchical task execution |

JSON Agent[​](#json-agent)
--------------------------

This component creates a JSON agent from a JSON or YAML file and an LLM.

### Inputs[​](#inputs-4)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| path | File | Path to the JSON or YAML file |

### Outputs[​](#outputs-4)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | JSON agent instance |

OpenAI Tools Agent[​](#openai-tools-agent)
------------------------------------------

This component creates an OpenAI Tools Agent using LangChain.

For more information, see the [LangChain documentation](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/openai_tools/).

### Inputs[​](#inputs-5)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent (must be tool-enabled) |
| system\_prompt | String | System prompt for the agent |
| user\_prompt | String | User prompt template (must contain 'input' key) |
| chat\_history | List[Data] | Optional chat history for the agent |
| tools | List[Tool] | List of tools available to the agent |

### Outputs[​](#outputs-5)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | OpenAI Tools Agent instance |

OpenAPI Agent[​](#openapi-agent)
--------------------------------

This component creates an OpenAPI Agent to interact with APIs defined by OpenAPI specifications.

For more information, see the LangChain documentation on OpenAPI Agents.

### Inputs[​](#inputs-6)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| path | File | Path to the OpenAPI specification file (JSON or YAML) |
| allow\_dangerous\_requests | Boolean | Whether to allow potentially dangerous API requests |

### Outputs[​](#outputs-6)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | OpenAPI Agent instance |

SQL Agent[​](#sql-agent)
------------------------

This component creates a SQL Agent to interact with SQL databases.

### Inputs[​](#inputs-7)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| database\_uri | String | URI of the SQL database to connect to |
| extra\_tools | List[Tool] | Additional tools to provide to the agent (optional) |

### Outputs[​](#outputs-7)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | SQL Agent instance |

Sequential Crew[​](#sequential-crew)
------------------------------------

This component represents a group of agents with tasks that are executed sequentially. This component allows for the creation of a crew that performs tasks in a specific order.

For more information, see the [CrewAI documentation](https://docs.crewai.com/how-to/Sequential/).

### Inputs[​](#inputs-8)

| Name | Display Name | Info |
| --- | --- | --- |
| tasks | Tasks | List of SequentialTask objects representing the tasks to be executed |
| verbose | Verbose | Enables verbose output for detailed logging |
| memory | Memory | Specifies the memory configuration for the crew |
| use\_cache | Use Cache | Enables caching of results |
| max\_rpm | Max RPM | Sets the maximum requests per minute |
| share\_crew | Share Crew | Determines if the crew information is shared among agents |
| function\_calling\_llm | Function Calling LLM | Specifies the language model for function calling |

### Outputs[​](#outputs-8)

| Name | Display Name | Info |
| --- | --- | --- |
| crew | Crew | The constructed Crew object with sequential task execution |

Sequential task agent[​](#sequential-task-agent)
------------------------------------------------

This component creates a CrewAI Task and its associated Agent, allowing for the definition of sequential tasks with specific agent roles and capabilities.

For more information, see the [CrewAI documentation](https://docs.crewai.com/how-to/Sequential/).

### Inputs[​](#inputs-9)

| Name | Display Name | Info |
| --- | --- | --- |
| role | Role | The role of the agent |
| goal | Goal | The objective of the agent |
| backstory | Backstory | The backstory of the agent |
| tools | Tools | Tools at agent's disposal |
| llm | Language Model | Language model that will run the agent |
| memory | Memory | Whether the agent should have memory or not |
| verbose | Verbose | Enables verbose output |
| allow\_delegation | Allow Delegation | Whether the agent is allowed to delegate tasks to other agents |
| allow\_code\_execution | Allow Code Execution | Whether the agent is allowed to execute code |
| agent\_kwargs | Agent kwargs | Additional kwargs for the agent |
| task\_description | Task Description | Descriptive text detailing task's purpose and execution |
| expected\_output | Expected Task Output | Clear definition of expected task outcome |
| async\_execution | Async Execution | Boolean flag indicating asynchronous task execution |
| previous\_task | Previous Task | The previous task in the sequence (for chaining) |

### Outputs[​](#outputs-9)

| Name | Display Name | Info |
| --- | --- | --- |
| task\_output | Sequential Task | List of SequentialTask objects representing the created task(s) |

Tool Calling Agent[​](#tool-calling-agent)
------------------------------------------

This component creates a Tool Calling Agent using LangChain.

### Inputs[​](#inputs-10)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| system\_prompt | String | System prompt for the agent |
| user\_prompt | String | User prompt template (must contain 'input' key) |
| chat\_history | List[Data] | Optional chat history for the agent |
| tools | List[Tool] | List of tools available to the agent |

### Outputs[​](#outputs-10)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | Tool Calling Agent instance |

Vector Store Agent[​](#vector-store-agent)
------------------------------------------

This component creates a Vector Store Agent using LangChain.

### Inputs[​](#inputs-11)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| vectorstore | VectorStoreInfo | Vector store information for the agent to use |

### Outputs[​](#outputs-11)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | Vector Store Agent instance |

Vector Store Router Agent[​](#vector-store-router-agent)
--------------------------------------------------------

This component creates a Vector Store Router Agent using LangChain.

### Inputs[​](#inputs-12)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| vectorstores | List[VectorStoreInfo] | List of vector store information for the agent to route between |

### Outputs[​](#outputs-12)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | Vector Store Router Agent instance |

XML Agent[​](#xml-agent)
------------------------

This component creates an XML Agent using LangChain.

The agent uses XML formatting for tool instructions to the Language Model.

### Inputs[​](#inputs-13)

| Name | Type | Description |
| --- | --- | --- |
| llm | LanguageModel | Language model to use for the agent |
| user\_prompt | String | Custom prompt template for the agent (includes XML formatting instructions) |
| tools | List[Tool] | List of tools available to the agent |

### Outputs[​](#outputs-13)

| Name | Type | Description |
| --- | --- | --- |
| agent | AgentExecutor | XML Agent instance |

[PreviousComponents overview](/components-overview)[NextData](/components-data)

* [Use an agent in a flow](#use-an-agent-in-a-flow)
* [Agent component](#agent-component)
  + [Inputs](#inputs)
  + [Outputs](#outputs)
* [CSV Agent](#csv-agent)
  + [Inputs](#inputs-1)
  + [Outputs](#outputs-1)
* [CrewAI Agent](#crewai-agent)
  + [Inputs](#inputs-2)
  + [Outputs](#outputs-2)
* [Hierarchical Crew](#hierarchical-crew)
  + [Inputs](#inputs-3)
  + [Outputs](#outputs-3)
* [JSON Agent](#json-agent)
  + [Inputs](#inputs-4)
  + [Outputs](#outputs-4)
* [OpenAI Tools Agent](#openai-tools-agent)
  + [Inputs](#inputs-5)
  + [Outputs](#outputs-5)
* [OpenAPI Agent](#openapi-agent)
  + [Inputs](#inputs-6)
  + [Outputs](#outputs-6)
* [SQL Agent](#sql-agent)
  + [Inputs](#inputs-7)
  + [Outputs](#outputs-7)
* [Sequential Crew](#sequential-crew)
  + [Inputs](#inputs-8)
  + [Outputs](#outputs-8)
* [Sequential task agent](#sequential-task-agent)
  + [Inputs](#inputs-9)
  + [Outputs](#outputs-9)
* [Tool Calling Agent](#tool-calling-agent)
  + [Inputs](#inputs-10)
  + [Outputs](#outputs-10)
* [Vector Store Agent](#vector-store-agent)
  + [Inputs](#inputs-11)
  + [Outputs](#outputs-11)
* [Vector Store Router Agent](#vector-store-router-agent)
  + [Inputs](#inputs-12)
  + [Outputs](#outputs-12)
* [XML Agent](#xml-agent)
  + [Inputs](#inputs-13)
  + [Outputs](#outputs-13)

Hi, how can I help you?

![](/img/langflow-icon-black-transparent.svg)![](https://www.facebook.com/tr?id=853345499983657&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1482048748489568&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1172982080582122&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=896532212496788&ev=PageView&noscript=1)