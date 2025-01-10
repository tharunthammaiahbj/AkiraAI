Summarize the raw documentation markdown, focusing on key points such as important definitions, processes, and steps. Ensure the summary is precise, relevant, and coherent, removing any redundant or non-essential information. Adapt to different markdown structures, ensuring clarity and completeness in the final summary.

API | Langflow Documentation[Skip to main content](#__docusaurus_skipToContent_fallback)[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)Search...CTRLK[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)

* [Welcome to Langflow](/)
* [Get Started](/get-started-installation)
* [Starter Projects](/starter-projects-basic-prompting)
* [Tutorials](/tutorials-blog-writer)
* [Workspace](/workspace-overview)
  + [Workspace concepts](/workspace-overview)
  + [API](/workspace-api)
  + [Logs](/workspace-logs)
  + [Playground](/workspace-playground)
* [Components](/components-overview)
* [Agents](/agents-overview)
* [Configuration](/configuration-api-keys)
* [Guides](/guides-chat-memory)
* [Deployment](/deployment-docker)
* [Integrations](/integrations-assemblyai)
* [Contributing](/contributing-community)
* [API Reference](/api)


* Workspace
* API
On this page

API
===

The **API** section presents code templates for integrating your flow into external applications.

![](/assets/images/api-pane-97a01b20a262676d4e21906df0e29f46.png)

### cURL[​](#4eb287a8424349c4b0b436a6703de5f3)

The **cURL** tab displays sample code for posting a query to your flow. Modify the `input_value` to change your input message. Copy the code and run it to post a query to your flow and get the result.

### Python API[​](#fb7db14e6330418389562ef647aa2354)

The **Python API** tab displays code to interact with your flow using the Python HTTP requests library.

### Python Code[​](#7af87438549b4972907ac310a4193067)

The **Python Code** tab displays code to interact with your flow's `.json` file using the Langflow runtime.

### Tweaks[​](#5680600063724590ac2302b4ddeea867)

The **Tweaks** tab displays the available parameters for your flow. Modifying the parameters changes the code parameters across all windows. For example, changing the **Chat Input** component's `input_value` will change that value across all API calls.

Send image files to your flow with the API[​](#send-image-files-to-your-flow-with-the-api)
------------------------------------------------------------------------------------------

Send image files to the Langflow API for AI analysis.

The default file limit is 100 MB. To configure this value, change the `LANGFLOW_MAX_FILE_SIZE_UPLOAD` environment variable. For more information, see [Supported environment variables](/environment-variables#supported-variables).

1. To send an image to your flow with the API, POST the image file to the `v1/files/upload/<YOUR-FLOW-ID>` endpoint of your flow.

 `_10curl -X POST "http://127.0.0.1:7860/api/v1/files/upload/a430cc57-06bb-4c11-be39-d3d4de68d2c4" \_10 -H "Content-Type: multipart/form-data" \_10 -F "file=@image-file.png"`

The API returns the image file path in the format `"file_path":"<YOUR-FLOW-ID>/<TIMESTAMP>_<FILE-NAME>"}`.

 `_10{"flowId":"a430cc57-06bb-4c11-be39-d3d4de68d2c4","file_path":"a430cc57-06bb-4c11-be39-d3d4de68d2c4/2024-11-27_14-47-50_image-file.png"}`

1. Post the image file to the **Chat Input** component of a **Basic prompting** flow. Pass the file path value as an input in the **Tweaks** section of the curl call to Langflow.

 `_12curl -X POST \_12 "http://127.0.0.1:7860/api/v1/run/a430cc57-06bb-4c11-be39-d3d4de68d2c4?stream=false" \_12 -H 'Content-Type: application/json'\_12 -d '{_12 "output_type": "chat",_12 "input_type": "chat",_12 "tweaks": {_12 "ChatInput-b67sL": {_12 "files": "a430cc57-06bb-4c11-be39-d3d4de68d2c4/2024-11-27_14-47-50_image-file.png",_12 "input_value": "what do you see?"_12 }_12}}'`

Your chatbot describes the image file you sent.

 `_10"text": "This flowchart appears to represent a complex system for processing financial inquiries using various AI agents and tools. Here’s a breakdown of its components and how they might work together..."`

Chat Widget[​](#48f121a6cb3243979a341753da0c2700)
-------------------------------------------------

---

The **Chat Widget HTML** tab displays code that can be inserted in the `<body>` of your HTML to interact with your flow.

The **Langflow Chat Widget** is a powerful web component that enables communication with a Langflow project. This widget allows for a chat interface embedding, allowing the integration of Langflow into web applications effortlessly.

You can get the HTML code embedded with the chat by clicking the Code button at the Sidebar after building a flow.

Clicking the Chat Widget HTML tab, you'll get the code to be inserted. Read below to learn how to use it with HTML, React and Angular.

### Embed your flow into HTML[​](#6e84db2f2a0d451db6fa03c57e9bf9a4)

The Chat Widget can be embedded into any HTML page, inside a `<body>` tag, as demonstrated in the video below.

### Embed your flow with React[​](#fe5d3b1c42e74e4c84ebc9d1799b7665)

To embed the Chat Widget using React, insert this `<script>` tag into the React *index.html* file, inside the `<body>`tag:

 `_10<script src="https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@main/dist/build/static/js/bundle.min.js"></script>`

Declare your Web Component and encapsulate it in a React component.

 `_10declare global { namespace JSX { interface IntrinsicElements { "langflow-chat": any; } }}export default function ChatWidget({ className }) { return ( <div className={className}> <langflow-chat chat_inputs='{"your_key":"value"}' chat_input_field="your_chat_key" flow_id="your_flow_id" host_url="langflow_url" ></langflow-chat> </div> );}`

Finally, you can place the component anywhere in your code to display the Chat Widget.

### Embed your flow with Angular[​](#4fd87355b9aa409894acfbb9e1497980)

To use the chat widget in Angular, first add this `<script>` tag into the Angular *index.html* file, inside the `<body>` tag.

 `_10<script src="https://cdn.jsdelivr.net/gh/langflow-ai/langflow-embedded-chat@main/dist/build/static/js/bundle.min.js"></script>`

When you use a custom web component in an Angular template, the Angular compiler might show a warning when it doesn't recognize the custom elements by default. To suppress this warning, add `CUSTOM_ELEMENTS_SCHEMA` to the module's `@NgModule.schemas`.

* Open the module file (it typically ends with *.module.ts*) where you'd add the `langflow-chat` web component.
* Import `CUSTOM_ELEMENTS_SCHEMA` at the top of the file:

`import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from "@angular/core";`

* Add `CUSTOM_ELEMENTS_SCHEMA` to the 'schemas' array inside the '@NgModule' decorator:

 `_10@NgModule({ declarations: [ // ... Other components and directives ... ], imports: [ // ... Other imported modules ... ], schemas: [CUSTOM_ELEMENTS_SCHEMA], // Add the CUSTOM_ELEMENTS_SCHEMA here})export class YourModule {}`

In your Angular project, find the component belonging to the module where `CUSTOM_ELEMENTS_SCHEMA` was added. Inside the template, add the `langflow-chat` tag to include the Chat Widget in your component's view:

 `_10<langflow-chat chat_inputs='{"your_key":"value"}' chat_input_field="your_chat_key" flow_id="your_flow_id" host_url="langflow_url"></langflow-chat>`tip

`CUSTOM_ELEMENTS_SCHEMA` is a built-in schema that allows Angular to recognize custom elements. Adding `CUSTOM_ELEMENTS_SCHEMA` tells Angular to allow custom elements in your templates, and it will suppress the warning related to unknown elements like `langflow-chat`. Notice that you can only use the Chat Widget in components that are part of the module where you added `CUSTOM_ELEMENTS_SCHEMA`.

Chat Widget Configuration[​](#5ede4bbbd2ac43e29c90f3edb43cba58)
---------------------------------------------------------------

---

Use the widget API to customize your Chat Widget:

caution

Props with the type JSON need to be passed as stringified JSONs, with the format {"key":"value"}.

| Prop | Type | Required | Description |
| --- | --- | --- | --- |
| bot\_message\_style | JSON | No | Applies custom formatting to bot messages. |
| chat\_input\_field | String | Yes | Defines the type of the input field for chat messages. |
| chat\_inputs | JSON | Yes | Determines the chat input elements and their respective values. |
| chat\_output\_key | String | No | Specifies which output to display if multiple outputs are available. |
| chat\_position | String | No | Positions the chat window on the screen (options include: top-left, top-center, top-right, center-left, center-right, bottom-right, bottom-center, bottom-left). |
| chat\_trigger\_style | JSON | No | Styles the chat trigger button. |
| chat\_window\_style | JSON | No | Customizes the overall appearance of the chat window. |
| error\_message\_style | JSON | No | Sets the format for error messages within the chat window. |
| flow\_id | String | Yes | Identifies the flow that the component is associated with. |
| height | Number | No | Sets the height of the chat window in pixels. |
| host\_url | String | Yes | Specifies the URL of the host for chat component communication. |
| input\_container\_style | JSON | No | Applies styling to the container where chat messages are entered. |
| input\_style | JSON | No | Sets the style for the chat input field. |
| online | Boolean | No | Toggles the online status of the chat component. |
| online\_message | String | No | Sets a custom message to display when the chat component is online. |
| placeholder | String | No | Sets the placeholder text for the chat input field. |
| placeholder\_sending | String | No | Sets the placeholder text to display while a message is being sent. |
| send\_button\_style | JSON | No | Sets the style for the send button in the chat window. |
| send\_icon\_style | JSON | No | Sets the style for the send icon in the chat window. |
| tweaks | JSON | No | Applies additional custom adjustments for the associated flow. |
| user\_message\_style | JSON | No | Determines the formatting for user messages in the chat window. |
| width | Number | No | Sets the width of the chat window in pixels. |
| window\_title | String | No | Sets the title displayed in the chat window's header or title bar. |

[PreviousWorkspace concepts](/workspace-overview)[NextLogs](/workspace-logs)

* [cURL](#4eb287a8424349c4b0b436a6703de5f3)
* [Python API](#fb7db14e6330418389562ef647aa2354)
* [Python Code](#7af87438549b4972907ac310a4193067)
* [Tweaks](#5680600063724590ac2302b4ddeea867)
* [Send image files to your flow with the API](#send-image-files-to-your-flow-with-the-api)
* [Chat Widget](#48f121a6cb3243979a341753da0c2700)
  + [Embed your flow into HTML](#6e84db2f2a0d451db6fa03c57e9bf9a4)
  + [Embed your flow with React](#fe5d3b1c42e74e4c84ebc9d1799b7665)
  + [Embed your flow with Angular](#4fd87355b9aa409894acfbb9e1497980)
* [Chat Widget Configuration](#5ede4bbbd2ac43e29c90f3edb43cba58)

Hi, how can I help you?

![](/img/langflow-icon-black-transparent.svg)![](https://www.facebook.com/tr?id=853345499983657&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1482048748489568&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1172982080582122&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=896532212496788&ev=PageView&noscript=1)