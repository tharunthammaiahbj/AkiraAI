Sales analytics - Business Central | Microsoft Learn[Skip to main content](#main)

Microsoft Learn Challenge
-------------------------

Nov 23, 2024 – Jan 10, 2025

Build skills in the latest technologies and earn a digital badge by January 10!

[Register now](https://aka.ms/MSIgniteChallenge/Tier1Banner?wt.mc_id=ignite24_learnbanner_tier1_cnl)Dismiss alert

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881 )[More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)Table of contentsExit focus mode[Read in English](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-analytics-overview)Save

* Add to Collections
* Add to Plan
Table of contents[Read in English](https://learn.microsoft.com/en-us/dynamics365/business-central/sales-analytics-overview)Add to CollectionsAdd to Plan[Edit](https://github.com/MicrosoftDocs/dynamics365smb-docs/blob/main/business-central/sales-analytics-overview.md)

---

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview%3FWT.mc_id%3Dfacebook)[x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Sales%20analytics%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview%3FWT.mc_id%3Dtwitter)[LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Sales%20analytics%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview%3FWT.mc_id%3Dlinkedin)[Email](mailto:?subject=%5BShared%20Article%5D%20Sales%20analytics%20-%20Business%20Central%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Sales%20analytics%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview%3FWT.mc_id%3Demail)

---

PrintTable of contents

Sales analytics
===============

* Article
* 11/11/2024
* 2 contributors
Feedback

In this article
---------------

1. [Analytics needs in sales](#analytics-needs-in-sales)
2. [Using Power BI to monitor sales KPIs](#using-power-bi-to-monitor-sales-kpis)
3. [Use financial reporting to produce financial statements and KPIs related to sales](#use-financial-reporting-to-produce-financial-statements-and-kpis-related-to-sales)
4. [Finance reporting across business units or legal entities related to sales](#finance-reporting-across-business-units-or-legal-entities-related-to-sales)
5. [Ad-hoc analysis of sales data](#ad-hoc-analysis-of-sales-data)
6. [Built-in reports for sales](#built-in-reports-for-sales)
7. [On-screen sales analytics](#on-screen-sales-analytics)
8. [See also](#see-also)
9. [Start a free trial!](#section)

Show 5 more

Businesses capture lots of data during daily activities that supports business intelligence (BI) for sales managers:

* Opportunities
* Sales quotes
* Sales orders
* Sales invoices

Business Central provides features to help you gather, analyze, and share your organization's sales data:

* Power BI reports for sales
* Ad-hoc analysis on lists
* Ad-hoc analysis of data in Excel (using Open in Excel)
* Built-in sales analytics tools
* Built-in sales reports

Each of these features has its advantages and disadvantages, depending on the type of data analysis and the role of the user. To learn more, go to [Analytics, business intelligence, and reporting overview](reports-bi-reporting).

This article introduces how you can use these analytical features to gain sales insights.

Analytics needs in sales
------------------------

When you think about the analytics needs in sales management, it might help to use a persona-based model that describes different analytics needs at a high-level.

[![](/en-us/dynamics365/business-central/dev-itpro/developer/media/analytics-personas.svg)](/en-us/dynamics365/business-central/dev-itpro/developer/media/analytics-personas.svg#lightbox)

People in different roles have different needs when it comes to data, and they use the data in different ways. For example, people in asset management and finance interact with data differently than people in sales.

[![](/en-us/dynamics365/business-central/dev-itpro/developer/media/analytics-personas-scenarios.svg)](/en-us/dynamics365/business-central/dev-itpro/developer/media/analytics-personas-scenarios.svg#lightbox)

Expand table

| Role | Data aggregation | Typical ways to consume data |
| --- | --- | --- |
| CCO / CFO / CEO | Performance data | KPIs  Dashboards  Financial reports |
| Sales Manager | Trends, summaries | Built-in managerial reports  Ad-hoc analysis |
| Account Manager / Sales Person | Detailed data | Built-in operational reports  On-screen task data |

Using Power BI to monitor sales KPIs
------------------------------------

A key performance indicator (KPI) is a measurable value that shows how effectively you’re meeting your goals. In sales, people often use the following KPIs to monitor their sales organization's performance:

* Gross Profit
* Gross Profit Margin
* Sales by period
* Sales vs. budget
* Number of new customers
* Period-over-Period Sales Amount Growth
* Sales by item/customer/location/sales person

[![](media/powerbi/sales/sales-overview.png)](media/powerbi/sales/sales-overview.png#lightbox)

These sales KPIs, and more, are available in the Power BI Sales app for Business Central. To learn more, go to [Power BI sales app](sales-powerbi-app).

The following table describes the reports in the Power BI Sales app and how you can use them.

Expand table

| To... | Open in Business Central (CTRL+select) | Learn more |
| --- | --- | --- |
| Analyze high level information on sales activities. Identify sales figures for quantity or amounts from both posted and unposted documents. | [Sales Overview](https://businesscentral.dynamics.com?page=36998) | [About Sales Overview](sales-powerbi-sales-overview) |
| Analyze sales by weekday over different periods. The heat maps highlight the days on which you sell the most, which helps you identify patterns in your sales. | [Daily Sales](https://businesscentral.dynamics.com?page=36999) | [About Daily Sales](sales-powerbi-daily-sales) |
| Analyze sales trends by smoothing out spikes and drops using the **30 Day Moving Averages** report. | [Moving Average](https://businesscentral.dynamics.com?page=37000) | [About Moving Average](sales-powerbi-moving-average) |
| Analyze the aggregated sales over a rolling 12-month period. Use this analysis as an alternative to a Year-to-Date report. | [Moving Annual Total](https://businesscentral.dynamics.com?page=37001) | [About Moving Annual Total](sales-powerbi-moving-annual-total) |
| Compare sales in one period with the same period in a prior year, quarter, or month. | [Period-Over-Period Growth](https://businesscentral.dynamics.com?page=37002) | [About Period-Over-Period Growth](sales-powerbi-period-over-period-growth) |
| Analyze accumulating sales for a desired period. | [Month-To-Date](https://businesscentral.dynamics.com?page=37003) | [About Month-To-Date](sales-powerbi-month-to-date) |
| Analyze sales by item and view key sales metrics as a percentage of total sales. | [Sales by Item](https://businesscentral.dynamics.com?page=37004) | [About Sales by Item](sales-powerbi-sales-by-item) |
| Analyze sales by customer and view key metrics. Metrics include sales amount, sales quantity, cost amount, gross profit, gross profit margin, and the sales amount as a percent of total sales. | [Sales by Customer](https://businesscentral.dynamics.com?page=37005) | [About Sales by Customer](sales-powerbi-sales-by-customer) |
| Analyze sales by salesperson and view key metrics. Metrics include sales amount, sales quantity, cost amount, gross profit, gross profit margin, and the sales amount as a percent of total sales. | [Sales by Salesperson](https://businesscentral.dynamics.com?page=37006) | [About Sales by Salesperson](sales-powerbi-sales-by-salesperson) |
| Analyze sales by location and view key metrics. Metrics include sales amount, sales quantity, cost amount, gross profit, gross profit margin, and the sales amount as a percent of total sales. | [Sales by Location](https://businesscentral.dynamics.com?page=ID) | [About Sales by Location](sales-powerbi-sales-by-location) |
| Analyze item sales budgets against actual sales. View target variances for both sales amounts and sales quantity. | [Actual vs. Budget](https://businesscentral.dynamics.com?page=37008) | [About Actual vs. Budget](sales-powerbi-actual-vs-budget) |

 Tip

You can easily track the KPIs that the Power BI reports display against your business objectives. To learn more, go to [Track your business KPIs with Power BI metrics](track-kpis-with-power-bi-metrics).

Use financial reporting to produce financial statements and KPIs related to sales
---------------------------------------------------------------------------------

The **Financial Reporting** feature gives you insights into the financial data shown on your chart of accounts (COA). You can set up financial reports to analyze figures in general ledger (G/L) accounts, and compare general ledger entries with budget entries. Specifically for sales management, you can set up financial reports on the general ledger (G/L) accounts that you use to track sales postings.

Dimensions play an important role in business intelligence. A dimension is data that you add to an entry as a parameter. Dimensions let you group entries that have similar characteristics, such as customers, regions, products, and salesperson. Among other purposes, use dimensions when you define analysis views and create financial reports. To learn more, go to [Work with Dimensions](finance-dimensions).

To learn more about financial reports, go to [Prepare Financial Reports with Financial Data and Account Categories](bi-how-work-account-schedule).

Finance reporting across business units or legal entities related to sales
--------------------------------------------------------------------------

Some organizations use Business Central in multiple business units or legal entities. Others use Business Central in subsidiaries that report to parent organizations. Business Central gives accountants tools that help them transfer general ledger entries from two or more companies (subsidiaries) into a consolidated company. Specifically for sales management, you might want to consolidate general ledger entries for your sales accounts to be able to track sales KPIs across business units or legal entities.

To learn more, go to [Company consolidation](finance-consolidated-company-reporting).

Ad-hoc analysis of sales data
-----------------------------

Sometimes, you just need to check whether the numbers add up correctly, or quickly confirm a figure. The following features are great for ad-hoc analyses:

* Data analysis on ledger list pages
* Open in Excel

The Data Analysis feature lets you open almost any list page, such as **General Ledger Entries**, **Customer Ledger Entries**, **Item Ledger Entries**, or **Posted Invoices**, enter analysis mode, and then group, filter, and pivot data as you see fit.

[![](media/data-analysis-customer-ledger-entries.png)](media/data-analysis-customer-ledger-entries.png#lightbox)

Similarly, you can use the **Open in Excel** action to open a list page, optionally filter the list to a subset of the data, and then use Excel to work with the data. For example, by using features such as Analyze Data, What-If Analysis, or Forecast Sheet.

[![](media/open-in-excel-customer-ledger-entries.png)](media/open-in-excel-customer-ledger-entries.png#lightbox)

 Tip

If you configure OneDrive for system features, the Excel workbook opens in your browser.

To learn more about how to do ad-hoc analysis on sales data, go to [Ad hoc analysis of sales data](ad-hoc-analysis-sales).

Built-in reports for sales
--------------------------

Business Central includes several built-in reports, tracing functions, and tools to help sales organizations report on their data.

To get an overview of the reports that are available for sales, choose **All Reports** on your Home page. This action opens the Role Explorer, which is filtered to the features in the **Report & Analysis** option. Under the **Sales and Marketing** heading, choose **Explore**.

[![](media/report-explorer-sales.png)](media/report-explorer-sales.png#lightbox)

The built-in sales reports come in two flavors:

* Designed for print (pdf).
* Designed for analysis in Excel.

To learn more, go to [Finding Reports with the Role Explorer](ui-role-explorer).

On-screen sales analytics
-------------------------

Business Central has several pages that give you sales overviews and tasks to do. Here are some examples to get you started:

* [Open the Sales Quotes list](https://businesscentral.dynamics.com/?page=9300)
* [Open the Sales Orders list](https://businesscentral.dynamics.com/?page=9305)
* [Open the Posted Sales Invoices list](https://businesscentral.dynamics.com/?page=143)
* [Open the Sales Return Orders list](https://businesscentral.dynamics.com/?page=9304)
* [Calculate order promising dates](sales-how-to-calculate-order-promising-dates)
* [Calculate delivery dates for sales orders](sales-date-calculation-for-sales)
* [Track packages](sales-how-track-packages)
* [View the Availability of Items](inventory-how-availability-overview)
* [Blanket sales order status](sales-how-to-create-blanket-sales-orders#to-view-the-status-of-a-blanket-sales-order)
* [View unposted and posted blanket sales order lines](sales-how-to-create-blanket-sales-orders#to-view-unposted-and-posted-blanket-sales-order-lines)

### Show sales-related general ledger entries and balances from the Chart of Accounts page

The **Chart of Accounts** page shows all general ledger accounts with aggregated numbers posted to the general ledger. From this page, you can do things like:

* View reports that show general ledger entries and balances.
* Review a list of posting groups for that account.
* View separate debit and credit balances for a single account.

Specifically for sales, you can create a view that only shows the accounts you use for posting sales entries.

[![](media/chart-of-accounts-page.png)](media/chart-of-accounts-page.png#lightbox)

To learn more, go to [Understand the Chart of Accounts](finance-general-ledger#the-chart-of-accounts).

### Analyze data by dimensions (related to sales)

Dimensions are values that categorize entries so you can track and analyze them on documents, such as sales orders. Dimensions can, for example, indicate the project or department an entry came from.

So, instead of setting up separate general ledger accounts for each department or location, you can use dimensions as a basis for analysis and avoid having to create a complicated chart of accounts structure.

To learn more, go to [Analyze Data by Dimensions](bi-how-analyze-data-dimension).

See also
--------

[Company consolidation](finance-consolidated-company-reporting)  
[Power BI sales app](sales-powerbi-app)  
[Prepare Financial Reports with Financial Data and Account Categories](bi-how-work-account-schedule)  
[Handling finance reporting across business units or legal entities](finance-consolidated-company-reporting)  
[Ad hoc analysis of sales data](ad-hoc-analysis-sales)  
[Built-in sales reports](sales-reports)  
[Understand the Chart of Accounts](finance-general-ledger#the-chart-of-accounts)  
[Analyze Data by Dimensions](bi-how-analyze-data-dimension)  
[Analytics, business intelligence, and reporting overview](reports-bi-reporting)  
[Work with Business Central](ui-work-product)

Start a [free trial!](https://go.microsoft.com/fwlink/?linkid=847861)
---------------------------------------------------------------------

[Find free e-learning modules for Business Central here](/en-us/training/dynamics365/business-central)

---

Feedback
--------

Was this page helpful?

YesNo[Provide product feedback](https://experience.dynamics.com/ideas/categories/?forum=e288ef32-82ed-e611-8101-5065f38b21f1&forumName=Dynamics%20365%20Business%20Central)

---

Additional resources
--------------------

---

 Events

 [Join us at FabCon Vegas](https://aka.ms/fabcon25/lt2?ocid=fabcon25_learn_bannert2_azdata) 

Mar 31, 11 PM - Apr 2, 11 PM

The ultimate Microsoft Fabric, Power BI, SQL, and AI community-led event. March 31 to April 2, 2025.

 [Register today](https://aka.ms/fabcon25/lt2?ocid=fabcon25_learn_bannert2_azdata) [English (United States)](/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview)[California Consumer Privacy Act (CCPA) Opt-Out IconYour Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

* Light
* Dark
* High contrast


* [Previous Versions](/en-us/previous-versions/)
* [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
* [Contribute](/en-us/contribute/)
* [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
* [Terms of Use](/en-us/legal/termsofuse)
* [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
* © Microsoft 2024

Additional resources
--------------------

---

 Events

 [Join us at FabCon Vegas](https://aka.ms/fabcon25/lt2?ocid=fabcon25_learn_bannert2_azdata) 

Mar 31, 11 PM - Apr 2, 11 PM

The ultimate Microsoft Fabric, Power BI, SQL, and AI community-led event. March 31 to April 2, 2025.

 [Register today](https://aka.ms/fabcon25/lt2?ocid=fabcon25_learn_bannert2_azdata) 
### In this article

[English (United States)](/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Fsales-analytics-overview)[California Consumer Privacy Act (CCPA) Opt-Out IconYour Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

* Light
* Dark
* High contrast


* [Previous Versions](/en-us/previous-versions/)
* [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
* [Contribute](/en-us/contribute/)
* [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
* [Terms of Use](/en-us/legal/termsofuse)
* [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
* © Microsoft 2024
