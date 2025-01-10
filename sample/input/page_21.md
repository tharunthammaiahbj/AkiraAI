Summarize the raw documentation markdown by condensing the key information, including important concepts, steps, and explanations. Ensure the summary is precise, clear, and relevant, adapting to various markdown formats while excluding redundant or unnecessary details.

Initial setup - Anthropic[Anthropic home page![](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)EnglishSearch...Ctrl K

* [Go to claude.ai](https://claude.ai/)
* [Research](https://www.anthropic.com/research)
* [News](https://www.anthropic.com/news)
* [Go to claude.ai](https://claude.ai/)
Search...NavigationGet startedInitial setup[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)[Developer Newsletter](/en/developer-newsletter/overview)- [Developer Console](https://console.anthropic.com/)
- [Developer Discord](https://www.anthropic.com/discord)
- [Support](https://support.anthropic.com/)
##### Get started

* [Overview](/en/docs/welcome)
* [Initial setup](/en/docs/initial-setup)
* [Intro to Claude](/en/docs/intro-to-claude)
##### Learn about Claude

* Use cases
* [Models](/en/docs/about-claude/models)
* [Security and compliance](https://trust.anthropic.com/)
##### Build with Claude

* [Define success criteria](/en/docs/build-with-claude/define-success)
* [Develop test cases](/en/docs/build-with-claude/develop-tests)
* Prompt engineering
* [Text generation](/en/docs/build-with-claude/text-generation)
* [Embeddings](/en/docs/build-with-claude/embeddings)
* [Google Sheets add-on](/en/docs/build-with-claude/claude-for-sheets)
* [Vision](/en/docs/build-with-claude/vision)
* [Tool use (function calling)](/en/docs/build-with-claude/tool-use)
* [Computer use (beta)](/en/docs/build-with-claude/computer-use)
* [Prompt caching](/en/docs/build-with-claude/prompt-caching)
* [Message Batches](/en/docs/build-with-claude/message-batches)
* [PDF support](/en/docs/build-with-claude/pdf-support)
* [Token counting](/en/docs/build-with-claude/token-counting)
##### Test and evaluate

* Strengthen guardrails
* [Using the Evaluation Tool](/en/docs/test-and-evaluate/eval-tool)
##### Administration

* [Admin API](/en/docs/administration/administration-api)
##### Resources

* [Glossary](/en/docs/resources/glossary)
* [Model Deprecations](/en/docs/resources/model-deprecations)
* [System status](https://status.anthropic.com/)
* [Claude 3 model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf)
* [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
* [Anthropic Courses](https://github.com/anthropics/courses)
##### Legal center

* [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
Get started

Initial setup
=============

Let’s learn how to use the Anthropic API to build with Claude.

In this example, we’ll have Claude write a Python function that checks if a string is a palindrome.

[​](#prerequisites)Prerequisites
--------------------------------

You will need:

* An Anthropic [Console account](console.anthropic.com)
* An [API key](https://console.anthropic.com/settings/keys)
* Python 3.7+ or TypeScript 4.5+

Anthropic provides [Python and TypeScript SDKs](https://docs.anthropic.com/en/api/client-sdks), although you can make direct HTTP requests to the API.

[​](#start-with-the-workbench)Start with the Workbench
------------------------------------------------------

Any API call you make–-regardless of the specific task-–sends a well-configured prompt to the Anthropic API. As you’re learning to make the most of Claude, we recommend that you start the development process in the Workbench, a web-based interface to Claude.

Log into the [Anthropic Console](https://console.anthropic.com) and click **Workbench**.

In the middle section, under User, let’s ask Claude a question.

User
```
Why is the ocean salty?
```

Click **Run**. On the right side, you’ll see output like

Response
```
The ocean is salty due to several factors:1. Weathering of rocks: Over millions of years, rain, rivers, and streams have eroded rocks containing mineral salts. These salts are carried into the ocean by water runoff.2. Volcanic activity: Underwater volcanoes and hydrothermal vents release minerals, including salts, into the ocean water.3. Atmospheric deposition: Salt particles from ocean spray can be carried by wind and deposited back into the ocean.4. Evaporation: As water evaporates from the surface of the ocean, it leaves behind dissolved salts, increasing the concentration of salt in the remaining water.5. Biological processes: Some marine organisms contribute to the ocean's salinity by releasing salt compounds as byproducts of their metabolism.Over time, these processes have continuously added salts to the ocean, while evaporation removes pure water, leading to the ocean's current salinity levels. It's important to note that the total amount of salt in the ocean remains relatively stable because the input of salts is balanced by the removal of salts through processes like the formation of evaporite deposits.
```

This is a good answer, but let’s say we wanted to control the exact type of answer Claude gives. For example, only allowing Claude to respond to questions with poems. We can control the format, tone, and personality of the response by adding a System Prompt.

System prompt
```
You are a world-class poet. Respond only with short poems.
```

Click **Run** again.

Response
```
The ocean's salty brine,A tale of time and elements combined.Rocks and rain, a slow erosion,Minerals carried in solution.Eons pass, the salt remains,In the vast, eternal watery domain.
```

See how Claude’s response has changed? LLMs respond well to clear and direct instructions. You can put the role instructions in either the system prompt or the user message. We recommend testing to see which way yields the best results for your use case.

Once you’ve tweaked the inputs such that you’re pleased with the output–-and have a good sense how to use Claude–-convert your Workbench into an integration.

Click **Get Code** to copy the generated code representing your Workbench session.

[​](#install-the-sdk)Install the SDK
------------------------------------

Anthropic provides SDKs for Python (3.7+) and TypeScript (4.5+).

* Python
* TypeScript

In your project directory, create a virtual environment.

Python
```
python -m venv claude-env
```

Activate the virtual environment using

* On macOS or Linux, `source claude-env/bin/activate`
* On Windows, `claude-env\Scripts\activate`

Python
```
pip install anthropic
```

[​](#set-your-api-key)Set your API key
--------------------------------------

Every API call requires a valid API key. The SDKs are designed to pull the API key from an environmental variable `ANTHROPIC_API_KEY`. You can also supply the key to the Anthropic client when initializing it.

* macOS and Linux
* Windows

```
exportANTHROPIC_API_KEY='your-api-key-here'
```

[​](#call-the-api)Call the API
------------------------------

Call the API by passing the proper parameters to the [/messages/create](https://docs.anthropic.com/en/api/messages) endpoint.

Note that the code provided by the Workbench sets the API key in the constructor. If you set the API key as an environment variable, you can omit that line as below.

* Python
* TypeScript

claude\_quickstart.py
```
import anthropicclient = anthropic.Anthropic()message = client.messages.create( model="claude-3-5-sonnet-20241022", max_tokens=1000, temperature=0, system="You are a world-class poet. Respond only with short poems.", messages=[{"role":"user","content":[{"type":"text","text":"Why is the ocean salty?"}]}])print(message.content)
```

Run the code using `python3 claude_quickstart.py` or `node claude_quickstart.js`.

Response
```
[TextBlock(text="The ocean's salty brine,\nA tale of time and design.\nRocks and rivers, their minerals shed,\nAccumulating in the ocean's bed.\nEvaporation leaves salt behind,\nIn the vast waters, forever enshrined.",type='text')]
```
The Workbench and code examples use default model settings for: model (name), temperature, and max tokens to sample. 

This quickstart shows how to develop a basic, but functional, Claude-powered application using the Console, Workbench, and API. You can use this same workflow as the foundation for much more powerful use cases.

[​](#next-steps)Next steps
--------------------------

Now that you have made your first Anthropic API request, it’s time to explore what else is possible:

[Use Case Guides
---------------

End to end implementation guides for common use cases.](/en/docs/about-claude/use-case-guides/overview)[Anthropic Cookbook
------------------

Learn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.](https://github.com/anthropics/anthropic-cookbook)[Prompt Library
--------------

Explore dozens of example prompts for inspiration across use cases.](/en/prompt-library/library)

Was this page helpful?

YesNo[Overview](/en/docs/welcome)[Intro to Claude](/en/docs/intro-to-claude)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page

* [Prerequisites](#prerequisites)
* [Start with the Workbench](#start-with-the-workbench)
* [Install the SDK](#install-the-sdk)
* [Set your API key](#set-your-api-key)
* [Call the API](#call-the-api)
* [Next steps](#next-steps)
