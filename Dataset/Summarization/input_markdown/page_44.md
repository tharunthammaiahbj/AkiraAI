Rules for automatic application of payments - Business Central | Microsoft Learn[Skip to main content](#main)

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881 )[More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)Table of contentsExit focus mode[Read in English](https://learn.microsoft.com/en-us/dynamics365/business-central/receivables-how-set-up-payment-application-rules)Save

* Add to Collections
* Add to Plan
Table of contents[Read in English](https://learn.microsoft.com/en-us/dynamics365/business-central/receivables-how-set-up-payment-application-rules)Add to CollectionsAdd to Plan[Edit](https://github.com/MicrosoftDocs/dynamics365smb-docs/blob/main/business-central/receivables-how-set-up-payment-application-rules.md)

---

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules%3FWT.mc_id%3Dfacebook)[x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Rules%20for%20automatic%20application%20of%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules%3FWT.mc_id%3Dtwitter)[LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Rules%20for%20automatic%20application%20of%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules%3FWT.mc_id%3Dlinkedin)[Email](mailto:?subject=%5BShared%20Article%5D%20Rules%20for%20automatic%20application%20of%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Rules%20for%20automatic%20application%20of%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules%3FWT.mc_id%3Demail)

---

PrintTable of contents

Set up rules for automatic application of payments
==================================================

* Article
* 07/08/2024
* 9 contributors
Feedback

In this article
---------------

1. [To set up a payment application rule](#to-set-up-a-payment-application-rule)
2. [See also](#see-also)

On the **Payment Application Rules** page, you set up rules to govern how payment text (on a bank transaction) is automatically matched with text on related open (unpaid) invoices, credit memos, or other entries when you use the **Apply Automatically** function on the **Payment Reconciliation Journal** page. For more information, see [Reconcile payments using automatic application](receivables-how-reconcile-payments-auto-application).

You set up new payment application rules by choosing which types of data on a payment reconciliation journal line must match with data on one or more open entries before the related payment is automatically applied to the open entries. The quality of each automatic application is shown as a value of **Low** to **High** in the **Match Confidence** field on the **Payment Reconciliation Journal** page according to the payment application rule that was used.

Each row on the **Payment Application Rules** page represents a payment application rule. Rules are applied in the order specified by the **Sorting Order** field. If multiple rules are used simultaneously, then the match confidence of the highest sorted rule is used.

The automatic application function is based on prioritized matching criteria. First the function tries, in prioritized order, to match text in the five **Related-Party** fields on a journal line with text in the bank account, name, or address of customers or vendors with unpaid documents representing open entries. Then, the function tries to match text in the **Transaction Text** and **Additional Transaction Info** fields on a journal line with text in the **External Document No.** and **Document No.** fields on open entries. Last, the function tries to match the amount in the **Statement Amount** field on a journal line with the amount on open entries.

 Note

Text matching is only possible for text longer than four characters.

In addition to the matching criteria, the following applies concerning the sign of the payment amount:

* For negative amounts, a match is made first against open entries representing customer invoices and then against vendor credit memos.
* For positive amounts, a match is made first against open entries representing vendor invoices and then against customer credit memos.

To set up a payment application rule
------------------------------------

1. Choose the ![](media/ui-search/search_small.png) icon, enter **Payment Application Rules**, and then choose the related link.
2. Define a new or edited payment application rule by filling the fields on a line as described in the following table.

Expand table

| Field | Description |
| --- | --- |
| **Match Confidence** | Specifies your confidence in the application rule that you define on the line. A value that you specify in this field is shown in the **Match Confidence** field on the **Payment Reconciliation Journal** page according to the quality of the automatic payment application on the journal line. |
| **Priority** | Specifies the priority of the application rule relative to other application rules that are defined as lines on the **Payment Application Rules** page. 1 represents the highest priority. |
| **Related Party Matched** | Specifies how much information about the customer or vendor, such as address, city name, and bank account number, on the payment reconciliation journal line must match with information about the open entry before the application rule will be used to automatically apply the payment to the open entry. |
| **Document No./Ext. Document No. Matched** | Specifies whether text on the payment reconciliation journal line must match with the value in the **Document No.** field or the **External Document No.** field on the open entry before the application rule will be used to automatically apply the payment to the open entry. |
| **Number of Entries Within Amount Tolerance Found** | Specifies how many entries for a customer or vendor must match the amount including payment tolerance before the application rule will be used to automatically apply a payment to the open entry. |
| **Review Required** | Specifies whether the automatic payment application is recommended for manual review by the user before posting. Choosing the **Lines to Review** field on the **Payment Application Journal** page starts a guided experience where you can easily review multiple applications in a sequence on the **Payment Application Review** page. |

The following table describes the standard payment application rules in Business Central.

 Important

The payment application rules may be different in your implementation of Business Central.

Expand table

| Match Confidence | Priority | Related Party Matched | Document No./Ext. Document No. Matched | Number of Entries Within Amount Tolerance Found |
| --- | --- | --- | --- | --- |
| High | 1 | Fully | Yes - Multiple | One Match |
| High | 2 | Fully | Yes - Multiple | Multiple Matches |
| High | 3 | Fully | Yes | One Match |
| High | 4 | Fully | Yes | Multiple Matches |
| High | 5 | Partially | Yes - Multiple | One Match |
| High | 6 | Partially | Yes - Multiple | Multiple Matches |
| High | 7 | Partially | Yes | One Match |
| High | 8 | Fully | No | One Match |
| High | 9 | No | Yes - Multiple | One Match |
| High | 10 | No | Yes - Multiple | Multiple Matches |
| Medium | 1 | Fully | Yes - Multiple | Not Considered |
| Medium | 2 | Fully | Yes | Not Considered |
| Medium | 3 | Fully | No | Multiple Matches |
| Medium | 4 | Partially | Yes - Multiple | Not Considered |
| Medium | 5 | Partially | Yes | Not Considered |
| Medium | 6 | No | Yes | One Match |
| Medium | 7 | No | Yes-Multiple | Not Considered |
| Medium | 8 | Partially | No | One Match |
| Medium | 9 | No | Yes | Not Considered |
| Low | 1 | Fully | No | No Matches |
| Low | 2 | Partially | No | Multiple Matches |
| Low | 3 | Partially | No | No Matches |
| Low | 4 | No | No | One Match |
| Low | 5 | No | No | Multiple Matches |

See also
--------

[Reconcile Payments Using Automatic Application](receivables-how-reconcile-payments-auto-application)  
[Managing Receivables](receivables-manage-receivables)  
[Sales](sales-manage-sales)  
[Work with Business Central](ui-work-product)

[Find free e-learning modules for Business Central here](/en-us/training/dynamics365/business-central)

---

Feedback
--------

Was this page helpful?

YesNo[Provide product feedback](https://experience.dynamics.com/ideas/categories/?forum=e288ef32-82ed-e611-8101-5065f38b21f1&forumName=Dynamics%20365%20Business%20Central)

---

Additional resources
--------------------

[English (United States)](/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules)[California Consumer Privacy Act (CCPA) Opt-Out IconYour Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

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

### In this article

[English (United States)](/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-set-up-payment-application-rules)[California Consumer Privacy Act (CCPA) Opt-Out IconYour Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

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
