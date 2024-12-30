Contribute to Langflow | Langflow Documentation[Skip to main content](#__docusaurus_skipToContent_fallback)[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)Search...CTRLK[![](/img/langflow-logo-black.svg)![](/img/langflow-logo-white.svg)](/)

* [Welcome to Langflow](/)
* [Get Started](/get-started-installation)
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
  + [Join the Langflow community](/contributing-community)
  + [Contribute components](/contributing-components)
  + [Ask for help on the Discussions board](/contributing-github-discussions)
  + [Request an enhancement or report a bug](/contributing-github-issues)
  + [Contribute to Langflow](/contributing-how-to-contribute)
  + [Telemetry](/contributing-telemetry)
* [API Reference](/api)


* Contributing
* Contribute to Langflow
On this page

Contribute to Langflow
======================

This guide is intended to help you start contributing to Langflow. As an open-source project in a rapidly developing field, Langflow welcomes contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

To contribute code or documentation to this project, follow the [fork and pull request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow.

Contribute code[​](#contribute-code)
------------------------------------

Develop Langflow locally with [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Node.js](https://nodejs.org/en/download/package-manager).

### Prerequisites[​](#prerequisites)

* [uv(>=0.4)](https://docs.astral.sh/uv/getting-started/installation/)
* [Node.js](https://nodejs.org/en/download/package-manager)

### Clone the Langflow Repository[​](#clone-the-langflow-repository)

1. Navigate to the [Langflow GitHub repository](https://github.com/langflow-ai/langflow), and then click **Fork**.
2. Add the new remote to your local repository on your local machine:

 `_10git remote add fork https://github.com/<your_git_username>/langflow.git`
### Prepare the development environment[​](#prepare-the-development-environment)

1. Create development hooks.

 `_10make init`

This command sets up the development environment by installing backend and frontend dependencies, building the frontend static files, and initializing the project. It runs `make install_backend`, `make install_frontend`, `make build_frontend`, and finally `uv run langflow run` to start the application.

1. Run `make lint`, `make format`, and `make unit_tests` before pushing to the repository.

### Debug[​](#debug)

The repo includes a `.vscode/launch.json` file for debugging the backend in VSCode, which is faster than debugging with Docker Compose. To debug Langflow with the `launch.json` file in VSCode:

1. Open Langflow in VSCode.
2. Press **Ctrl+Shift+D** for Windows **or Cmd+Shift+D** for Mac to open the Run and Debug view.
3. From the **Run and Debug** dropdown, choose a debugging configuration.
4. Click the green **Play** button or press F5 to start debugging.

Use `launch.json` to quickly debug different parts of your application, like the backend, frontend, or CLI, directly from VSCode.

### Run Langflow locally[​](#run-langflow-locally)

After setting up the environment with `make init`, you can run Langflow's backend and frontend separately for development. Langflow recommends using a virtual environment like [venv](https://docs.python.org/3/library/venv.html) or [conda](https://anaconda.org/anaconda/conda) to isolate dependencies.

Before you begin, ensure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) and [Node.js](https://nodejs.org/en/download/package-manager) installed.

1. In the repository root, install the dependencies and start the development server for the backend:

 `_10make backend`

1. Install dependencies and start the frontend:

 `_10make frontend`

This approach allows you to work on the backend and frontend independently, with hot-reloading for faster development.

Contribute documentation[​](#contribute-documentation)
------------------------------------------------------

The documentation is built using [Docusaurus](https://docusaurus.io/) and written in [Markdown](https://docusaurus.io/docs/markdown-features).

### Prerequisites[​](#prerequisites-1)

* [Node.js](https://nodejs.org/en/download/package-manager)

### Clone the Langflow repository[​](#clone-the-langflow-repository-1)

1. Navigate to the [Langflow GitHub repository](https://github.com/langflow-ai/langflow), and then click **Fork**.
2. Add the new remote to your local repository on your local machine:

 `_10git remote add fork https://github.com/<your_git_username>/langflow.git`

1. To run the documentation locally, run the following commands:

 `_10cd docs_10npm install_10npm run start`

The documentation will be available at `localhost:3000` and all the files are located in the `docs/docs` folder.

Open a pull request[​](#open-a-pull-request)
--------------------------------------------

Once you have written and manually tested your changes with `make lint` and `make unit_tests`, open a pull request to send your changes upstream to the main Langflow repository.

1. Open a new GitHub pull request with your patch against the `main` branch.
2. Ensure the PR title follows semantic commit conventions. For example, features are `feat: add new feature` and fixes are `fix: correct issue with X`.
3. A Langflow maintainer will review your pull request. Thanks for your contribution!

Some additional guidance on pull request titles:

* Ensure the pull request description clearly describes the problem and solution. If the PR fixes an issue, include a link to the fixed issue in the PR description with `Fixes #1234`.
* Pull request titles appear in Langflow's release notes, so they should explain what the PR does as explicitly as possible.
* Pull requests should strive to fix one thing **only**, and should contain a good description of what is being fixed.

For more information, see the [Python Developer's Guide](https://devguide.python.org/getting-started/pull-request-lifecycle/index.html#making-good-commits).

[PreviousRequest an enhancement or report a bug](/contributing-github-issues)[NextTelemetry](/contributing-telemetry)

* [Contribute code](#contribute-code)
  + [Prerequisites](#prerequisites)
  + [Clone the Langflow Repository](#clone-the-langflow-repository)
  + [Prepare the development environment](#prepare-the-development-environment)
  + [Debug](#debug)
  + [Run Langflow locally](#run-langflow-locally)
* [Contribute documentation](#contribute-documentation)
  + [Prerequisites](#prerequisites-1)
  + [Clone the Langflow repository](#clone-the-langflow-repository-1)
* [Open a pull request](#open-a-pull-request)

Hi, how can I help you?

![](/img/langflow-icon-black-transparent.svg)![](https://www.facebook.com/tr?id=853345499983657&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1482048748489568&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1172982080582122&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=896532212496788&ev=PageView&noscript=1)