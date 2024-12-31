Intro to Claude - Anthropic[Anthropic home page![](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](/)EnglishSearch...Ctrl K

* [Go to claude.ai](https://claude.ai/)
* [Research](https://www.anthropic.com/research)
* [News](https://www.anthropic.com/news)
* [Go to claude.ai](https://claude.ai/)
Search...NavigationGet startedIntro to Claude[Welcome](/en/home)[User Guides](/en/docs/welcome)[API Reference](/en/api/getting-started)[Prompt Library](/en/prompt-library/library)[Release Notes](/en/release-notes/overview)[Developer Newsletter](/en/developer-newsletter/overview)- [Developer Console](https://console.anthropic.com/)
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

Intro to Claude
===============

Claude is a family of [highly performant and intelligent AI models](/en/docs/about-claude/models) built by Anthropic. While Claude is powerful and extensible, it’s also the most trustworthy and reliable AI available. It follows critical protocols, makes fewer mistakes, and is resistant to jailbreaks—allowing [enterprise customers](https://www.anthropic.com/customers) to build the safest AI-powered applications at scale.

This guide introduces Claude’s enterprise capabilities, the end-to-end flow for developing with Claude, and how to start building.

[​](#what-you-can-do-with-claude)What you can do with Claude
------------------------------------------------------------

Claude is designed to empower enterprises at scale with [strong performance](https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf) across benchmark evaluations for reasoning, math, coding, and fluency in English and non-English languages.

Here’s a non-exhaustive list of Claude’s capabilities and common uses.

| Capability | Enables you to… |
| --- | --- |
| Text and code generation | * Adhere to brand voice for excellent customer-facing experiences such as copywriting and chatbots * Create production-level code and operate (in-line code generation, debugging, and conversational querying) within complex codebases * Build automatic translation features between languages * Conduct complex financial forecasts * Support legal use cases that require high-quality technical analysis, long context windows for processing detailed documents, and fast outputs |
| Vision | * Process and analyze visual input, such as extracting insights from charts and graphs * Generate code from images with code snippets or templates based on diagrams * Describe an image for a user with low vision |
| Tool use | * Interact with external client-side tools and functions, allowing Claude to reason, plan, and execute actions by generating structured outputs through API calls |

---

[​](#model-options)Model options
--------------------------------

Enterprise use cases often mean complex needs and edge cases. Anthropic offers a range of models across the Claude 3 and Claude 3.5 families to allow you to choose the right balance of intelligence, speed, and [cost](https://www.anthropic.com/api).

### [​](#claude-3-5-family)Claude 3.5 Family

|  | **Claude 3.5 Sonnet** | **Claude 3.5 Haiku** |
| --- | --- | --- |
| **Description** | Most intelligent model, combining top-tier performance with improved speed. | Fastest and most-cost effective model. |
| **Example uses** | * Advanced research and analysis * Complex problem-solving * Sophisticated language understanding and generation * High-level strategic planning | * Code generation * Real-time chatbots * Data extraction and labeling * Content classification |
| **Latest 1P APImodel name** | `claude-3-5-sonnet-20241022` | `claude-3-5-haiku-20241022` |
| **Latest AWS Bedrockmodel name** | `anthropic.claude-3-5-sonnet-20241022-v2:0` | `anthropic.claude-3-5-haiku-20241022-v1:0` |
| **Vertex AImodel name** | `claude-3-5-sonnet-v2@20241022` | `claude-3-5-haiku@20241022` |

### [​](#claude-3-family)Claude 3 Family

|  | **Opus** | **Sonnet** | **Haiku** |
| --- | --- | --- | --- |
| **Description** | Strong performance on highly complex tasks, such as math and coding. | Balances intelligence and speed for high-throughput tasks. | Near-instant responsiveness that can mimic human interactions. |
| **Example uses** | * Task automation across APIs and databases, and powerful coding tasks * R&D, brainstorming and hypothesis generation, and drug discovery * Strategy, advanced analysis of charts and graphs, financials and market trends, and forecasting | * Data processing over vast amounts of knowledge * Sales forecasting and targeted marketing * Code generation and quality control | * Live support chat * Translations * Content moderation * Extracting knowledge from unstructured data |
| **Latest 1P APImodel name** | `claude-3-opus-20240229` | `claude-3-sonnet-20240229` | `claude-3-haiku-20240307` |
| **Latest AWS Bedrockmodel name** | `anthropic.claude-3-opus-20240229-v1:0` | `anthropic.claude-3-sonnet-20240229-v1:0` | `anthropic.claude-3-haiku-20240307-v1:0` |
| **Vertex AImodel name** | `claude-3-opus@20240229` | `claude-3-sonnet@20240229` | `claude-3-haiku@20240307` |

[​](#enterprise-considerations)Enterprise considerations
--------------------------------------------------------

Along with an extensive set of features, tools, and capabilities, Claude is also built to be secure, trustworthy, and scalable for wide-reaching enterprise needs.

| Feature | Description |
| --- | --- |
| **Secure** | * [Enterprise-grade](https://trust.anthropic.com/) security and data handling for API * SOC II Type 2 certified, HIPAA compliance options for API * Accessible through AWS (GA) and GCP (in private preview) |
| **Trustworthy** | * Resistant to jailbreaks and misuse. We continuously monitor prompts and outputs for harmful, malicious use cases that violate our [AUP](https://www.anthropic.com/legal/aup). * Copyright indemnity protections for paid commercial services * Uniquely positioned to serve high trust industries that process large volumes of sensitive user data |
| **Capable** | * 200K token context window for expanded use cases, with future support for 1M * [Tool use](/en/docs/build-with-claude/tool-use), also known as function calling, which allows seamless integration of Claude into specialized applications and custom workflows * Multimodal input capabilities with text output, allowing you to upload images (such as tables, graphs, and photos) along with text prompts for richer context and complex use cases * [Developer Console](https://console.anthropic.com) with Workbench and prompt generation tool for easier, more powerful prompting and experimentation * [SDKs](/en/api/client-sdks) and [APIs](/en/api) to expedite and enhance development |
| **Reliable** | * Very low hallucination rates * Accurate over long documents |
| **Global** | * Great for coding tasks and fluency in English and non-English languages like Spanish and Japanese * Enables use cases like translation services and broader global utility |
| **Cost conscious** | * Family of models balances cost, performance, and intelligence |

[​](#implementing-claude)Implementing Claude
--------------------------------------------

1

Scope your use case

* Identify a problem to solve or tasks to automate with Claude.
* Define requirements: features, performance, and cost.
2

Design your integration

* Select Claude’s capabilities (e.g., vision, tool use) and models (Opus, Sonnet, Haiku) based on needs.
* Choose a deployment method, such as the Anthropic API, AWS Bedrock, or Vertex AI.
3

Prepare your data

* Identify and clean relevant data (databases, code repos, knowledge bases) for Claude’s context.
4

Develop your prompts

* Use Workbench to create evals, draft prompts, and iteratively refine based on test results.
* Deploy polished prompts and monitor real-world performance for further refinement.
5

Implement Claude

* Set up your environment, integrate Claude with your systems (APIs, databases, UIs), and define human-in-the-loop requirements.
6

Test your system

* Conduct red teaming for potential misuse and A/B test improvements.
7

Deploy to production

* Once your application runs smoothly end-to-end, deploy to production.
8

Monitor and improve

* Monitor performance and effectiveness to make ongoing improvements.

[​](#start-building-with-claude)Start building with Claude
----------------------------------------------------------

When you’re ready, start building with Claude:

* Follow the [Quickstart](/en/docs/quickstart) to make your first API call
* Check out the [API Reference](/en/api)
* Explore the [Prompt Library](/en/prompt-library/library) for example prompts
* Experiment and start building with the [Workbench](https://console.anthropic.com)
* Check out the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) for working code examples

Was this page helpful?

YesNo[Initial setup](/en/docs/initial-setup)[Overview](/en/docs/about-claude/use-case-guides/overview)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page

* [What you can do with Claude](#what-you-can-do-with-claude)
* [Model options](#model-options)
* [Claude 3.5 Family](#claude-3-5-family)
* [Claude 3 Family](#claude-3-family)
* [Enterprise considerations](#enterprise-considerations)
* [Implementing Claude](#implementing-claude)
* [Start building with Claude](#start-building-with-claude)
