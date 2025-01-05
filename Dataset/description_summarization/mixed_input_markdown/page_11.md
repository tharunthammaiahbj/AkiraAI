Summarize the key concepts, instructions, and relevant details from the raw tech documentation markdown. Focus on delivering the most important information, such as key steps, explanations, and context, while omitting unnecessary or redundant content. Adapt to different markdown styles, ensuring the summary is clear, concise, and informative.

Extensions — Scrapy 2.12.0 documentation [Scrapy](../index.html)  2.12 

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
* [Stats Collection](stats.html)
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
* [Extensions](#)
  + [Extension settings](#extension-settings)
  + [Loading & activating extensions](#loading-activating-extensions)
  + [Available, enabled and disabled extensions](#available-enabled-and-disabled-extensions)
  + [Disabling an extension](#disabling-an-extension)
  + [Writing your own extension](#writing-your-own-extension)
    - [Sample extension](#sample-extension)
  + [Built-in extensions reference](#built-in-extensions-reference)
    - [General purpose extensions](#general-purpose-extensions)
      * [Log Stats extension](#module-scrapy.extensions.logstats)
      * [Core Stats extension](#module-scrapy.extensions.corestats)
      * [Telnet console extension](#module-scrapy.extensions.telnet)
      * [Memory usage extension](#module-scrapy.extensions.memusage)
      * [Memory debugger extension](#module-scrapy.extensions.memdebug)
      * [Spider state extension](#module-scrapy.extensions.spiderstate)
      * [Close spider extension](#module-scrapy.extensions.closespider)
      * [StatsMailer extension](#module-scrapy.extensions.statsmailer)
      * [Periodic log extension](#periodic-log-extension)
    - [Debugging extensions](#debugging-extensions)
      * [Stack trace dump extension](#stack-trace-dump-extension)
      * [Debugger extension](#debugger-extension)
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


* Extensions
* [View page source](../_sources/topics/extensions.rst.txt)

---

Extensions[¶](#extensions)
==========================

The extensions framework provides a mechanism for inserting your own custom functionality into Scrapy.

Extensions are just regular classes.

Extension settings[¶](#extension-settings)
------------------------------------------

Extensions use the [Scrapy settings](settings.html#topics-settings) to manage their settings, just like any other Scrapy code.

It is customary for extensions to prefix their settings with their own name, to avoid collision with existing (and future) extensions. For example, a hypothetical extension to handle [Google Sitemaps](https://en.wikipedia.org/wiki/Sitemaps) would use settings like `GOOGLESITEMAP_ENABLED`, `GOOGLESITEMAP_DEPTH`, and so on.

Loading & activating extensions[¶](#loading-activating-extensions)
------------------------------------------------------------------

Extensions are loaded and activated at startup by instantiating a single instance of the extension class per spider being run. All the extension initialization code must be performed in the class `__init__` method.

To make an extension available, add it to the [`EXTENSIONS`](settings.html#std-setting-EXTENSIONS) setting in your Scrapy settings. In [`EXTENSIONS`](settings.html#std-setting-EXTENSIONS), each extension is represented by a string: the full Python path to the extension’s class name. For example:

```
EXTENSIONS={"scrapy.extensions.corestats.CoreStats":500,"scrapy.extensions.telnet.TelnetConsole":500,}
```

As you can see, the [`EXTENSIONS`](settings.html#std-setting-EXTENSIONS) setting is a dict where the keys are the extension paths, and their values are the orders, which define the extension *loading* order. The [`EXTENSIONS`](settings.html#std-setting-EXTENSIONS) setting is merged with the [`EXTENSIONS_BASE`](settings.html#std-setting-EXTENSIONS_BASE) setting defined in Scrapy (and not meant to be overridden) and then sorted by order to get the final sorted list of enabled extensions.

As extensions typically do not depend on each other, their loading order is irrelevant in most cases. This is why the [`EXTENSIONS_BASE`](settings.html#std-setting-EXTENSIONS_BASE) setting defines all extensions with the same order (`0`). However, this feature can be exploited if you need to add an extension which depends on other extensions already loaded.

Available, enabled and disabled extensions[¶](#available-enabled-and-disabled-extensions)
-----------------------------------------------------------------------------------------

Not all available extensions will be enabled. Some of them usually depend on a particular setting. For example, the HTTP Cache extension is available by default but disabled unless the [`HTTPCACHE_ENABLED`](downloader-middleware.html#std-setting-HTTPCACHE_ENABLED) setting is set.

Disabling an extension[¶](#disabling-an-extension)
--------------------------------------------------

In order to disable an extension that comes enabled by default (i.e. those included in the [`EXTENSIONS_BASE`](settings.html#std-setting-EXTENSIONS_BASE) setting) you must set its order to `None`. For example:

```
EXTENSIONS={"scrapy.extensions.corestats.CoreStats":None,}
```

Writing your own extension[¶](#writing-your-own-extension)
----------------------------------------------------------

Each extension is a Python class. The main entry point for a Scrapy extension (this also includes middlewares and pipelines) is the `from_crawler` class method which receives a `Crawler` instance. Through the Crawler object you can access settings, signals, stats, and also control the crawling behaviour.

Typically, extensions connect to [signals](signals.html#topics-signals) and perform tasks triggered by them.

Finally, if the `from_crawler` method raises the [`NotConfigured`](exceptions.html#scrapy.exceptions.NotConfigured) exception, the extension will be disabled. Otherwise, the extension will be enabled.

### Sample extension[¶](#sample-extension)

Here we will implement a simple extension to illustrate the concepts described in the previous section. This extension will log a message every time:

* a spider is opened
* a spider is closed
* a specific number of items are scraped

The extension will be enabled through the `MYEXT_ENABLED` setting and the number of items will be specified through the `MYEXT_ITEMCOUNT` setting.

Here is the code of such extension:

```
importloggingfromscrapyimportsignalsfromscrapy.exceptionsimportNotConfiguredlogger=logging.getLogger(__name__)classSpiderOpenCloseLogging:def__init__(self,item_count):self.item_count=item_countself.items_scraped=0@classmethoddeffrom_crawler(cls,crawler):# first check if the extension should be enabled and raise# NotConfigured otherwiseifnotcrawler.settings.getbool("MYEXT_ENABLED"):raiseNotConfigured# get the number of items from settingsitem_count=crawler.settings.getint("MYEXT_ITEMCOUNT",1000)# instantiate the extension objectext=cls(item_count)# connect the extension object to signalscrawler.signals.connect(ext.spider_opened,signal=signals.spider_opened)crawler.signals.connect(ext.spider_closed,signal=signals.spider_closed)crawler.signals.connect(ext.item_scraped,signal=signals.item_scraped)# return the extension objectreturnextdefspider_opened(self,spider):logger.info("opened spider %s",spider.name)defspider_closed(self,spider):logger.info("closed spider %s",spider.name)defitem_scraped(self,item,spider):self.items_scraped+=1ifself.items_scraped%self.item_count==0:logger.info("scraped %d items",self.items_scraped)
```

Built-in extensions reference[¶](#built-in-extensions-reference)
----------------------------------------------------------------

### General purpose extensions[¶](#general-purpose-extensions)

#### Log Stats extension[¶](#module-scrapy.extensions.logstats)

*class*scrapy.extensions.logstats.LogStats[[source]](../_modules/scrapy/extensions/logstats.html#LogStats)[¶](#scrapy.extensions.logstats.LogStats)

Log basic stats like crawled pages and scraped items.

#### Core Stats extension[¶](#module-scrapy.extensions.corestats)

*class*scrapy.extensions.corestats.CoreStats[[source]](../_modules/scrapy/extensions/corestats.html#CoreStats)[¶](#scrapy.extensions.corestats.CoreStats)

Enable the collection of core statistics, provided the stats collection is enabled (see [Stats Collection](stats.html#topics-stats)).

#### Telnet console extension[¶](#module-scrapy.extensions.telnet)

*class*scrapy.extensions.telnet.TelnetConsole[[source]](../_modules/scrapy/extensions/telnet.html#TelnetConsole)[¶](#scrapy.extensions.telnet.TelnetConsole)

Provides a telnet console for getting into a Python interpreter inside the currently running Scrapy process, which can be very useful for debugging.

The telnet console must be enabled by the [`TELNETCONSOLE_ENABLED`](settings.html#std-setting-TELNETCONSOLE_ENABLED) setting, and the server will listen in the port specified in [`TELNETCONSOLE_PORT`](telnetconsole.html#std-setting-TELNETCONSOLE_PORT).

#### Memory usage extension[¶](#module-scrapy.extensions.memusage)

*class*scrapy.extensions.memusage.MemoryUsage[[source]](../_modules/scrapy/extensions/memusage.html#MemoryUsage)[¶](#scrapy.extensions.memusage.MemoryUsage)

Note

This extension does not work in Windows.

Monitors the memory used by the Scrapy process that runs the spider and:

1. sends a notification e-mail when it exceeds a certain value
2. closes the spider when it exceeds a certain value

The notification e-mails can be triggered when a certain warning value is reached ([`MEMUSAGE_WARNING_MB`](settings.html#std-setting-MEMUSAGE_WARNING_MB)) and when the maximum value is reached ([`MEMUSAGE_LIMIT_MB`](settings.html#std-setting-MEMUSAGE_LIMIT_MB)) which will also cause the spider to be closed and the Scrapy process to be terminated.

This extension is enabled by the [`MEMUSAGE_ENABLED`](settings.html#std-setting-MEMUSAGE_ENABLED) setting and can be configured with the following settings:

* [`MEMUSAGE_LIMIT_MB`](settings.html#std-setting-MEMUSAGE_LIMIT_MB)
* [`MEMUSAGE_WARNING_MB`](settings.html#std-setting-MEMUSAGE_WARNING_MB)
* [`MEMUSAGE_NOTIFY_MAIL`](settings.html#std-setting-MEMUSAGE_NOTIFY_MAIL)
* [`MEMUSAGE_CHECK_INTERVAL_SECONDS`](settings.html#std-setting-MEMUSAGE_CHECK_INTERVAL_SECONDS)
#### Memory debugger extension[¶](#module-scrapy.extensions.memdebug)

*class*scrapy.extensions.memdebug.MemoryDebugger[[source]](../_modules/scrapy/extensions/memdebug.html#MemoryDebugger)[¶](#scrapy.extensions.memdebug.MemoryDebugger)

An extension for debugging memory usage. It collects information about:

* objects uncollected by the Python garbage collector
* objects left alive that shouldn’t. For more info, see [Debugging memory leaks with trackref](leaks.html#topics-leaks-trackrefs)

To enable this extension, turn on the [`MEMDEBUG_ENABLED`](settings.html#std-setting-MEMDEBUG_ENABLED) setting. The info will be stored in the stats.

#### Spider state extension[¶](#module-scrapy.extensions.spiderstate)

*class*scrapy.extensions.spiderstate.SpiderState[[source]](../_modules/scrapy/extensions/spiderstate.html#SpiderState)[¶](#scrapy.extensions.spiderstate.SpiderState)

Manages spider state data by loading it before a crawl and saving it after.

Give a value to the [`JOBDIR`](settings.html#std-setting-JOBDIR) setting to enable this extension. When enabled, this extension manages the [`state`](spiders.html#scrapy.Spider.state) attribute of your [`Spider`](spiders.html#scrapy.Spider) instance:

* When your spider closes ([`spider_closed`](signals.html#std-signal-spider_closed)), the contents of its [`state`](spiders.html#scrapy.Spider.state) attribute are serialized into a file named `spider.state` in the [`JOBDIR`](settings.html#std-setting-JOBDIR) folder.
* When your spider opens ([`spider_opened`](signals.html#std-signal-spider_opened)), if a previously-generated `spider.state` file exists in the [`JOBDIR`](settings.html#std-setting-JOBDIR) folder, it is loaded into the [`state`](spiders.html#scrapy.Spider.state) attribute.

For an example, see [Keeping persistent state between batches](jobs.html#topics-keeping-persistent-state-between-batches).

#### Close spider extension[¶](#module-scrapy.extensions.closespider)

*class*scrapy.extensions.closespider.CloseSpider[[source]](../_modules/scrapy/extensions/closespider.html#CloseSpider)[¶](#scrapy.extensions.closespider.CloseSpider)

Closes a spider automatically when some conditions are met, using a specific closing reason for each condition.

The conditions for closing a spider can be configured through the following settings:

* [`CLOSESPIDER_TIMEOUT`](#std-setting-CLOSESPIDER_TIMEOUT)
* [`CLOSESPIDER_TIMEOUT_NO_ITEM`](#std-setting-CLOSESPIDER_TIMEOUT_NO_ITEM)
* [`CLOSESPIDER_ITEMCOUNT`](#std-setting-CLOSESPIDER_ITEMCOUNT)
* [`CLOSESPIDER_PAGECOUNT`](#std-setting-CLOSESPIDER_PAGECOUNT)
* [`CLOSESPIDER_ERRORCOUNT`](#std-setting-CLOSESPIDER_ERRORCOUNT)

Note

When a certain closing condition is met, requests which are currently in the downloader queue (up to [`CONCURRENT_REQUESTS`](settings.html#std-setting-CONCURRENT_REQUESTS) requests) are still processed.

##### CLOSESPIDER\_TIMEOUT[¶](#closespider-timeout)

Default: `0`

An integer which specifies a number of seconds. If the spider remains open for more than that number of second, it will be automatically closed with the reason `closespider_timeout`. If zero (or non set), spiders won’t be closed by timeout.

##### CLOSESPIDER\_TIMEOUT\_NO\_ITEM[¶](#closespider-timeout-no-item)

Default: `0`

An integer which specifies a number of seconds. If the spider has not produced any items in the last number of seconds, it will be closed with the reason `closespider_timeout_no_item`. If zero (or non set), spiders won’t be closed regardless if it hasn’t produced any items.

##### CLOSESPIDER\_ITEMCOUNT[¶](#closespider-itemcount)

Default: `0`

An integer which specifies a number of items. If the spider scrapes more than that amount and those items are passed by the item pipeline, the spider will be closed with the reason `closespider_itemcount`. If zero (or non set), spiders won’t be closed by number of passed items.

##### CLOSESPIDER\_PAGECOUNT[¶](#closespider-pagecount)

Default: `0`

An integer which specifies the maximum number of responses to crawl. If the spider crawls more than that, the spider will be closed with the reason `closespider_pagecount`. If zero (or non set), spiders won’t be closed by number of crawled responses.

##### CLOSESPIDER\_PAGECOUNT\_NO\_ITEM[¶](#closespider-pagecount-no-item)

Default: `0`

An integer which specifies the maximum number of consecutive responses to crawl without items scraped. If the spider crawls more consecutive responses than that and no items are scraped in the meantime, the spider will be closed with the reason `closespider_pagecount_no_item`. If zero (or not set), spiders won’t be closed by number of crawled responses with no items.

##### CLOSESPIDER\_ERRORCOUNT[¶](#closespider-errorcount)

Default: `0`

An integer which specifies the maximum number of errors to receive before closing the spider. If the spider generates more than that number of errors, it will be closed with the reason `closespider_errorcount`. If zero (or non set), spiders won’t be closed by number of errors.

#### StatsMailer extension[¶](#module-scrapy.extensions.statsmailer)

*class*scrapy.extensions.statsmailer.StatsMailer[[source]](../_modules/scrapy/extensions/statsmailer.html#StatsMailer)[¶](#scrapy.extensions.statsmailer.StatsMailer)

This simple extension can be used to send a notification e-mail every time a domain has finished scraping, including the Scrapy stats collected. The email will be sent to all recipients specified in the [`STATSMAILER_RCPTS`](settings.html#std-setting-STATSMAILER_RCPTS) setting.

Emails can be sent using the [`MailSender`](email.html#scrapy.mail.MailSender) class. To see a full list of parameters, including examples on how to instantiate [`MailSender`](email.html#scrapy.mail.MailSender) and use mail settings, see [Sending e-mail](email.html#topics-email).

#### Periodic log extension[¶](#periodic-log-extension)

*class*scrapy.extensions.periodic\_log.PeriodicLog[[source]](../_modules/scrapy/extensions/periodic_log.html#PeriodicLog)[¶](#scrapy.extensions.periodic_log.PeriodicLog)

This extension periodically logs rich stat data as a JSON object:

```
2023-08-0402:30:57[scrapy.extensions.logstats]INFO:Crawled976pages(at162pages/min),scraped925items(at161items/min)2023-08-0402:30:57[scrapy.extensions.periodic_log]INFO:{"delta":{"downloader/request_bytes":55582,"downloader/request_count":162,"downloader/request_method_count/GET":162,"downloader/response_bytes":618133,"downloader/response_count":162,"downloader/response_status_count/200":162,"item_scraped_count":161},"stats":{"downloader/request_bytes":338243,"downloader/request_count":992,"downloader/request_method_count/GET":992,"downloader/response_bytes":3836736,"downloader/response_count":976,"downloader/response_status_count/200":976,"item_scraped_count":925,"log_count/INFO":21,"log_count/WARNING":1,"scheduler/dequeued":992,"scheduler/dequeued/memory":992,"scheduler/enqueued":1050,"scheduler/enqueued/memory":1050},"time":{"elapsed":360.008903,"log_interval":60.0,"log_interval_real":60.006694,"start_time":"2023-08-03 23:24:57","utcnow":"2023-08-03 23:30:57"}}
```

This extension logs the following configurable sections:

* `"delta"` shows how some numeric stats have changed since the last stats log message.
  
  The [`PERIODIC_LOG_DELTA`](#std-setting-PERIODIC_LOG_DELTA) setting determines the target stats. They must have `int` or `float` values.
* `"stats"` shows the current value of some stats.
  
  The [`PERIODIC_LOG_STATS`](#std-setting-PERIODIC_LOG_STATS) setting determines the target stats.
* `"time"` shows detailed timing data.
  
  The [`PERIODIC_LOG_TIMING_ENABLED`](#std-setting-PERIODIC_LOG_TIMING_ENABLED) setting determines whether or not to show this section.

This extension logs data at the start, then on a fixed time interval configurable through the [`LOGSTATS_INTERVAL`](settings.html#std-setting-LOGSTATS_INTERVAL) setting, and finally right before the crawl ends.

Example extension configuration:

```
custom_settings={"LOG_LEVEL":"INFO","PERIODIC_LOG_STATS":{"include":["downloader/","scheduler/","log_count/","item_scraped_count/"],},"PERIODIC_LOG_DELTA":{"include":["downloader/"]},"PERIODIC_LOG_TIMING_ENABLED":True,"EXTENSIONS":{"scrapy.extensions.periodic_log.PeriodicLog":0,},}
```
##### PERIODIC\_LOG\_DELTA[¶](#periodic-log-delta)

Default: `None`

* `"PERIODIC_LOG_DELTA":True` - show deltas for all `int` and `float` stat values.
* `"PERIODIC_LOG_DELTA":{"include":["downloader/","scheduler/"]}` - show deltas for stats with names containing any configured substring.
* `"PERIODIC_LOG_DELTA":{"exclude":["downloader/"]}` - show deltas for all stats with names not containing any configured substring.
##### PERIODIC\_LOG\_STATS[¶](#periodic-log-stats)

Default: `None`

* `"PERIODIC_LOG_STATS":True` - show the current value of all stats.
* `"PERIODIC_LOG_STATS":{"include":["downloader/","scheduler/"]}` - show current values for stats with names containing any configured substring.
* `"PERIODIC_LOG_STATS":{"exclude":["downloader/"]}` - show current values for all stats with names not containing any configured substring.
##### PERIODIC\_LOG\_TIMING\_ENABLED[¶](#periodic-log-timing-enabled)

Default: `False`

`True` enables logging of timing data (i.e. the `"time"` section).

### Debugging extensions[¶](#debugging-extensions)

#### Stack trace dump extension[¶](#stack-trace-dump-extension)

*class*scrapy.extensions.periodic\_log.StackTraceDump[¶](#scrapy.extensions.periodic_log.StackTraceDump)

Dumps information about the running process when a [SIGQUIT](https://en.wikipedia.org/wiki/SIGQUIT) or [SIGUSR2](https://en.wikipedia.org/wiki/SIGUSR1_and_SIGUSR2) signal is received. The information dumped is the following:

1. engine status (using `scrapy.utils.engine.get_engine_status()`)
2. live references (see [Debugging memory leaks with trackref](leaks.html#topics-leaks-trackrefs))
3. stack trace of all threads

After the stack trace and engine status is dumped, the Scrapy process continues running normally.

This extension only works on POSIX-compliant platforms (i.e. not Windows), because the [SIGQUIT](https://en.wikipedia.org/wiki/SIGQUIT) and [SIGUSR2](https://en.wikipedia.org/wiki/SIGUSR1_and_SIGUSR2) signals are not available on Windows.

There are at least two ways to send Scrapy the [SIGQUIT](https://en.wikipedia.org/wiki/SIGQUIT) signal:

1. By pressing Ctrl-while a Scrapy process is running (Linux only?)
2. By running this command (assuming `<pid>` is the process id of the Scrapy process):
   
   ```
   kill-QUIT<pid>
   ```
#### Debugger extension[¶](#debugger-extension)

*class*scrapy.extensions.periodic\_log.Debugger[¶](#scrapy.extensions.periodic_log.Debugger)

Invokes a [Python debugger](https://docs.python.org/3/library/pdb.html) inside a running Scrapy process when a [SIGUSR2](https://en.wikipedia.org/wiki/SIGUSR1_and_SIGUSR2) signal is received. After the debugger is exited, the Scrapy process continues running normally.

This extension only works on POSIX-compliant platforms (i.e. not Windows).

 [Previous](spider-middleware.html)[Next](signals.html) 

---

© Copyright Scrapy developers. Last updated on Nov 19, 2024. 

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

---

Close