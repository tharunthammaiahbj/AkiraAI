Scrapy at a glance — Scrapy 2.12.0 documentation [Scrapy](../index.html)  2.12 

First steps

* [Scrapy at a glance](#)
  + [Walk-through of an example spider](#walk-through-of-an-example-spider)
    - [What just happened?](#what-just-happened)
  + [What else?](#what-else)
  + [What’s next?](#what-s-next)
* [Installation guide](install.html)
* [Scrapy Tutorial](tutorial.html)
* [Examples](examples.html)

Basic concepts

* [Command line tool](../topics/commands.html)
* [Spiders](../topics/spiders.html)
* [Selectors](../topics/selectors.html)
* [Items](../topics/items.html)
* [Item Loaders](../topics/loaders.html)
* [Scrapy shell](../topics/shell.html)
* [Item Pipeline](../topics/item-pipeline.html)
* [Feed exports](../topics/feed-exports.html)
* [Requests and Responses](../topics/request-response.html)
* [Link Extractors](../topics/link-extractors.html)
* [Settings](../topics/settings.html)
* [Exceptions](../topics/exceptions.html)

Built-in services

* [Logging](../topics/logging.html)
* [Stats Collection](../topics/stats.html)
* [Sending e-mail](../topics/email.html)
* [Telnet Console](../topics/telnetconsole.html)

Solving specific problems

* [Frequently Asked Questions](../faq.html)
* [Debugging Spiders](../topics/debug.html)
* [Spiders Contracts](../topics/contracts.html)
* [Common Practices](../topics/practices.html)
* [Broad Crawls](../topics/broad-crawls.html)
* [Using your browser’s Developer Tools for scraping](../topics/developer-tools.html)
* [Selecting dynamically-loaded content](../topics/dynamic-content.html)
* [Debugging memory leaks](../topics/leaks.html)
* [Downloading and processing files and images](../topics/media-pipeline.html)
* [Deploying Spiders](../topics/deploy.html)
* [AutoThrottle extension](../topics/autothrottle.html)
* [Benchmarking](../topics/benchmarking.html)
* [Jobs: pausing and resuming crawls](../topics/jobs.html)
* [Coroutines](../topics/coroutines.html)
* [asyncio](../topics/asyncio.html)

Extending Scrapy

* [Architecture overview](../topics/architecture.html)
* [Add-ons](../topics/addons.html)
* [Downloader Middleware](../topics/downloader-middleware.html)
* [Spider Middleware](../topics/spider-middleware.html)
* [Extensions](../topics/extensions.html)
* [Signals](../topics/signals.html)
* [Scheduler](../topics/scheduler.html)
* [Item Exporters](../topics/exporters.html)
* [Components](../topics/components.html)
* [Core API](../topics/api.html)

All the rest

* [Release notes](../news.html)
* [Contributing to Scrapy](../contributing.html)
* [Versioning and API stability](../versioning.html)
[Scrapy](../index.html)


* Scrapy at a glance
* [View page source](../_sources/intro/overview.rst.txt)

---

Scrapy at a glance[¶](#scrapy-at-a-glance)
==========================================

Scrapy (/ˈskreɪpaɪ/) is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

Even though Scrapy was originally designed for [web scraping](https://en.wikipedia.org/wiki/Web_scraping), it can also be used to extract data using APIs (such as [Amazon Associates Web Services](https://affiliate-program.amazon.com/welcome/ecs)) or as a general purpose web crawler.

Walk-through of an example spider[¶](#walk-through-of-an-example-spider)
------------------------------------------------------------------------

In order to show you what Scrapy brings to the table, we’ll walk you through an example of a Scrapy Spider using the simplest way to run a spider.

Here’s the code for a spider that scrapes famous quotes from website <https://quotes.toscrape.com>, following the pagination:

```
importscrapyclassQuotesSpider(scrapy.Spider):name="quotes"start_urls=["https://quotes.toscrape.com/tag/humor/",]defparse(self,response):forquoteinresponse.css("div.quote"):yield{"author":quote.xpath("span/small/text()").get(),"text":quote.css("span.text::text").get(),}next_page=response.css('li.next a::attr("href")').get()ifnext_pageisnotNone:yieldresponse.follow(next_page,self.parse)
```

Put this in a text file, name it something like `quotes_spider.py` and run the spider using the [`runspider`](../topics/commands.html#std-command-runspider) command:

```
scrapyrunspiderquotes_spider.py-oquotes.jsonl
```

When this finishes you will have in the `quotes.jsonl` file a list of the quotes in JSON Lines format, containing the text and author, which will look like this:

```
{"author":"Jane Austen","text":"\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"}{"author":"Steve Martin","text":"\u201cA day without sunshine is like, you know, night.\u201d"}{"author":"Garrison Keillor","text":"\u201cAnyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.\u201d"}...
```
### What just happened?[¶](#what-just-happened)

When you ran the command `scrapyrunspiderquotes_spider.py`, Scrapy looked for a Spider definition inside it and ran it through its crawler engine.

The crawl started by making requests to the URLs defined in the `start_urls` attribute (in this case, only the URL for quotes in the *humor* category) and called the default callback method `parse`, passing the response object as an argument. In the `parse` callback, we loop through the quote elements using a CSS Selector, yield a Python dict with the extracted quote text and author, look for a link to the next page and schedule another request using the same `parse` method as callback.

Here you will notice one of the main advantages of Scrapy: requests are [scheduled and processed asynchronously](../topics/architecture.html#topics-architecture). This means that Scrapy doesn’t need to wait for a request to be finished and processed, it can send another request or do other things in the meantime. This also means that other requests can keep going even if a request fails or an error happens while handling it.

While this enables you to do very fast crawls (sending multiple concurrent requests at the same time, in a fault-tolerant way) Scrapy also gives you control over the politeness of the crawl through [a few settings](../topics/settings.html#topics-settings-ref). You can do things like setting a download delay between each request, limiting the amount of concurrent requests per domain or per IP, and even [using an auto-throttling extension](../topics/autothrottle.html#topics-autothrottle) that tries to figure these settings out automatically.

Note

This is using [feed exports](../topics/feed-exports.html#topics-feed-exports) to generate the JSON file, you can easily change the export format (XML or CSV, for example) or the storage backend (FTP or [Amazon S3](https://aws.amazon.com/s3/), for example). You can also write an [item pipeline](../topics/item-pipeline.html#topics-item-pipeline) to store the items in a database.

What else?[¶](#what-else)
-------------------------

You’ve seen how to extract and store items from a website using Scrapy, but this is just the surface. Scrapy provides a lot of powerful features for making scraping easy and efficient, such as:

* Built-in support for [selecting and extracting](../topics/selectors.html#topics-selectors) data from HTML/XML sources using extended CSS selectors and XPath expressions, with helper methods for extraction using regular expressions.
* An [interactive shell console](../topics/shell.html#topics-shell) (IPython aware) for trying out the CSS and XPath expressions to scrape data, which is very useful when writing or debugging your spiders.
* Built-in support for [generating feed exports](../topics/feed-exports.html#topics-feed-exports) in multiple formats (JSON, CSV, XML) and storing them in multiple backends (FTP, S3, local filesystem)
* Robust encoding support and auto-detection, for dealing with foreign, non-standard and broken encoding declarations.
* [Strong extensibility support](../index.html#extending-scrapy), allowing you to plug in your own functionality using [signals](../topics/signals.html#topics-signals) and a well-defined API (middlewares, [extensions](../topics/extensions.html#topics-extensions), and [pipelines](../topics/item-pipeline.html#topics-item-pipeline)).
* A wide range of built-in extensions and middlewares for handling:
  
  + cookies and session handling
  + HTTP features like compression, authentication, caching
  + user-agent spoofing
  + robots.txt
  + crawl depth restriction
  + and more
* A [Telnet console](../topics/telnetconsole.html#topics-telnetconsole) for hooking into a Python console running inside your Scrapy process, to introspect and debug your crawler
* Plus other goodies like reusable spiders to crawl sites from [Sitemaps](https://www.sitemaps.org/index.html) and XML/CSV feeds, a media pipeline for [automatically downloading images](../topics/media-pipeline.html#topics-media-pipeline) (or any other media) associated with the scraped items, a caching DNS resolver, and much more!

What’s next?[¶](#what-s-next)
-----------------------------

The next steps for you are to [install Scrapy](install.html#intro-install), [follow through the tutorial](tutorial.html#intro-tutorial) to learn how to create a full-blown Scrapy project and [join the community](https://scrapy.org/community/). Thanks for your interest!

 [Previous](../index.html)[Next](install.html) 

---

© Copyright Scrapy developers. Last updated on Nov 19, 2024. 

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

---

Close