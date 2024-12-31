Concepts | 🦜️🛠️ LangSmith[Skip to main content](#__docusaurus_skipToContent_fallback)Learn the essentials of LangSmith in the new Introduction to LangSmith course!  [Enroll for free.](https://academy.langchain.com/courses/intro-to-langsmith) [![](/img/langsmith-logo-black.svg)![](/img/langsmith-logo-white.svg)](/)[API Reference](#)

* [REST](https://api.smith.langchain.com/redoc)
* [Python](https://docs.smith.langchain.com/reference/python)
SearchRegion

* US
* EU
[Go to App](https://smith.langchain.com/)

* [Quick Start](/)
* [Observability](/observability/tutorials)
* [Evaluation](/evaluation)
* [Prompt Engineering](/prompt_engineering/tutorials)
  + [Tutorials](/prompt_engineering/tutorials)
    - [Optimize a classifier](/prompt_engineering/tutorials/optimize_classifier)
  + [How-to Guides](/prompt_engineering/how_to_guides)
    - [Playground](/prompt_engineering/how_to_guides/playground/custom_endpoint)
    - [Prompts](/prompt_engineering/how_to_guides/prompts/create_a_prompt)
  + [Conceptual Guide](/prompt_engineering/concepts)
* [Deployment (LangGraph Platform)](/langgraph_cloud)
* ---
* [Administration](/administration/tutorials)
* [Self-hosting](/self_hosting)
* [Pricing](/administration/pricing)
* ---
* [Reference](/reference)
  + [Cloud architecture and scalability](/reference/cloud_architecture_and_scalability)
  + [Authz and Authn](/reference/authentication_authorization/authentication_methods)
    - [Authentication methods](/reference/authentication_authorization/authentication_methods)
  + [data\_formats](/reference/data_formats/example_data_format)
  + [Evaluation](/reference/evaluation/dataset_transformations)
    - [Dataset transformations](/reference/evaluation/dataset_transformations)
  + [Regions FAQ](/reference/regions_faq)
  + [sdk\_reference](/reference/sdk_reference/langchain_evaluators)


* [Prompt Engineering](/prompt_engineering/tutorials)
* Conceptual Guide
On this page

Concepts
========

Prompt engineering is one the core pillars of LangSmith. While traditional software application are built by writing code, AI applications often involve a good amount of writing prompts. We aim to make this as easy possible by providing a set of tools designed to enable and facilitate prompt engineering.

Why prompt engineering?[​](#why-prompt-engineering)
---------------------------------------------------

A prompt sets the stage for the model, like an audience member at an improv show directing the actor's next performance - it guides the model's behavior without changing its underlying capabilities. Just as telling an actor to "be a pirate" determines how they act, a prompt provides instructions, examples, and context that shape how the model responds.

Prompt engineering is important because it allows you to change the way the model behaves. While there are other ways to change the model's behavior (like fine-tuning), prompt engineering is usually the simplest to get started with and often provides the highest ROI.

We often see that prompt engineering is multi-disciplinary. Sometimes the best prompt engineer is not the software engineer who is building the application, but rather the product manager or another domain expert. It is important to have the proper tooling and infrastructure to support this cross-disciplinary building.

Prompts vs Prompt Templates[​](#prompts-vs-prompt-templates)
------------------------------------------------------------

Although we often use these terms interchangably, it is important to understand the difference between "prompts" and "prompt templates".

Prompts refer to the messages that are passed into the language model.

Prompt Templates refer to a way of formatting information to get that prompt to hold the information that you want. Prompt templates can include variables for few shot examples, outside context, or any other external data that is needed in your prompt.

![](/assets/images/prompt_vs_prompt_template-3e48c649bfe69dcd49d5fd7381aab163.png)

Prompts in LangSmith[​](#prompts-in-langsmith)
----------------------------------------------

You can store and version prompts templates in LangSmith. There are few key aspects of a prompt template to understand.

### Chat vs Completion[​](#chat-vs-completion)

There are two different types of prompts: `chat` style prompts and `completion` style prompts.

Chat style prompts are a **list of messages**. This is the prompting style supported by most model APIs these days, and so this should generally be preferred.

Completion style prompts are just a string. This is an older style of prompting, and so mostly exists for legacy reasons.

### F-string vs mustache[​](#f-string-vs-mustache)

You can format your prompt with input variables using either [f-string](https://realpython.com/python-f-strings/) or [mustache](https://mustache.github.io/mustache.5.html) format. Here is an example prompt with f-string format:

```
Hello,{name}!  

```

And here is one with mustache:

```
Hello,{{name}}!  

```
Mustache format

Mustache format gives your more flexbility around conditional variables, loops, and nested keys. Read [the documentation](https://mustache.github.io/mustache.5.html)

### Tools[​](#tools)

Tools are interfaces the LLM can use to interact with the outside world. Tools consist of a name, description, and JSON schema of arguments used to call the tool.

### Structured Output[​](#structured-output)

Structured output is a feature of most state of the art LLMs, wherein instead of producing raw text as output they stick to a specified schema. This may or may not use [Tools](#tools) under the hood.

Structured Output vs Tools

Structured outputs are similar to tools, but different in a few key ways. With tools, the LLM choose which tool to call (or may choose not to call any); with structured output, the LLM **always** responds in this format. With tools, the LLM may select **multiple** tools; with structured output, only one response is generate.

### Model[​](#model)

Optionally, you can store a model configuration alongside a prompt template. This includes the name of the model and any other parameters (temperature, etc).

Prompt Versioning[​](#prompt-versioning)
----------------------------------------

Verisioning is a key part of iterating and collaborating on your different prompts.

### Commits[​](#commits)

Every saved update to a prompt creates a new commit. You can view previous commits, making it easy to review earlier prompt versions or revert to a previous state if needed. In the SDK, you can access a specific commit of a prompt by specifying the commit hash along with the prompt name (e.g. `prompt_name:commit_hash`).

In the UI, you can compare a commit with its previous version by toggling the "diff" button in the top-right corner of the Commits tab. ![](/assets/images/commit_diff-e6773531883507d745eb22d08bab0056.png)

### Tags[​](#tags)

You may want to tag prompt commits with a human-readable tag so that you can refer to it even as new commits are added. Common use cases include tagging a prompt with `dev` or `prod` tags. This allows you to track which versions of prompts are used where.

Prompt Playground[​](#prompt-playground)
----------------------------------------

The prompt playground makes the process of iterating and testing your prompts seamless. You can enter the playground from the sidebar or directly from a saved prompt.

In the playground you can:

* Change the model being used
* Change prompt template being used
* Change the output schema
* Change the tools available
* Enter the input variables to run through the prompt template
* Run the prompt through the model
* Observe the outputs

Testing multiple prompts[​](#testing-multiple-prompts)
------------------------------------------------------

You can add more prompts to your playground to easily compare outputs and decide which version is better:

![](/assets/images/add_prompt_to_playground-72edfaaf4ebadc6404b5dd1c5c3e5680.gif)

Testing over a dataset[​](#testing-over-a-dataset)
--------------------------------------------------

To test over a dataset, you simply select the dataset from the top right and press Start. You can modify whether the results are streamed back as well as how many repitions there are in the test.

![](/assets/images/test_over_dataset_in_playground-d9300964035796aede159c8bf87d3910.gif)

You can click on the "View Experiment" button to dive deeper into the results of the test.

Prompt Canvas[​](#prompt-canvas)
--------------------------------

The prompt canvas makes it easy to edit a prompt with the help of an LLM. This allows you to iterate faster on long prompts and also makes it easier to make overarching stylisting or tonal changes to your prompt. You can enter the promp canvas by clicking the glowing wand over any message in your prompt:

![](/assets/images/prompt_canvas_open-1f4ee00de4116761fdc60bb20860837e.gif)

### Chat sidebar[​](#chat-sidebar)

You can use the chat sidebar to ask questions about your prompt, or to give instructions in natural language to the LLM for how to rewrite your prompt.

![](/assets/images/prompt_canvas_rewrite-63f6f747175551dadebbdf717dea9c09.gif)

### Write directly[​](#write-directly)

You can also edit the prompt directly - you don't **need** to use the LLM. This is useful if you know what edits you want to make and just want to make them directly

### Quick actions[​](#quick-actions)

There are quick actions to change the reading level or length of the prompt with a single mouse click:

![](/assets/images/prompt_canvas_quick_actions-8c873fd6715397171030767d54b27927.gif)

### Custom quick actions[​](#custom-quick-actions)

You can also save your own custom quick actions, for ease of use across all the prompts you are working on in LangSmith:

![](/assets/images/prompt_canvas_custom_quick_action-3fbc8dd98c06f336c5323092801cbc67.gif)

### Diffing[​](#diffing)

You can also see the specific differences between each version of your prompt by selecting the diff slider in the top right of the canvas:

![](/assets/images/prompt_canvas_diff-c1ea4921287c4b36b0ef803989f09fba.gif)

### Saving and using[​](#saving-and-using)

Lastly, you can save the prompt you have created in the canvas by clicking the "Use this Version" button in the bottom right:

![](/assets/images/prompt_canvas_save-f9de1dd20a376b45787c7014b9c2e1b3.gif)

---

#### Was this page helpful?

  
#### You can leave detailed feedback [on GitHub](https://github.com/langchain-ai/langsmith-docs/issues/new?title=DOC%3A+%3CPlease+write+a+comprehensive+title+after+the+%27DOC%3A+%27+prefix%3E).

[PreviousLangChain Hub](/prompt_engineering/how_to_guides/prompts/langchain_hub)[NextDeployment (LangGraph Platform)](/langgraph_cloud)

* [Why prompt engineering?](#why-prompt-engineering)
* [Prompts vs Prompt Templates](#prompts-vs-prompt-templates)
* [Prompts in LangSmith](#prompts-in-langsmith)
  + [Chat vs Completion](#chat-vs-completion)
  + [F-string vs mustache](#f-string-vs-mustache)
  + [Tools](#tools)
  + [Structured Output](#structured-output)
  + [Model](#model)
* [Prompt Versioning](#prompt-versioning)
  + [Commits](#commits)
  + [Tags](#tags)
* [Prompt Playground](#prompt-playground)
* [Testing multiple prompts](#testing-multiple-prompts)
* [Testing over a dataset](#testing-over-a-dataset)
* [Prompt Canvas](#prompt-canvas)
  + [Chat sidebar](#chat-sidebar)
  + [Write directly](#write-directly)
  + [Quick actions](#quick-actions)
  + [Custom quick actions](#custom-quick-actions)
  + [Diffing](#diffing)
  + [Saving and using](#saving-and-using)
Community

* [Discord](https://discord.gg/cU2adEyC7w)
* [Twitter](https://twitter.com/LangChainAI)
GitHub

* [Docs Code](https://github.com/langchain-ai/langsmith-docs)
* [LangSmith SDK](https://github.com/langchain-ai/langsmith-sdk)
* [Python](https://github.com/langchain-ai/langchain)
* [JS/TS](https://github.com/langchain-ai/langchainjs)
More

* [Homepage](https://langchain.com)
* [Blog](https://blog.langchain.dev)
* [LangChain Python Docs](https://python.langchain.com/en/latest/)
* [LangChain JS/TS Docs](https://js.langchain.com/docs/)
Copyright © 2024 LangChain, Inc.