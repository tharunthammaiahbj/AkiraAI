Chat Memory | Langflow Documentation[Skip to main content](#__docusaurus_skipToContent_fallback)[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)Search...CTRLK[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)

* [Welcome to Langflow](/)
* [Get Started](/get-started-installation)
* [Starter Projects](/starter-projects-basic-prompting)
* [Tutorials](/tutorials-blog-writer)
* [Workspace](/workspace-overview)
* [Components](/components-overview)
* [Agents](/agents-overview)
* [Configuration](/configuration-api-keys)
* [Guides](/guides-chat-memory)
  + [Chat Memory](/guides-chat-memory)
  + [Data & Message](/guides-data-message)
  + [📚 New to LLMs?](/guides-new-to-llms)
* [Deployment](/deployment-docker)
* [Integrations](/integrations-assemblyai)
* [Contributing](/contributing-community)
* [API Reference](/api)


* Guides
* Chat Memory
On this page

Chat Memory
===========

Langflow allows every chat message to be stored, and a single flow can have multiple memory sessions. This enables you to create separate *memories* for agents to store and recall information as needed.

In any project, as long as there are [**Chat**](/components-io) being used, memories are always being stored by default. These are messages from a user to the AI or vice-versa.

To see and access this history of messages, Langflow features a component called [Message history](/components-helpers#memory-history). It retrieves previous messages and outputs them in structured format or parsed.

To learn the basics about memory in Langflow, check out the [Memory Chatbot](/tutorials-memory-chatbot) starter example.

Memories can be visualized and managed directly from the **Playground**. You can edit and remove previous messages to inspect and validate the AI’s response behavior. You can remove or edit previous messages to get your models acting just right.

![](/assets/images/playground-b2c623fb6849024570bc9bd5285309f5.png)

Modifying these memories will influence the behavior of the chatbot responses, as long as an agent uses them. Here you have the ability to remove or edit previous messages, allowing them to manipulate and explore how these changes affect model responses.

To modify chat memories, from the playground, click the **Options** menu of any session, and then select **Message Logs**.

![](/assets/images/logs-7deb7c1a822f826469d17856b9dcebb5.png)

Session ID[​](#4ee86e27d1004e8288a72c633c323703)
------------------------------------------------

---

Chat conversations store messages categorized by a `Session ID`. A single flow can host multiple session IDs, and different flows can also share the same one.

The **Chat Memory** component also retrieves message histories by `Session ID`, which users can change in the component's **Controls** pane.

![](/assets/images/chat-input-controls-pane-b60b21c923aa47a2265ae1775e693cb0.png)

By default, if the `Session ID` value is empty, it is set to the same value as `Flow ID`.

You can also display all messages stored across every flow and session by going to **Settings** > **Messages**.

![](/assets/images/settings-messages-d0ad3a8e3bea5f8896565c041946a919.png)

Store chat memory in an external database[​](#store-chat-memory-in-an-external-database)
----------------------------------------------------------------------------------------

Chat memory is retrieved from an external database or vector store using the [Chat Memory](/components-helpers#chat-memory) component.

Chat memory is stored to an external database or vector store using the [Store Message](/components-helpers#store-message) component.

The [**Chat Memories**](/components-memories) components provide access to their respective external databases **as memory**. This allows AIs to access external memory for persistence and context retention. For example, connect the **Chat Memory** component to an **AstraDBChatMemory** component to store the message history in an external Astra DB database.

This example stores and retrieves chat history from an [AstraDBChatMemory](/components-memories#astradbchatmemory-component) component with **Store Message** and **Chat Memory** components.

### Prerequisites[​](#prerequisites)

* [An OpenAI API key](https://platform.openai.com/)
* [An Astra DB vector database](https://docs.datastax.com/en/astra-db-serverless/get-started/quickstart.html) with:
  + Application Token
  + API Endpoint

### Connect the chat memory component to an external database[​](#connect-the-chat-memory-component-to-an-external-database)

1. Load the [Memory Chatbot](/tutorials-memory-chatbot) starter project. This starter project extends the basic prompting flow to include a chat memory component.
2. Add the [Store Message](/components-helpers#store-message) component to the flow. The **Store message** component stores messages in the external database.
3. Add the [AstraDBChatMemory Component](/components-memories#astradbchatmemory-component) to the flow. The **Astra DB Chat Memory** component stores and retrieves messages from **Astra DB**.
4. Configure the **AstraDBChatMemory** component with your AstraDB instance details.
   1. In the **Astra DB Application Token** field, add your Astra token. (`AstraCS:...`)
   2. In the **API Endpoint** field, add your Astra database's endpoint. (for example, `https://12adb-bc-5378c845f05a6-e0a12-bd889b4-us-east-2.apps.astra.datastax.com`)
5. Connect the **AstraDBChatMemory** component output to the external memory inputs of the [Chat Memory](/components-helpers#chat-memory) and [Store Message](/components-helpers#store-message) components.
6. Link the [Chat Output](/components-io#chat-output) component to the input of the [Store Message](/components-helpers#store-message) component.

Your completed flow should look like this:

![](/assets/images/astra_db_chat_memory_rounded-9746ca2bb69d3b07ac0a071f4b9471b3.png)

1. In Langflow, create message traffic by running a flow.
2. Inspect your Astra database's tables and activity. You will see new tables and traffic created.
[PreviousSecurity best practices](/configuration-security-best-practices)[NextData & Message](/guides-data-message)

* [Session ID](#4ee86e27d1004e8288a72c633c323703)
* [Store chat memory in an external database](#store-chat-memory-in-an-external-database)
  + [Prerequisites](#prerequisites)
  + [Connect the chat memory component to an external database](#connect-the-chat-memory-component-to-an-external-database)

Hi, how can I help you?

![](/img/langflow-icon-black-transparent.svg)![](https://www.facebook.com/tr?id=853345499983657&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1482048748489568&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1172982080582122&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=896532212496788&ev=PageView&noscript=1)