Setting up Text-to-Account mapping for recurring payments - Business Central | Microsoft Learn[Skip to main content](#main)

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881 )[More info about Internet Explorer and Microsoft Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-microsoft-edge)Table of contentsExit focus mode[Read in English](https://learn.microsoft.com/en-us/dynamics365/business-central/receivables-how-map-text-recurring-payments-accounts-auto-reconcilliation)Save

* Add to Collections
* Add to Plan
Table of contents[Read in English](https://learn.microsoft.com/en-us/dynamics365/business-central/receivables-how-map-text-recurring-payments-accounts-auto-reconcilliation)Add to CollectionsAdd to Plan[Edit](https://github.com/MicrosoftDocs/dynamics365smb-docs/blob/main/business-central/receivables-how-map-text-recurring-payments-accounts-auto-reconcilliation.md)

---

#### Share via

[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation%3FWT.mc_id%3Dfacebook)[x.com](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation%3FWT.mc_id%3Dtwitter&text=Today%20I%20completed%20%22Setting%20up%20Text-to-Account%20mapping%20for%20recurring%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!&tw_p=tweetbutton&url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation%3FWT.mc_id%3Dtwitter)[LinkedIn](https://www.linkedin.com/feed/?shareActive=true&text=Today%20I%20completed%20%22Setting%20up%20Text-to-Account%20mapping%20for%20recurring%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation%3FWT.mc_id%3Dlinkedin)[Email](mailto:?subject=%5BShared%20Article%5D%20Setting%20up%20Text-to-Account%20mapping%20for%20recurring%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn&body=Today%20I%20completed%20%22Setting%20up%20Text-to-Account%20mapping%20for%20recurring%20payments%20-%20Business%20Central%20%7C%20Microsoft%20Learn%22!%20I'm%20so%20proud%20to%20be%20celebrating%20this%20achievement%20and%20hope%20this%20inspires%20you%20to%20start%20your%20own%20%40MicrosoftLearn%20journey!%0A%0D%0Ahttps%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation%3FWT.mc_id%3Demail)

---

PrintTable of contents

Map text on recurring payments to accounts for automatic reconciliation
=======================================================================

* Article
* 07/08/2024
* 9 contributors
Feedback

In this article
---------------

1. [To map text on recurring payments to accounts for automatic reconciliation](#to-map-text-on-recurring-payments-to-accounts-for-automatic-reconciliation)
2. [Example: Text-to-Account mapping for bank fees](#example-text-to-account-mapping-for-bank-fees)
3. [See also](#see-also)

On the **Text-to-Account Mapping** page, which you open from the **Payment Reconciliation Journal** page, you can set up mappings between text on payments and specific debit, credit, and balancing accounts so that such payments are posted to the specified accounts when you post the payment reconciliation journal.

Similar functionality exists to reconcile excess amounts on payment reconciliation journal lines on an ad-hoc basis. For more information, see [Reconcile Payments that Can't be Applied Automatically](receivables-how-reconcile-payments-cannot-apply-auto).

Payments posted based on text-to-account mapping are not applied to open entries, but are merely posted to the specified accounts in addition to creating bank account ledger entries. Accordingly, text-to-account mapping is suited for recurring cash receipts or expenses, such as frequent purchases of car fuel or bank fees and interest, that regularly occur on the bank statement and don't need a related business document. For more information, see the "Example - Text-to-Account Mapping for Fuel Expense" section in this article.

 Note

Payments on reconciliation journal lines are only set to posting according to text-to-account mapping if the automatic application function can only provide a match confidence of **Low** or **Medium**. If the automatic application function provides a match confidence of High, then the payment is automatically applied to one or more open entries, and the payment is not posted to the accounts specified on the **Text-to-Account Mapping** page. In other words, a match confidence of **High** overrules a text-to-account mapping.

On a payment reconciliation journal line where the payment has been set to posting according to text-to-account mapping, the **Match Confidence** field contains **High - Text-to-Account Mapping**, and the **Account Type** and **Account No.** fields contain the mapped accounts.

To map text on recurring payments to accounts for automatic reconciliation
--------------------------------------------------------------------------

1. Choose the ![](media/ui-search/search_small.png) icon, enter **Payment Reconciliation Journals**, and then choose the related link.
2. Open a payment reconciliation journal. For more information, see [Reconcile Payments Using Automatic Application](receivables-how-reconcile-payments-auto-application).
3. Choose the **Map Text to Account** action. The **Text-to-Account Mapping** page opens.
4. In the **Mapping Text** field, enter any text that occurs on payments that you want to post to specified accounts without applying to an open entry. You can enter up to 50 characters.
   
    Note
   
   If no other payments exist with the mapping text in question, then the text-to-account mapping will occur even when only a part of the text on the payment exists as a mapping text.
5. In the **Vendor No.** field, enter the vendor that the payments will be posted to.
6. In the **Bal. Source Type** field, specify if the payment will be posted to a general ledger account or to a customer or vendor account.
7. In the **Bal. Source No.** field, specify the account that the payment will be posted to, depending on your selection in the **Bal. Source Type** field.
   
    Note
   
   Do not use the **Debit Acc. No.** and **Credit Acc. No.** fields in connection with payment reconciliation. They are used for incoming documents only. For more information, see [Use OCR to Turn PDF and Image Files into Electronic Documents](across-how-use-ocr-pdf-images-files).
8. Repeat steps 3 through 7 for all text on payments that you want to map to accounts for direct posting without application.

Next time you import a bank statement file or choose the **Apply Automatically** action on the **Payment Reconciliation Journal** page, journal lines for the payments that contain the specified mapping text will contain the mapped accounts in the **Account Type** and **Account No.** fields. The **Match Confidence** field will contain **High - Text-to-Account Mapping**. This is on the condition that the automatic application function can only provide a match confidence of **Low** or **Medium**.

Example: Text-to-Account mapping for bank fees
----------------------------------------------

To always post expenses that are related to fees from a specific bank, MyBank, to the general ledger account for bank charges and fees (account 60400), fill a line on the **Text-to-Account Mapping** page as follows.

Expand table

| Mapping Text | Debit Acc. No. | Credit Acc. No. | Bal. Source Type | Bal. Source No. |
| --- | --- | --- | --- | --- |
| MyBank | BLANK | 60400 | G/L Account | BLANK |

See also
--------

[Managing Receivables](receivables-manage-receivables)  
[Sales](sales-manage-sales)  
[Set Up the Envestnet Yodlee Bank Feeds Service](bank-how-setup-bank-statement-service)  
[Customizing Business Central Using Extensions](ui-extensions)  
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

[English (United States)](/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation)[California Consumer Privacy Act (CCPA) Opt-Out IconYour Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

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

[English (United States)](/en-us/locale?target=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fdynamics365%2Fbusiness-central%2Freceivables-how-map-text-recurring-payments-accounts-auto-reconcilliation)[California Consumer Privacy Act (CCPA) Opt-Out IconYour Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)Theme

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
