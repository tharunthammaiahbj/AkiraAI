Scrapy 2.12 documentation — Scrapy 2.12.0 documentation [Scrapy](#)  2.12 

First steps

* [Scrapy at a glance](intro/overview.html)
* [Installation guide](intro/install.html)
* [Scrapy Tutorial](intro/tutorial.html)
* [Examples](intro/examples.html)

Basic concepts

* [Command line tool](topics/commands.html)
* [Spiders](topics/spiders.html)
* [Selectors](topics/selectors.html)
* [Items](topics/items.html)
* [Item Loaders](topics/loaders.html)
* [Scrapy shell](topics/shell.html)
* [Item Pipeline](topics/item-pipeline.html)
* [Feed exports](topics/feed-exports.html)
* [Requests and Responses](topics/request-response.html)
* [Link Extractors](topics/link-extractors.html)
* [Settings](topics/settings.html)
* [Exceptions](topics/exceptions.html)

Built-in services

* [Logging](topics/logging.html)
* [Stats Collection](topics/stats.html)
* [Sending e-mail](topics/email.html)
* [Telnet Console](topics/telnetconsole.html)

Solving specific problems

* [Frequently Asked Questions](faq.html)
* [Debugging Spiders](topics/debug.html)
* [Spiders Contracts](topics/contracts.html)
* [Common Practices](topics/practices.html)
* [Broad Crawls](topics/broad-crawls.html)
* [Using your browser’s Developer Tools for scraping](topics/developer-tools.html)
* [Selecting dynamically-loaded content](topics/dynamic-content.html)
* [Debugging memory leaks](topics/leaks.html)
* [Downloading and processing files and images](topics/media-pipeline.html)
* [Deploying Spiders](topics/deploy.html)
* [AutoThrottle extension](topics/autothrottle.html)
* [Benchmarking](topics/benchmarking.html)
* [Jobs: pausing and resuming crawls](topics/jobs.html)
* [Coroutines](topics/coroutines.html)
* [asyncio](topics/asyncio.html)

Extending Scrapy

* [Architecture overview](topics/architecture.html)
* [Add-ons](topics/addons.html)
* [Downloader Middleware](topics/downloader-middleware.html)
* [Spider Middleware](topics/spider-middleware.html)
* [Extensions](topics/extensions.html)
* [Signals](topics/signals.html)
* [Scheduler](topics/scheduler.html)
* [Item Exporters](topics/exporters.html)
* [Components](topics/components.html)
* [Core API](topics/api.html)

All the rest

* [Release notes](news.html)
* [Contributing to Scrapy](contributing.html)
* [Versioning and API stability](versioning.html)
[Scrapy](#)


* Scrapy 2.12 documentation
* [View page source](_sources/index.rst.txt)

---

Scrapy 2.12 documentation[¶](#scrapy-version-documentation)
===========================================================

Scrapy is a fast high-level [web crawling](https://en.wikipedia.org/wiki/Web_crawler) and [web scraping](https://en.wikipedia.org/wiki/Web_scraping) framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

Getting help[¶](#getting-help)
------------------------------

Having trouble? We’d like to help!

* Try the [FAQ](faq.html) – it’s got answers to some common questions.
* Looking for specific information? Try the [Index](genindex.html) or [Module Index](py-modindex.html).
* Ask or search questions in [StackOverflow using the scrapy tag](https://stackoverflow.com/tags/scrapy).
* Ask or search questions in the [Scrapy subreddit](https://www.reddit.com/r/scrapy/).
* Search for questions on the archives of the [scrapy-users mailing list](https://groups.google.com/forum/#!forum/scrapy-users).
* Ask a question in the [#scrapy IRC channel](irc://irc.freenode.net/scrapy),
* Report bugs with Scrapy in our [issue tracker](https://github.com/scrapy/scrapy/issues).
* Join the Discord community [Scrapy Discord](https://discord.com/invite/mv3yErfpvq).

First steps[¶](#first-steps)
----------------------------

[Scrapy at a glance](intro/overview.html)

Understand what Scrapy is and how it can help you.

[Installation guide](intro/install.html)

Get Scrapy installed on your computer.

[Scrapy Tutorial](intro/tutorial.html)

Write your first Scrapy project.

[Examples](intro/examples.html)

Learn more by playing with a pre-made Scrapy project.

Basic concepts[¶](#basic-concepts)
----------------------------------

[Command line tool](topics/commands.html)

Learn about the command-line tool used to manage your Scrapy project.

[Spiders](topics/spiders.html)

Write the rules to crawl your websites.

[Selectors](topics/selectors.html)

Extract the data from web pages using XPath.

[Scrapy shell](topics/shell.html)

Test your extraction code in an interactive environment.

[Items](topics/items.html)

Define the data you want to scrape.

[Item Loaders](topics/loaders.html)

Populate your items with the extracted data.

[Item Pipeline](topics/item-pipeline.html)

Post-process and store your scraped data.

[Feed exports](topics/feed-exports.html)

Output your scraped data using different formats and storages.

[Requests and Responses](topics/request-response.html)

Understand the classes used to represent HTTP requests and responses.

[Link Extractors](topics/link-extractors.html)

Convenient classes to extract links to follow from pages.

[Settings](topics/settings.html)

Learn how to configure Scrapy and see all [available settings](topics/settings.html#topics-settings-ref).

[Exceptions](topics/exceptions.html)

See all available exceptions and their meaning.

Built-in services[¶](#built-in-services)
----------------------------------------

[Logging](topics/logging.html)

Learn how to use Python’s builtin logging on Scrapy.

[Stats Collection](topics/stats.html)

Collect statistics about your scraping crawler.

[Sending e-mail](topics/email.html)

Send email notifications when certain events occur.

[Telnet Console](topics/telnetconsole.html)

Inspect a running crawler using a built-in Python console.

Solving specific problems[¶](#solving-specific-problems)
--------------------------------------------------------

[Frequently Asked Questions](faq.html)

Get answers to most frequently asked questions.

[Debugging Spiders](topics/debug.html)

Learn how to debug common problems of your Scrapy spider.

[Spiders Contracts](topics/contracts.html)

Learn how to use contracts for testing your spiders.

[Common Practices](topics/practices.html)

Get familiar with some Scrapy common practices.

[Broad Crawls](topics/broad-crawls.html)

Tune Scrapy for crawling a lot domains in parallel.

[Using your browser’s Developer Tools for scraping](topics/developer-tools.html)

Learn how to scrape with your browser’s developer tools.

[Selecting dynamically-loaded content](topics/dynamic-content.html)

Read webpage data that is loaded dynamically.

[Debugging memory leaks](topics/leaks.html)

Learn how to find and get rid of memory leaks in your crawler.

[Downloading and processing files and images](topics/media-pipeline.html)

Download files and/or images associated with your scraped items.

[Deploying Spiders](topics/deploy.html)

Deploying your Scrapy spiders and run them in a remote server.

[AutoThrottle extension](topics/autothrottle.html)

Adjust crawl rate dynamically based on load.

[Benchmarking](topics/benchmarking.html)

Check how Scrapy performs on your hardware.

[Jobs: pausing and resuming crawls](topics/jobs.html)

Learn how to pause and resume crawls for large spiders.

[Coroutines](topics/coroutines.html)

Use the [coroutine syntax](https://docs.python.org/3/reference/compound_stmts.html#async).

[asyncio](topics/asyncio.html)

Use [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio) and [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio)-powered libraries.

Extending Scrapy[¶](#extending-scrapy)
--------------------------------------

[Architecture overview](topics/architecture.html)

Understand the Scrapy architecture.

[Add-ons](topics/addons.html)

Enable and configure third-party extensions.

[Downloader Middleware](topics/downloader-middleware.html)

Customize how pages get requested and downloaded.

[Spider Middleware](topics/spider-middleware.html)

Customize the input and output of your spiders.

[Extensions](topics/extensions.html)

Extend Scrapy with your custom functionality

[Signals](topics/signals.html)

See all available signals and how to work with them.

[Scheduler](topics/scheduler.html)

Understand the scheduler component.

[Item Exporters](topics/exporters.html)

Quickly export your scraped items to a file (XML, CSV, etc).

[Components](topics/components.html)

Learn the common API and some good practices when building custom Scrapy components.

[Core API](topics/api.html)

Use it on extensions and middlewares to extend Scrapy functionality.

All the rest[¶](#all-the-rest)
------------------------------

[Release notes](news.html)

See what has changed in recent Scrapy versions.

[Contributing to Scrapy](contributing.html)

Learn how to contribute to the Scrapy project.

[Versioning and API stability](versioning.html)

Understand Scrapy versioning and API stability.

[Next](intro/overview.html) 

---

© Copyright Scrapy developers. Last updated on Nov 19, 2024. 

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

---

Close