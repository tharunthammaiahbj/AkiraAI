Generate a concise and clear summary of the raw tech documentation markdown. Focus on key elements like core concepts, instructions, and essential workflows while ignoring extraneous or repetitive details. Ensure the summary is coherent, relevant, and adaptable to various markdown formats.

Stats Collection — Scrapy 2.12.0 documentation [Scrapy](../index.html)  2.12 

First steps

* [Scrapy at a glance](../intro/overview.html)
* [Installation guide](../intro/install.html)
* [Scrapy Tutorial](../intro/tutorial.html)
* [Examples](../intro/examples.html)

Basic concepts

* [Command line tool](commands.html)
* [Spiders](spiders.html)
* [Selectors](selectors.html)
* [Items](items.html)
* [Item Loaders](loaders.html)
* [Scrapy shell](shell.html)
* [Item Pipeline](item-pipeline.html)
* [Feed exports](feed-exports.html)
* [Requests and Responses](request-response.html)
* [Link Extractors](link-extractors.html)
* [Settings](settings.html)
* [Exceptions](exceptions.html)

Built-in services

* [Logging](logging.html)
* [Stats Collection](#)
  + [Common Stats Collector uses](#common-stats-collector-uses)
  + [Available Stats Collectors](#available-stats-collectors)
    - [MemoryStatsCollector](#memorystatscollector)
      * [`MemoryStatsCollector`](#scrapy.statscollectors.MemoryStatsCollector)
    - [DummyStatsCollector](#dummystatscollector)
      * [`DummyStatsCollector`](#scrapy.statscollectors.DummyStatsCollector)
* [Sending e-mail](email.html)
* [Telnet Console](telnetconsole.html)

Solving specific problems

* [Frequently Asked Questions](../faq.html)
* [Debugging Spiders](debug.html)
* [Spiders Contracts](contracts.html)
* [Common Practices](practices.html)
* [Broad Crawls](broad-crawls.html)
* [Using your browser’s Developer Tools for scraping](developer-tools.html)
* [Selecting dynamically-loaded content](dynamic-content.html)
* [Debugging memory leaks](leaks.html)
* [Downloading and processing files and images](media-pipeline.html)
* [Deploying Spiders](deploy.html)
* [AutoThrottle extension](autothrottle.html)
* [Benchmarking](benchmarking.html)
* [Jobs: pausing and resuming crawls](jobs.html)
* [Coroutines](coroutines.html)
* [asyncio](asyncio.html)

Extending Scrapy

* [Architecture overview](architecture.html)
* [Add-ons](addons.html)
* [Downloader Middleware](downloader-middleware.html)
* [Spider Middleware](spider-middleware.html)
* [Extensions](extensions.html)
* [Signals](signals.html)
* [Scheduler](scheduler.html)
* [Item Exporters](exporters.html)
* [Components](components.html)
* [Core API](api.html)

All the rest

* [Release notes](../news.html)
* [Contributing to Scrapy](../contributing.html)
* [Versioning and API stability](../versioning.html)
[Scrapy](../index.html)


* Stats Collection
* [View page source](../_sources/topics/stats.rst.txt)

---

Stats Collection[¶](#stats-collection)
======================================

Scrapy provides a convenient facility for collecting stats in the form of key/values, where values are often counters. The facility is called the Stats Collector, and can be accessed through the [`stats`](api.html#scrapy.crawler.Crawler.stats) attribute of the [Crawler API](api.html#topics-api-crawler), as illustrated by the examples in the [Common Stats Collector uses](#topics-stats-usecases) section below.

However, the Stats Collector is always available, so you can always import it in your module and use its API (to increment or set new stat keys), regardless of whether the stats collection is enabled or not. If it’s disabled, the API will still work but it won’t collect anything. This is aimed at simplifying the stats collector usage: you should spend no more than one line of code for collecting stats in your spider, Scrapy extension, or whatever code you’re using the Stats Collector from.

Another feature of the Stats Collector is that it’s very efficient (when enabled) and extremely efficient (almost unnoticeable) when disabled.

The Stats Collector keeps a stats table per open spider which is automatically opened when the spider is opened, and closed when the spider is closed.

Common Stats Collector uses[¶](#common-stats-collector-uses)
------------------------------------------------------------

Access the stats collector through the [`stats`](api.html#scrapy.crawler.Crawler.stats) attribute. Here is an example of an extension that access stats:

```
classExtensionThatAccessStats:def__init__(self,stats):self.stats=stats@classmethoddeffrom_crawler(cls,crawler):returncls(crawler.stats)
```

Set stat value:

```
stats.set_value("hostname",socket.gethostname())
```

Increment stat value:

```
stats.inc_value("custom_count")
```

Set stat value only if greater than previous:

```
stats.max_value("max_items_scraped",value)
```

Set stat value only if lower than previous:

```
stats.min_value("min_free_memory_percent",value)
```

Get stat value:

```
>>> stats.get_value("custom_count")1
```

Get all stats:

```
>>> stats.get_stats(){'custom_count': 1, 'start_time': datetime.datetime(2009, 7, 14, 21, 47, 28, 977139)}
```

Available Stats Collectors[¶](#available-stats-collectors)
----------------------------------------------------------

Besides the basic `StatsCollector` there are other Stats Collectors available in Scrapy which extend the basic Stats Collector. You can select which Stats Collector to use through the [`STATS_CLASS`](settings.html#std-setting-STATS_CLASS) setting. The default Stats Collector used is the `MemoryStatsCollector`.

### MemoryStatsCollector[¶](#memorystatscollector)

*class*scrapy.statscollectors.MemoryStatsCollector[[source]](../_modules/scrapy/statscollectors.html#MemoryStatsCollector)[¶](#scrapy.statscollectors.MemoryStatsCollector)

A simple stats collector that keeps the stats of the last scraping run (for each spider) in memory, after they’re closed. The stats can be accessed through the [`spider_stats`](#scrapy.statscollectors.MemoryStatsCollector.spider_stats) attribute, which is a dict keyed by spider domain name.

This is the default Stats Collector used in Scrapy.

spider\_stats[¶](#scrapy.statscollectors.MemoryStatsCollector.spider_stats)

A dict of dicts (keyed by spider name) containing the stats of the last scraping run for each spider.

### DummyStatsCollector[¶](#dummystatscollector)

*class*scrapy.statscollectors.DummyStatsCollector[[source]](../_modules/scrapy/statscollectors.html#DummyStatsCollector)[¶](#scrapy.statscollectors.DummyStatsCollector)

A Stats collector which does nothing but is very efficient (because it does nothing). This stats collector can be set via the [`STATS_CLASS`](settings.html#std-setting-STATS_CLASS) setting, to disable stats collect in order to improve performance. However, the performance penalty of stats collection is usually marginal compared to other Scrapy workload like parsing pages.

 [Previous](logging.html)[Next](email.html) 

---

© Copyright Scrapy developers. Last updated on Nov 19, 2024. 

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

---

Close


