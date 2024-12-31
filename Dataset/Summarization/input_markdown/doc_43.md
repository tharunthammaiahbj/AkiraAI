Sending e-mail — Scrapy 2.12.0 documentation [Scrapy](../index.html)  2.12 

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
* [Sending e-mail](#)
  + [Quick example](#quick-example)
  + [MailSender class reference](#mailsender-class-reference)
    - [`MailSender`](#scrapy.mail.MailSender)
      * [`MailSender.from_crawler()`](#scrapy.mail.MailSender.from_crawler)
      * [`MailSender.send()`](#scrapy.mail.MailSender.send)
  + [Mail settings](#mail-settings)
    - [MAIL\_FROM](#mail-from)
    - [MAIL\_HOST](#mail-host)
    - [MAIL\_PORT](#mail-port)
    - [MAIL\_USER](#mail-user)
    - [MAIL\_PASS](#mail-pass)
    - [MAIL\_TLS](#mail-tls)
    - [MAIL\_SSL](#mail-ssl)
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


* Sending e-mail
* [View page source](../_sources/topics/email.rst.txt)

---

Sending e-mail[¶](#module-scrapy.mail)
======================================

Although Python makes sending e-mails relatively easy via the [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib) library, Scrapy provides its own facility for sending e-mails which is very easy to use and it’s implemented using [Twisted non-blocking IO](https://docs.twisted.org/en/stable/core/howto/defer-intro.html), to avoid interfering with the non-blocking IO of the crawler. It also provides a simple API for sending attachments and it’s very easy to configure, with a few [settings](#topics-email-settings).

Quick example[¶](#quick-example)
--------------------------------

There are two ways to instantiate the mail sender. You can instantiate it using the standard `__init__` method:

```
fromscrapy.mailimportMailSendermailer=MailSender()
```

Or you can instantiate it passing a `scrapy.Crawler` instance, which will respect the [settings](#topics-email-settings):

```
mailer=MailSender.from_crawler(crawler)
```

And here is how to use it to send an e-mail (without attachments):

```
mailer.send(to=["someone@example.com"],subject="Some subject",body="Some body",cc=["another@example.com"],)
```

MailSender class reference[¶](#mailsender-class-reference)
----------------------------------------------------------

MailSender is the preferred class to use for sending emails from Scrapy, as it uses [Twisted non-blocking IO](https://docs.twisted.org/en/stable/core/howto/defer-intro.html), like the rest of the framework.

*class*scrapy.mail.MailSender(*smtphost=None*, *mailfrom=None*, *smtpuser=None*, *smtppass=None*, *smtpport=None*)[[source]](../_modules/scrapy/mail.html#MailSender)[¶](#scrapy.mail.MailSender)Parameters:

* **smtphost** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *or* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)) – the SMTP host to use for sending the emails. If omitted, the [`MAIL_HOST`](#std-setting-MAIL_HOST) setting will be used.
* **mailfrom** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the address used to send emails (in the `From:` header). If omitted, the [`MAIL_FROM`](#std-setting-MAIL_FROM) setting will be used.
* **smtpuser** – the SMTP user. If omitted, the [`MAIL_USER`](#std-setting-MAIL_USER) setting will be used. If not given, no SMTP authentication will be performed.
* **smtppass** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *or* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes)) – the SMTP pass for authentication.
* **smtpport** ([*int*](https://docs.python.org/3/library/functions.html#int)) – the SMTP port to connect to
* **smtptls** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – enforce using SMTP STARTTLS
* **smtpssl** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – enforce using a secure SSL connection
*classmethod*from\_crawler(*crawler*)[[source]](../_modules/scrapy/mail.html#MailSender.from_crawler)[¶](#scrapy.mail.MailSender.from_crawler)

Instantiate using a `scrapy.Crawler` instance, which will respect [these Scrapy settings](#topics-email-settings).

Parameters:

**crawler** – the crawler

send(*to*, *subject*, *body*, *cc=None*, *attachs=()*, *mimetype='text/plain'*, *charset=None*)[[source]](../_modules/scrapy/mail.html#MailSender.send)[¶](#scrapy.mail.MailSender.send)

Send email to the given recipients.

Parameters:

* **to** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list)) – the e-mail recipients as a string or as a list of strings
* **subject** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the subject of the e-mail
* **cc** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list)) – the e-mails to CC as a string or as a list of strings
* **body** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the e-mail body
* **attachs** ([*collections.abc.Iterable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)) – an iterable of tuples `(attach_name,mimetype,file_object)` where `attach_name` is a string with the name that will appear on the e-mail’s attachment, `mimetype` is the mimetype of the attachment and `file_object` is a readable file object with the contents of the attachment
* **mimetype** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the MIME type of the e-mail
* **charset** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – the character encoding to use for the e-mail contents

Mail settings[¶](#mail-settings)
--------------------------------

These settings define the default `__init__` method values of the [`MailSender`](#scrapy.mail.MailSender) class, and can be used to configure e-mail notifications in your project without writing any code (for those extensions and code that uses [`MailSender`](#scrapy.mail.MailSender)).

### MAIL\_FROM[¶](#mail-from)

Default: `'scrapy@localhost'`

Sender email to use (`From:` header) for sending emails.

### MAIL\_HOST[¶](#mail-host)

Default: `'localhost'`

SMTP host to use for sending emails.

### MAIL\_PORT[¶](#mail-port)

Default: `25`

SMTP port to use for sending emails.

### MAIL\_USER[¶](#mail-user)

Default: `None`

User to use for SMTP authentication. If disabled no SMTP authentication will be performed.

### MAIL\_PASS[¶](#mail-pass)

Default: `None`

Password to use for SMTP authentication, along with [`MAIL_USER`](#std-setting-MAIL_USER).

### MAIL\_TLS[¶](#mail-tls)

Default: `False`

Enforce using STARTTLS. STARTTLS is a way to take an existing insecure connection, and upgrade it to a secure connection using SSL/TLS.

### MAIL\_SSL[¶](#mail-ssl)

Default: `False`

Enforce connecting using an SSL encrypted connection

 [Previous](stats.html)[Next](telnetconsole.html) 

---

© Copyright Scrapy developers. Last updated on Nov 19, 2024. 

 Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org). 

---

Close