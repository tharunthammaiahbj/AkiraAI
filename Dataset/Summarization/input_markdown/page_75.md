Install Langflow | Langflow Documentation[Skip to main content](#__docusaurus_skipToContent_fallback)[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)Search...CTRLK[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)

* [Welcome to Langflow](/)
* [Get Started](/get-started-installation)
  + [Install Langflow](/get-started-installation)
  + [Quickstart](/get-started-quickstart)
* [Starter Projects](/starter-projects-basic-prompting)
* [Tutorials](/tutorials-blog-writer)
* [Workspace](/workspace-overview)
* [Components](/components-overview)
* [Agents](/agents-overview)
* [Configuration](/configuration-api-keys)
* [Guides](/guides-chat-memory)
* [Deployment](/deployment-docker)
* [Integrations](/integrations-assemblyai)
* [Contributing](/contributing-community)
* [API Reference](/api)


* Get Started
* Install Langflow
On this page

Install Langflow
================

You can deploy Langflow either locally or as a hosted service with [**Datastax Langflow**](#datastax-langflow).

Install Langflow locally[​](#install-langflow-locally)
------------------------------------------------------

Install Langflow locally with [uv (recommended)](https://docs.astral.sh/uv/getting-started/installation/), [pip](https://pypi.org/project/pip/), or [pipx](https://pipx.pypa.io/stable/installation/).

### Prerequisites[​](#prerequisites)

* [Python 3.10 to 3.12](https://www.python.org/downloads/release/python-3100/) installed
* [uv](https://docs.astral.sh/uv/getting-started/installation/), [pip](https://pypi.org/project/pip/), or [pipx](https://pipx.pypa.io/stable/installation/) installed
* Before installing Langflow, we recommend creating a virtual environment to isolate your Python dependencies with [uv](https://docs.astral.sh/uv/pip/environments), [venv](https://docs.python.org/3/library/venv.html), or [conda](https://anaconda.org/anaconda/conda)

### Install Langflow with pip or pipx[​](#install-langflow-with-pip-or-pipx)

Install Langflow with uv:

 `_10uv pip install langflow`

Install Langflow with pip:

 `_10python -m pip install langflow`

Install Langflow with pipx using the Python 3.10 executable:

 `_10pipx install langflow --python python3.10`

Run Langflow[​](#run-langflow)
------------------------------

1. To run Langflow with uv, enter the following command.

 `_10uv run langflow run`

1. To run Langflow with pip, enter the following command.

 `_10python -m langflow run`

1. Confirm that a local Langflow instance starts by visiting `http://127.0.0.1:7860` in a Chromium-based browser.

Now that Langflow is running, follow the [Quickstart](/get-started-quickstart) to create your first flow.

Manage Langflow versions[​](#manage-langflow-versions)
------------------------------------------------------

To upgrade Langflow to the latest version with uv, use the uv pip upgrade command.

 `_10uv pip install langflow -U`

To upgrade Langflow to the latest version, use the pip upgrade command.

 `_10python -m pip install langflow -U`

To install a specific version of the Langflow package, add the required version to the command.

 `_10python -m pip install langflow==1.1`

To reinstall Langflow and all of its dependencies, add the `--force-reinstall` flag to the command.

 `_10python -m pip install langflow --force-reinstall`

DataStax Langflow[​](#datastax-langflow)
----------------------------------------

**DataStax Langflow** is a hosted version of Langflow integrated with [Astra DB](https://www.datastax.com/products/datastax-astra). Be up and running in minutes with no installation or setup required. [Sign up for free](https://astra.datastax.com/signup?type=langflow).

Common installation issues[​](#common-installation-issues)
----------------------------------------------------------

This is a list of possible issues that you may encounter when installing and running Langflow.

### No `langflow.__main__` module[​](#no-langflow__main__-module)

When you try to run Langflow with the command `langflow run`, you encounter the following error:

 `_10> No module named 'langflow.__main__'`

1. Run `python -m langflow run` instead of `langflow run`.
2. If that doesn't work, reinstall the latest Langflow version with `python -m pip install langflow -U`.
3. If that doesn't work, reinstall Langflow and its dependencies with `python -m pip install langflow --pre -U --force-reinstall`.

### Langflow runTraceback[​](#langflow-runtraceback)

When you try to run Langflow using the command `langflow run`, you encounter the following error:

 `_10> langflow runTraceback (most recent call last): File ".../langflow", line 5, in <module> from langflow.__main__ import mainModuleNotFoundError: No module named 'langflow.__main__'`

There are two possible reasons for this error:

1. You've installed Langflow using `pip install langflow` but you already had a previous version of Langflow installed in your system. In this case, you might be running the wrong executable. To solve this issue, run the correct executable by running `python -m langflow run` instead of `langflow run`. If that doesn't work, try uninstalling and reinstalling Langflow with `python -m pip install langflow --pre -U`.
2. Some version conflicts might have occurred during the installation process. Run `python -m pip install langflow --pre -U --force-reinstall` to reinstall Langflow and its dependencies.

### Something went wrong running migrations[​](#something-went-wrong-running-migrations)

 `_10> Something went wrong running migrations. Please, run 'langflow migration --fix'`

Clear the cache by deleting the contents of the cache folder.

This folder can be found at:

* **Linux or WSL2 on Windows**: `home/<username>/.cache/langflow/`
* **MacOS**: `/Users/<username>/Library/Caches/langflow/`

This error can occur during Langflow upgrades when the new version can't override `langflow-pre.db` in `.cache/langflow/`. Clearing the cache removes this file but also erases your settings.

If you wish to retain your files, back them up before clearing the folder.

### Langflow installation freezes at pip dependency resolution[​](#langflow-installation-freezes-at-pip-dependency-resolution)

Installing Langflow with `pip install langflow` slowly fails with this error message:

 `_10pip is looking at multiple versions of <<library>> to determine which version is compatible with other requirements. This could take a while.`

To work around this issue, install Langflow with [`uv`](https://docs.astral.sh/uv/getting-started/installation/) instead of `pip`.

 `_10uv pip install langflow`

To run Langflow with uv:

 `_10uv run langflow run`[PreviousWelcome to Langflow](/)[NextQuickstart](/get-started-quickstart)

* [Install Langflow locally](#install-langflow-locally)
  + [Prerequisites](#prerequisites)
  + [Install Langflow with pip or pipx](#install-langflow-with-pip-or-pipx)
* [Run Langflow](#run-langflow)
* [Manage Langflow versions](#manage-langflow-versions)
* [DataStax Langflow](#datastax-langflow)
* [Common installation issues](#common-installation-issues)
  + [No `langflow.__main__` module](#no-langflow__main__-module)
  + [Langflow runTraceback](#langflow-runtraceback)
  + [Something went wrong running migrations](#something-went-wrong-running-migrations)
  + [Langflow installation freezes at pip dependency resolution](#langflow-installation-freezes-at-pip-dependency-resolution)

Hi, how can I help you?

![](/img/langflow-icon-black-transparent.svg)![](https://www.facebook.com/tr?id=853345499983657&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1482048748489568&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1172982080582122&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=896532212496788&ev=PageView&noscript=1)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%40posix%26Google%20Inc.%26Linux%20x86_64%26255%261280%26720%2612%2624%261280%26720%260%26na&eci=3&event=%7B%7D&event_id=1d158afd-3dd0-43d4-b1b1-265d944f085e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=856c11fc-6b79-4347-92aa-c89deea73fd7&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fget-started-installation&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%40posix%26Google%20Inc.%26Linux%20x86_64%26255%261280%26720%2612%2624%261280%26720%260%26na&eci=3&event=%7B%7D&event_id=1d158afd-3dd0-43d4-b1b1-265d944f085e&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=856c11fc-6b79-4347-92aa-c89deea73fd7&tw_document_href=https%3A%2F%2Fdocs.langflow.org%2Fget-started-installation&tw_iframe_status=0&txn_id=omt17&type=javascript&version=2.3.31)