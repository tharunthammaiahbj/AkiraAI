What Is Artificial Intelligence (AI)? | Google CloudPage Contents

* [Topics](https://cloud.google.com/discover)
* What is Artificial Intelligence?

What is Artificial Intelligence (AI)?
=====================================

Artificial intelligence (AI) is a set of technologies that enable computers to perform a variety of advanced functions, including the ability to [see](https://cloud.google.com/vision#section-8), understand and [translate spoken and written language](https://cloud.google.com/speech-to-text), [analyze data](https://cloud.google.com/vertex-ai), make recommendations, and more.

AI is the backbone of innovation in modern computing, unlocking value for individuals and businesses. For example, [optical character recognition (OCR](https://cloud.google.com/use-cases/ocr)) uses AI to extract text and data from images and documents, turns unstructured content into business-ready structured data, and unlocks valuable insights.

Ready to get started? New customers get $300 in free credits to spend on Google Cloud.

[Get started for free](https://console.cloud.google.com/freetrial?redirectPath=/vertex-ai/)[Stay informed](https://cloud.google.com/newsletter/?)[![](https://www.gstatic.com/bricks/image/hEiNlSg0glwjqC7DfpS3j9qNjwBfDv9sps8_lH6Bwi_PZcAKzOvQwae08_oprztaFUQDRBbhzcPE.png)22:54](https://www.youtube.com/watch?v=cZaNf2rA30k)Introduction to generative AI 

Artificial intelligence defined
===============================

Artificial intelligence is a field of science concerned with building computers and machines that can reason, learn, and act in such a way that would normally require human intelligence or that involves data whose scale exceeds what humans can analyze.

AI is a broad field that encompasses many different disciplines, including computer science, data analytics and statistics, hardware and software engineering, linguistics, neuroscience, and even philosophy and psychology.

On an operational level for business use, AI is a set of technologies that are based primarily on machine learning and deep learning, used for data analytics, predictions and forecasting, object categorization, natural language processing, recommendations, intelligent data retrieval, and more.

How does AI work?
-----------------

While the specifics vary across different AI techniques, the core principle revolves around data. AI systems learn and improve through exposure to vast amounts of data, identifying patterns and relationships that humans may miss.

This learning process often involves algorithms, which are sets of rules or instructions that guide the AI's analysis and decision-making. In machine learning, a popular subset of AI, algorithms are trained on labeled or unlabeled data to make predictions or categorize information.

[Deep learning](https://cloud.google.com/discover/what-is-deep-learning), a further specialization, utilizes artificial neural networks with multiple layers to process information, mimicking the structure and function of the human brain. Through continuous learning and adaptation, AI systems become increasingly adept at performing specific tasks, from recognizing images to translating languages and beyond.

Want to learn how to get started with AI? Take the free beginner's [introduction to generative AI](https://www.cloudskillsboost.google/paths/118??utm_source=cgc-site&utm_medium=et&utm_campaign=FY24-Q2-global-website-skillsboost&utm_content=developers&utm_term=-).

Types of artificial intelligence
--------------------------------

Artificial intelligence can be organized in several ways, depending on stages of development or actions being performed.

For instance, four stages of AI development are commonly recognized.

1. **Reactive machines:** Limited AI that only reacts to different kinds of stimuli based on preprogrammed rules. Does not use memory and thus cannot learn with new data. IBM’s Deep Blue that beat chess champion Garry Kasparov in 1997 was an example of a reactive machine.
2. **Limited memory:** Most modern AI is considered to be limited memory. It can use memory to improve over time by being trained with new data, typically through an artificial neural network or other training model. Deep learning, a subset of machine learning, is considered limited memory artificial intelligence.
3. **Theory of mind:** Theory of mind AI does not currently exist, but research is ongoing into its possibilities. It describes AI that can emulate the human mind and has decision-making capabilities equal to that of a human, including recognizing and remembering emotions and reacting in social situations as a human would.
4. **Self aware:** A step above theory of mind AI, self-aware AI describes a mythical machine that is aware of its own existence and has the intellectual and emotional capabilities of a human. Like theory of mind AI, self-aware AI does not currently exist.

A more useful way of broadly categorizing types of artificial intelligence is by what the machine can do. All of what we currently call artificial intelligence is considered artificial “narrow” intelligence, in that it can perform only narrow sets of actions based on its programming and training. For instance, an AI algorithm that is used for object classification won’t be able to perform natural language processing. Google Search is a form of narrow AI, as is predictive analytics, or virtual assistants.

Artificial general intelligence (AGI) would be the ability for a machine to “sense, think, and act” just like a human. AGI does not currently exist. The next level would be artificial superintelligence (ASI), in which the machine would be able to function in all ways superior to a human.

Artificial intelligence training models
---------------------------------------

When businesses talk about AI, they often talk about “training data.” But what does that mean? Remember that limited-memory artificial intelligence is AI that improves over time by being trained with new data. Machine learning is a [subset of artificial intelligence](https://cloud.google.com/learn/artificial-intelligence-vs-machine-learning) that uses algorithms to train data to obtain results.

In broad strokes, three kinds of learnings models are often used in machine learning:

**Supervised learning** is a machine learning model that maps a specific input to an output using labeled training data (structured data). In simple terms, to train the algorithm to recognize pictures of cats, feed it pictures labeled as cats.

**Unsupervised learning** is a machine learning model that learns patterns based on unlabeled data (unstructured data). Unlike supervised learning, the end result is not known ahead of time. Rather, the algorithm learns from the data, categorizing it into groups based on attributes. For instance, unsupervised learning is good at pattern matching and descriptive modeling.

In addition to supervised and unsupervised learning, a mixed approach called semi-supervised learning is often employed, where only some of the data is labeled. In semi-supervised learning, an end result is known, but the algorithm must figure out how to organize and structure the data to achieve the desired results.

**Reinforcement learning** is a machine learning model that can be broadly described as “learn by doing.” An “agent” learns to perform a defined task by trial and error (a feedback loop) until its performance is within a desirable range. The agent receives positive reinforcement when it performs the task well and negative reinforcement when it performs poorly. An example of reinforcement learning would be teaching a robotic hand to pick up a ball.

Common types of artificial neural networks
------------------------------------------

A common type of training model in AI is an artificial neural network, a model loosely based on the human brain.

A neural network is a system of artificial neurons—sometimes called perceptrons—that are computational nodes used to classify and analyze data. The data is fed into the first layer of a neural network, with each perceptron making a decision, then passing that information onto multiple nodes in the next layer. Training models with more than three layers are referred to as “deep neural networks” or “deep learning.” Some modern neural networks have hundreds or thousands of layers. The output of the final perceptrons accomplish the task set to the neural network, such as classify an object or find patterns in data.

Some of the most common types of artificial neural networks you may encounter include:

**Feedforward neural networks (FF)** are one of the oldest forms of neural networks, with data flowing one way through layers of artificial neurons until the output is achieved. In modern days, most feedforward neural networks are considered “deep feedforward”with several layers (and more than one “hidden” layer). Feedforward neural networks are typically paired with an error-correction algorithm called “backpropagation” that, in simple terms, starts with the result of the neural network and works back through to the beginning, finding errors to improve the accuracy of the neural network. Many simple but powerful neural networks are deep feedforward.

**Recurrent neural networks (RNN)** differ from feedforward neural networks in that they typically use time series data or data that involves sequences. Unlike feedforward neural networks, which use weights in each node of the network, recurrent neural networks have “memory” of what happened in the previous layer as contingent to the output of the current layer. For instance, when performing natural language processing, RNNs can “keep in mind” other words used in a sentence. RNNs are often used for speech recognition, translation, and to caption images.

**Long/short term memory (LSTM)** is an advanced form of RNN that can use memory to “remember” what happened in previous layers. The difference between RNNs and LSTM is that LSTM can remember what happened several layers ago, through the use of “memory cells.” LSTM is often used in speech recognition and making predictions.

**Convolutional neural networks (CNN)** includesome of the most common neural networks in modern artificial intelligence. Most often used in image recognition, CNNs use several distinct layers (a convolutional layer, then a pooling layer) that filter different parts of an image before putting it back together (in the fully connected layer). The earlier convolutional layers may look for simple features of an image, such as colors and edges, before looking for more complex features in additional layers.

**Generative adversarial networks (GAN)** involve two neural networks competing against each other in a game that ultimately improves the accuracy of the output. One network (the generator) creates examples that the other network (the discriminator) attempts to prove true or false. GANs have been used to create realistic images and even make art.

### Benefits of AI

### Automation

AI can automate workflows and processes or work independently and autonomously from a human team. For example, AI can help automate aspects of cybersecurity by continuously monitoring and analyzing network traffic. Similarly, a smart factory may have dozens of different kinds of AI in use, such as robots using computer vision to navigate the factory floor or to inspect products for defects, create digital twins, or use real-time analytics to measure efficiency and output.

### Reduce human error

AI can eliminate manual errors in data processing, analytics, assembly in manufacturing, and other tasks through automation and algorithms that follow the same processes every single time.

### Eliminate repetitive tasks

AI can be used to perform repetitive tasks, freeing human capital to work on higher impact problems. AI can be used to automate processes, like verifying documents, transcribing phone calls, or answering simple customer questions like “what time do you close?” Robots are often used to perform “dull, dirty, or dangerous” tasks in the place of a human.

### Fast and accurate

AI can process more information more quickly than a human, finding patterns and discovering relationships in data that a human may miss.

### Infinite availability

AI is not limited by time of day, the need for breaks, or other human encumbrances. When running in the cloud, AI and machine learning can be “always on,” continuously working on its assigned tasks.

### Accelerated research and development

The ability to analyze vast amounts of data quickly can lead to accelerated breakthroughs in research and development. For instance, AI has been used in predictive modeling of potential new pharmaceutical treatments, or to quantify the human genome.

### Solve your business challenges with Google Cloud

New customers get $300 in free credits to spend on Google Cloud.[Get started](https://console.cloud.google.com/freetrial)Sign up for Google Cloud newsletters with product updates, event information, special offers, and more.[Stay informed](https://cloud.google.com/newsletter)
### Applications and use cases for artificial intelligence

### Speech recognition

Automatically convert spoken speech into written text.

### Image recognition

Identify and categorize various aspects of an image.

### Translation

Translate written or spoken words from one language into another.

### Predictive modeling

Mine data to forecast specific outcomes with high degrees of granularity.

### Data analytics

Find patterns and relationships in data for business intelligence.

### Cybersecurity

Autonomously scan networks for cyber attacks and threats.

Related products and services
-----------------------------

Google offers a number of sophisticated artificial intelligence products, solutions, and applications on a trusted cloud platform that enables businesses to easily build and implement AI algorithms and models.

By using products like [Vertex AI](https://cloud.google.com/ai-hub), [CCAI](https://cloud.google.com/solutions/contact-center), [DocAI](https://cloud.google.com/document-ai), or [AI APIs](https://cloud.google.com/ai/apis), organizations can make sense of all the data they’re producing, collecting, or otherwise analyzing, no matter what format it’s in, to make actionable business decisions.

* [![](https://www.gstatic.com/bricks/image/rc7m6af1wpQO_v5GlttqQ_nbbC4jLY0EEN4aVof8WsJLmVyWrtPTHYb5XSm4sJY_142oDc1IsIs.png)Explore all AI products and solutionsInnovative AI and machine learning products, solutions, and services powered by Google’s research and technology.](https://cloud.google.com/products/ai)
* [![](https://www.gstatic.com/bricks/image/me6u4lx8TR7uZxMdl7YC5WlyZC0P2y0LzMAYP3mICUJJz4x7eZ0AXWaXc3n9EPNxfvCoFc6Y3mmmGg.png)Vertex AIBuild, deploy, and scale ML models faster, with pretrained and custom tooling within a unified artificial intelligence platform.](https://cloud.google.com/vertex-ai)
* [![](https://www.gstatic.com/bricks/image/me6u4lx8TR7uZxMdl7YC5WlyZC0P2y0LzMAYP3mICUJJz4x7eZ0AXWaXc3n9EPNxfvCoFc6Y3mmmGg.png)Vertex AI Studio Tool for rapidly prototyping and testing generative AI models.](https://cloud.google.com/generative-ai-studio)
* [![](https://www.gstatic.com/bricks/image/cvl2iROAmlw6oqzO5Xsw4sU_2iAlg6UYuNjpZZir9FDNMGEsfAutoqHyFAy4l_mbEb0d-UY5TC67.png)Document AIAutomate data capture at scale to reduce document processing costs.](https://cloud.google.com/document-ai)
* [![](https://www.gstatic.com/bricks/image/A7NDzHSjhN7otiP1pd3-d37aQgC0c07khXBeOO5ILx_PO_I8690EcpLH5Uun0QwNVy7khMrqil8.png)AlloyDB AIBuild a wide range of generative AI applications using familiar PostgreSQL and run models in Vertex AI.](https://cloud.google.com/alloydb/ai)
* [Solution
  
  Contact Center AIDeliver exceptional customer service and increase operational efficiency using artificial intelligence. Enable your virtual agent to converse naturally with customers and expertly assist human agents on complex cases.](https://cloud.google.com/solutions/contact-center)
* [Solution
  
  Dialogflow CXCreate conversational experiences across devices and platforms.](https://cloud.google.com/dialogflow)
#### Take the next step

Start building on Google Cloud with $300 in free credits and 20+ always free products.

[Get started for free](https://console.cloud.google.com/freetrial/)

* ##### Need help getting started?
  
  [Contact sales](https://cloud.google.com/contact/)
* ##### Work with a trusted partner
  
  [Find a partner](https://cloud.google.com/find-a-partner/)
* ##### Want to hear from us?
  
  [Join the monthly newsletter](https://cloud.google.com/newsletter/?)
menu[![](https://www.gstatic.com/devrel-devsite/prod/v0e0f589edd85502a40d78d7d0825db8ea5ef3b99ab4070381ee86977c9168730/cloud/images/cloud-logo.svg)](https://cloud.google.com/)[Overview](https://cloud.google.com/why-google-cloud/)[Solutions](https://cloud.google.com/solutions/)[Products](https://cloud.google.com/products/)[Pricing](https://cloud.google.com/pricing/)[Resources](https://cloud.google.com/start/)[Docs](https://cloud.google.com/docs/)[Support](https://cloud.google.com/support-hub/)[Contact Us](https://cloud.google.com/contact/)*search\_spark**send\_spark*

[Docs](https://cloud.google.com/docs/)[Support](https://cloud.google.com/support-hub/)*language*‪English‬

* ‪English‬
* ‪Deutsch‬
* ‪Español‬
* ‪Español (Latinoamérica)‬
* ‪Français‬
* ‪Indonesia‬
* ‪Italiano‬
* ‪Português (Brasil)‬
* ‪简体中文‬
* ‪繁體中文‬
* ‪日本語‬
* ‪한국어‬
[Console](https://console.cloud.google.com/)[Sign in](https://cloud.google.com/_d/signin?continue=https%3A%2F%2Fcloud.google.com%2Flearn%2Fwhat-is-artificial-intelligence&prompt=select_account)[Start free](https://console.cloud.google.com/freetrial)[Start free](https://console.cloud.google.com/freetrial)[Contact Us](https://cloud.google.com/contact/)close

* Accelerate your digital transformation
* Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
* [Learn more](https://cloud.google.com/transform/)

* Key benefits
* [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud/)
* [AI and MLGet enterprise-ready AI.](https://cloud.google.com/ai/)
* [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud/)
* [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure/)

* [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud/)
* [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure/)
* [SecurityProtect your users, data, and apps.](https://cloud.google.com/security/)
* [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com/)

* Reports and insights
* [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights/)
* [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports/)
* [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers/)
* [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers/)
close

* [Industry Solutions](#)
* [Application Modernization](#)
* [Artificial Intelligence](#)
* [APIs and Applications](#)
* [Data Analytics](#)
* [Databases](#)
* [Infrastructure Modernization](#)
* [Productivity and Collaboration](#)
* [Security](#)
* [Startups and SMB](#)

[See all solutions](https://cloud.google.com/solutions/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)

* [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail/)

* [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg/)

* [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services/)

* [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences/)

* [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment/)

* [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications/)

* [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games/)

* [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing/)

* [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics/)

* [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/solutions/government/)

* [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/solutions/education/)

* Not seeing what you're looking for?
* [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationAssess, plan, implement, and measure software practices and capabilities to modernize and simplify your organization’s business application portfolios.](https://cloud.google.com/solutions/camp/)

* [CAMPProgram that uses DORA to improve your software delivery capabilities.](https://cloud.google.com/solutions/camp/)

* [Modernize Traditional ApplicationsAnalyze, categorize, and get started with cloud migration on traditional workloads.](https://cloud.google.com/solutions/modernize-traditional-applications/)

* [Migrate from PaaS: Cloud Foundry, OpenshiftTools for moving your existing containers into Google's managed container services.](https://cloud.google.com/solutions/migrate-from-paas/)

* [Migrate from MainframeAutomated tools and prescriptive guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization/)

* [Modernize Software DeliverySoftware supply chain best practices - innerloop productivity, CI/CD and S3C.](https://cloud.google.com/solutions/software-delivery/)

* [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops/)

* [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre/)

* [Day 2 Operations for GKETools and guidance for effective GKE management and monitoring.](https://cloud.google.com/solutions/app-modernization/day-2-operations-for-gke/)

* [FinOps and Optimization of GKEBest practices for running reliable, performant, and cost effective applications on GKE.](https://cloud.google.com/solutions/finops-optimize-gke/)

* [Run Applications at the EdgeGuidance for localized and low latency apps on Google’s hardware agnostic edge solution.](https://cloud.google.com/solutions/modernize-with-edge/)

* [Architect for MulticloudManage workloads across multiple clouds with a consistent platform.](https://cloud.google.com/solutions/architect-multicloud/)

* [Go ServerlessFully managed environment for developing, deploying and scaling apps.](https://cloud.google.com/solutions/serverless/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai/)

* [Customer Engagement Suite with Google AIEnd-to-end application that combines our most advanced conversational AI.](https://cloud.google.com/solutions/customer-engagement-ai/)

* [Document AIDocument processing and data capture automated at scale.](https://cloud.google.com/document-ai/)

* [Vertex AI Search for retailGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/solutions/retail-product-discovery/)

* [Gemini for Google CloudAI assistants for application development, coding, and more.](https://cloud.google.com/products/gemini/)

* [Generative AI on Google CloudTransform content creation and discovery, research, customer service, and developer efficiency with the power of generative AI.](https://cloud.google.com/use-cases/generative-ai/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications/)

* [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis/)

* [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications/)

* [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/smart-analytics/)

* [Data MigrationMigrate and modernize with an AI-ready data platform.](https://cloud.google.com/solutions/data-migration/)

* [Data Lake ModernizationServices for building and modernizing your data lake.](https://cloud.google.com/solutions/data-lake/)

* [Stream AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics/)

* [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics/)

* [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets/)

* [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence/)

* [AI for Data AnalyticsWrite SQL, build predictive models, and visualize data with AI for data analytics.](https://cloud.google.com/use-cases/ai-data-analytics/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases/)

* [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration/)

* [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization/)

* [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games/)

* [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases/)

* [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/migrate-oracle-workloads/)

* [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases/)

* [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server/)

* [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Infrastructure ModernizationMigrate quickly with solutions for SAP, VMware, Windows, Oracle, and other workloads.](https://cloud.google.com/solutions/infrastructure-modernization/)

* [Application MigrationDiscovery and analysis tools for moving to the cloud.](https://cloud.google.com/solutions/application-migration/)

* [SAP on Google CloudCertifications for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap/)

* [High Performance ComputingCompute, storage, and networking options to support any workload.](https://cloud.google.com/solutions/hpc/)

* [Windows on Google CloudTools and partners for running Windows workloads.](https://cloud.google.com/windows/)

* [Data Center MigrationMigration solutions for VMs, apps, databases, and more.](https://cloud.google.com/solutions/data-center-migration/)

* [Active AssistAutomatic cloud resource optimization and increased security.](https://cloud.google.com/solutions/active-assist/)

* [Virtual DesktopsRemote work solutions for desktops and applications (VDI & DaaS).](https://cloud.google.com/solutions/virtual-desktops/)

* [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program/)

* [Backup and Disaster RecoveryEnsure your business continuity needs are met.](https://cloud.google.com/solutions/backup-dr/)

* [Red Hat on Google CloudGoogle and Red Hat provide an enterprise-grade platform for traditional on-prem and custom applications.](https://cloud.google.com/solutions/redhat/)

* [Cross-Cloud NetworkSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network/)

* [ObservabilityMonitor, troubleshoot, and improve app performance with end-to-end visibility.](https://cloud.google.com/solutions/observability/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)

* [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)

* [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)

* [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity/)

* [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security/)

* [Security Analytics and OperationsSolution for analyzing petabytes of security telemetry.](https://cloud.google.com/solutions/security-analytics-and-operations/)

* [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/solutions/web-app-and-api-protection/)

* [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/solutions/security-and-resilience/)

* [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code/)

* [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/solutions/software-supply-chain-security/)

* [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/solutions/security-foundation/)

* [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/solutions/secops-cybershield/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)

* [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup/)

* [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb/)

* [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas/)
close

* [Featured Products](#)
* [AI and Machine Learning](#)
* [Business Intelligence](#)
* [Compute](#)
* [Containers](#)
* [Data Analytics](#)
* [Databases](#)
* [Developer Tools](#)
* [Distributed Cloud](#)
* [Hybrid and Multicloud](#)
* [Industry Specific](#)
* [Integration Services](#)
* [Management Tools](#)
* [Maps and Geospatial](#)
* [Media Services](#)
* [Migration](#)
* [Mixed Reality](#)
* [Networking](#)
* [Operations](#)
* [Productivity and Collaboration](#)
* [Security and Identity](#)
* [Serverless](#)
* [Storage](#)
* [Web3](#)

[See all products (100+)](https://cloud.google.com/products#featured-products/)

* Featured Products

* [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/compute/)

* [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage/)

* [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryData warehouse for business agility and insights.](https://cloud.google.com/bigquery/)

* [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run/)

* [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine/)

* [![](https://www.gstatic.com/cloud/images/navigation/vertex-ai.png)Vertex AIUnified platform for ML models and generative AI.](https://cloud.google.com/vertex-ai/)

* [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker/)

* [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee/)

* [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql/)

* [![](https://www.gstatic.com/cloud/images/navigation/gemini.png)GeminiGoogle Cloud products powered by Gemini.](https://cloud.google.com/ai/gemini/)

* [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn/)

* Not seeing what you're looking for?
* [See all products (100+)](https://cloud.google.com/products#featured-products/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai/)

* [Vertex AI PlatformUnified platform for ML models and generative AI.](https://cloud.google.com/vertex-ai/)

* [Vertex AI StudioBuild, tune, and deploy foundation models on Vertex AI.](https://cloud.google.com/generative-ai-studio)

* [Vertex AI Agent BuilderBuild and deploy gen AI experiences.](https://cloud.google.com/products/agent-builder/)

* [Conversational AgentsBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/products/conversational-agents/)

* [Vertex AI SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/enterprise-search/)

* [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text/)

* [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech/)

* [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate/)

* [Document AIDocument processing and data capture automated at scale.](https://cloud.google.com/document-ai/)

* [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision/)

* [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform/)

* Not seeing what you're looking for?
* [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)

* Business Intelligence

* [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker/)

* [Looker StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/looker-studio/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute/)

* [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/compute/)

* [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine/)

* [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu/)

* [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/migrate/virtual-machines/)

* [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms/)

* [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch/)

* [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes/)

* [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal/)

* [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/)

* [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine/)

* [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run/)

* Not seeing what you're looking for?
* [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers/)

* [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine/)

* [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run/)

* [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build/)

* [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/)

* [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code/)

* [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy/)

* [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/migrate/containers/)

* [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/)

* [KnativeComponents to create Kubernetes-native cloud-based software.](https://cloud.google.com/knative/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/smart-analytics/)

* [BigQueryData warehouse for business agility and insights.](https://cloud.google.com/bigquery/)

* [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker/)

* [DataflowStreaming analytics for stream and batch processing.](https://cloud.google.com/dataflow/)

* [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub/)

* [DataprocService for running Apache Spark and Apache Hadoop clusters.](https://cloud.google.com/dataproc/)

* [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion/)

* [Cloud ComposerWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/composer/)

* [BigLakeStorage engine to query multi-format and multimodal data.](https://cloud.google.com/biglake/)

* [DataplexIntelligent data fabric for unifying data management across silos.](https://cloud.google.com/dataplex/)

* [DataformBuild, version control, and deploy SQL workflows in BigQuery.](https://cloud.google.com/dataform/)

* [Analytics HubService for securely and efficiently exchanging data analytics assets.](https://cloud.google.com/analytics-hub/)

* Not seeing what you're looking for?
* [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases/)

* [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb/)

* [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql/)

* [FirestoreCloud-native document database for building rich mobile, web, and IoT apps.](https://cloud.google.com/firestore/)

* [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner/)

* [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable/)

* [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream/)

* [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration/)

* [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal/)

* [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools/)

* [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/)

* [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code/)

* [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build/)

* [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy/)

* [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs/)

* [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk/)

* [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/)

* [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/)

* [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/)

* [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations/)

* [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist/)

* Not seeing what you're looking for?
* [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud/)

* [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-edge/)

* [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-hosted/)

* Hybrid and Multicloud

* [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine/)

* [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee/)

* [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/migrate/containers/)

* [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build/)

* [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability/)

* [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh/)

* [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud/)

* Industry Specific

* [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai/)

* [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api/)

* [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect/)

* [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation/)

* [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric/)

* [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights/)

* [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/spectrum-access-system/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services/)

* [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration/)

* [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows/)

* [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee/)

* [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/)

* [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/)

* [DataprocService for running Apache Spark and Apache Hadoop clusters.](https://cloud.google.com/dataproc/)

* [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion/)

* [Cloud ComposerWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/composer/)

* [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub/)

* [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management/)

* [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/)

* [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console/)

* [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/)

* [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/iam/)

* [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis/)

* [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/private-catalog/)

* [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management/)

* [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability/)

* [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint/)

* [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview/)

* [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist/)

* Not seeing what you're looking for?
* [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial/)

* [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine/)

* [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com/)

* Media Services

* [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn/)

* [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs/)

* [OpenCueOpen source render manager for visual effects and animation.](https://cloud.google.com/opencue/)

* [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs/)

* [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration/)

* [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs/)

* [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration/)

* [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/migrate/virtual-machines/)

* [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/foundation-toolkit/)

* [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration/)

* [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/migrate/containers/)

* [BigQuery Data Transfer ServiceData import service for scheduling and moving data into BigQuery.](https://cloud.google.com/bigquery-transfer/docs/introduction/)

* [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program/)

* [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/)

* [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service/)

* [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine/)

* Mixed Reality

* [Immersive Stream for XRHosts, renders, and streams 3D and XR experiences.](https://cloud.google.com/immersive-stream/xr/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking/)

* [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/armor/)

* [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn/)

* [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns/)

* [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing/)

* [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat/)

* [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity/)

* [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center/)

* [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center/)

* [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers/)

* [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc/)

* [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect/)

* Not seeing what you're looking for?
* [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations/)

* [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging/)

* [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring/)

* [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/)

* [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus/)

* [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/)

* [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs/)

* [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)

* Productivity and Collaboration

* [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)

* [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation/)

* [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)

* [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)

* [Gemini for WorkspaceEmbeds generative AI across Google Workspace apps.](https://workspace.google.com/solutions/ai/)

* [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity/)

* [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://cloud.google.com/chrome-enterprise/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity/)

* [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam/)

* [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection/)

* [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense/)

* [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence/)

* [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center/)

* [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management/)

* [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services/)

* [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://chromeenterprise.google/products/chrome-enterprise-premium/)

* [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads/)

* [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations/)

* [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services/)

* Not seeing what you're looking for?
* [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless/)

* [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run/)

* [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions/)

* [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine/)

* [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows/)

* [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage/)

* [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage/)

* [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage/)

* [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore/)

* [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk/)

* [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage/)

* [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/local-ssd/)

* [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service/)

* [ParallelstoreHigh performance, managed parallel file service.](https://cloud.google.com/parallelstore/)

* [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes/)

* [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery/)

* [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3/)

* [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine/)

* [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc/)
close

* Save money with our transparent approach to pricing
* Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
* [Request a quote](https://cloud.google.com/contact/?direct=true)

* Pricing overview and tools
* [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing/)
* [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator/)
* [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free/)

* [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization/)
* [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management/)

* Product-specific Pricing
* [Compute Engine](https://cloud.google.com/compute/all-pricing/)
* [Cloud SQL](https://cloud.google.com/sql/pricing/)
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing/)
* [Cloud Storage](https://cloud.google.com/storage/pricing/)
* [BigQuery](https://cloud.google.com/bigquery/pricing/)
* [See full price list with 100+ products](https://cloud.google.com/pricing/list/)
close

* Learn & build
* [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free/)
* [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator/)
* [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)
* [BlogRead our latest product news and stories.](https://cloud.google.com/blog)

* [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn/)
* [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification/)
* [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover/)
* [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture/)

* Connect
* [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus/)
* [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers/)
* [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events/)
* [Google Cloud CommunityAsk questions, find answers, and connect.](https://cloud.google.com/communities/)

* Consulting and Partners
* [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting/)
* [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace/)
* [Google Cloud partnersExplore benefits of working with a partner.](https://cloud.google.com/partners/)
* [Become a partnerJoin the Partner Advantage program.](https://partners.cloud.google.com/)
close[![](https://www.gstatic.com/devrel-devsite/prod/v0e0f589edd85502a40d78d7d0825db8ea5ef3b99ab4070381ee86977c9168730/cloud/images/cloud-logo.svg)](https://cloud.google.com/)

* [Overview](https://cloud.google.com/why-google-cloud/)
  + arrow\_forward
* [Solutions](https://cloud.google.com/solutions/)
  + arrow\_forward
* [Products](https://cloud.google.com/products/)
  + arrow\_forward
* [Pricing](https://cloud.google.com/pricing/)
  + arrow\_forward
* [Resources](https://cloud.google.com/start/)
  + arrow\_forward
* [Docs](https://cloud.google.com/docs/)
* [Support](https://cloud.google.com/support-hub/)
* [Console](https://console.cloud.google.com/)

* Accelerate your digital transformation
* [Learn more](https://cloud.google.com/transform/)
* Key benefits
* [Why Google Cloud](https://cloud.google.com/why-google-cloud/)
* [AI and ML](https://cloud.google.com/ai/)
* [Multicloud](https://cloud.google.com/multicloud/)
* [Global infrastructure](https://cloud.google.com/infrastructure/)
* [Data Cloud](https://cloud.google.com/data-cloud/)
* [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure/)
* [Security](https://cloud.google.com/security/)
* [Productivity and collaboration](https://workspace.google.com/)
* Reports and insights
* [Executive insights](https://cloud.google.com/executive-insights/)
* [Analyst reports](https://cloud.google.com/analyst-reports/)
* [Whitepapers](https://cloud.google.com/whitepapers/)
* [Customer stories](https://cloud.google.com/customers/)

* [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
* [Retail](https://cloud.google.com/solutions/retail/)
* [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg/)
* [Financial Services](https://cloud.google.com/solutions/financial-services/)
* [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences/)
* [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment/)
* [Telecommunications](https://cloud.google.com/solutions/telecommunications/)
* [Games](https://cloud.google.com/solutions/games/)
* [Manufacturing](https://cloud.google.com/solutions/manufacturing/)
* [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics/)
* [Government](https://cloud.google.com/solutions/government/)
* [Education](https://cloud.google.com/solutions/education/)
* [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
* [See all solutions](https://cloud.google.com/solutions/)
* [Application Modernization](https://cloud.google.com/solutions/camp/)
* [CAMP](https://cloud.google.com/solutions/camp/)
* [Modernize Traditional Applications](https://cloud.google.com/solutions/modernize-traditional-applications/)
* [Migrate from PaaS: Cloud Foundry, Openshift](https://cloud.google.com/solutions/migrate-from-paas/)
* [Migrate from Mainframe](https://cloud.google.com/solutions/mainframe-modernization/)
* [Modernize Software Delivery](https://cloud.google.com/solutions/software-delivery/)
* [DevOps Best Practices](https://cloud.google.com/devops/)
* [SRE Principles](https://cloud.google.com/sre/)
* [Day 2 Operations for GKE](https://cloud.google.com/solutions/app-modernization/day-2-operations-for-gke/)
* [FinOps and Optimization of GKE](https://cloud.google.com/solutions/finops-optimize-gke/)
* [Run Applications at the Edge](https://cloud.google.com/solutions/modernize-with-edge/)
* [Architect for Multicloud](https://cloud.google.com/solutions/architect-multicloud/)
* [Go Serverless](https://cloud.google.com/solutions/serverless/)
* [Artificial Intelligence](https://cloud.google.com/solutions/ai/)
* [Customer Engagement Suite with Google AI](https://cloud.google.com/solutions/customer-engagement-ai/)
* [Document AI](https://cloud.google.com/document-ai/)
* [Vertex AI Search for retail](https://cloud.google.com/solutions/retail-product-discovery/)
* [Gemini for Google Cloud](https://cloud.google.com/products/gemini/)
* [Generative AI on Google Cloud](https://cloud.google.com/use-cases/generative-ai/)
* [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications/)
* [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis/)
* [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications/)
* [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix/)
* [Data Analytics](https://cloud.google.com/solutions/smart-analytics/)
* [Data Migration](https://cloud.google.com/solutions/data-migration/)
* [Data Lake Modernization](https://cloud.google.com/solutions/data-lake/)
* [Stream Analytics](https://cloud.google.com/solutions/stream-analytics/)
* [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics/)
* [Datasets](https://cloud.google.com/datasets/)
* [Business Intelligence](https://cloud.google.com/solutions/business-intelligence/)
* [AI for Data Analytics](https://cloud.google.com/use-cases/ai-data-analytics/)
* [Databases](https://cloud.google.com/solutions/databases/)
* [Database Migration](https://cloud.google.com/solutions/database-migration/)
* [Database Modernization](https://cloud.google.com/solutions/database-modernization/)
* [Databases for Games](https://cloud.google.com/solutions/databases/games/)
* [Google Cloud Databases](https://cloud.google.com/products/databases/)
* [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/migrate-oracle-workloads/)
* [Open Source Databases](https://cloud.google.com/solutions/open-source-databases/)
* [SQL Server on Google Cloud](https://cloud.google.com/sql-server/)
* [Gemini for Databases](https://cloud.google.com/products/gemini/databases/)
* [Infrastructure Modernization](https://cloud.google.com/solutions/infrastructure-modernization/)
* [Application Migration](https://cloud.google.com/solutions/application-migration/)
* [SAP on Google Cloud](https://cloud.google.com/solutions/sap/)
* [High Performance Computing](https://cloud.google.com/solutions/hpc/)
* [Windows on Google Cloud](https://cloud.google.com/windows/)
* [Data Center Migration](https://cloud.google.com/solutions/data-center-migration/)
* [Active Assist](https://cloud.google.com/solutions/active-assist/)
* [Virtual Desktops](https://cloud.google.com/solutions/virtual-desktops/)
* [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program/)
* [Backup and Disaster Recovery](https://cloud.google.com/solutions/backup-dr/)
* [Red Hat on Google Cloud](https://cloud.google.com/solutions/redhat/)
* [Cross-Cloud Network](https://cloud.google.com/solutions/cross-cloud-network/)
* [Observability](https://cloud.google.com/solutions/observability/)
* [Productivity and Collaboration](https://workspace.google.com/enterprise/)
* [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
* [Google Workspace Essentials](https://workspace.google.com/essentials/)
* [Cloud Identity](https://cloud.google.com/identity/)
* [Chrome Enterprise](https://chromeenterprise.google/)
* [Security](https://cloud.google.com/solutions/security/)
* [Security Analytics and Operations](https://cloud.google.com/solutions/security-analytics-and-operations/)
* [Web App and API Protection](https://cloud.google.com/solutions/web-app-and-api-protection/)
* [Security and Resilience Framework](https://cloud.google.com/solutions/security-and-resilience/)
* [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code/)
* [Software Supply Chain Security](https://cloud.google.com/solutions/software-supply-chain-security/)
* [Security Foundation](https://cloud.google.com/solutions/security-foundation/)
* [Google Cloud Cybershield™](https://cloud.google.com/solutions/secops-cybershield/)
* [Startups and SMB](https://cloud.google.com/solutions#section-13)
* [Startup Program](https://cloud.google.com/startup/)
* [Small and Medium Business](https://cloud.google.com/solutions/smb/)
* [Software as a Service](https://cloud.google.com/saas/)

* Featured Products
* [Compute Engine](https://cloud.google.com/compute/)
* [Cloud Storage](https://cloud.google.com/storage/)
* [BigQuery](https://cloud.google.com/bigquery/)
* [Cloud Run](https://cloud.google.com/run/)
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/)
* [Vertex AI](https://cloud.google.com/vertex-ai/)
* [Looker](https://cloud.google.com/looker/)
* [Apigee API Management](https://cloud.google.com/apigee/)
* [Cloud SQL](https://cloud.google.com/sql/)
* [Gemini](https://cloud.google.com/ai/gemini/)
* [Cloud CDN](https://cloud.google.com/cdn/)
* [See all products (100+)](https://cloud.google.com/products#featured-products/)
* [AI and Machine Learning](https://cloud.google.com/products/ai/)
* [Vertex AI Platform](https://cloud.google.com/vertex-ai/)
* [Vertex AI Studio](https://cloud.google.com/generative-ai-studio)
* [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder/)
* [Conversational Agents](https://cloud.google.com/products/conversational-agents/)
* [Vertex AI Search](https://cloud.google.com/enterprise-search/)
* [Speech-to-Text](https://cloud.google.com/speech-to-text/)
* [Text-to-Speech](https://cloud.google.com/text-to-speech/)
* [Translation AI](https://cloud.google.com/translate/)
* [Document AI](https://cloud.google.com/document-ai/)
* [Vision AI](https://cloud.google.com/vision/)
* [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform/)
* [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
* Business Intelligence
* [Looker](https://cloud.google.com/looker/)
* [Looker Studio](https://cloud.google.com/looker-studio/)
* [Compute](https://cloud.google.com/products/compute/)
* [Compute Engine](https://cloud.google.com/compute/)
* [App Engine](https://cloud.google.com/appengine/)
* [Cloud GPUs](https://cloud.google.com/gpu/)
* [Migrate to Virtual Machines](https://cloud.google.com/migrate/virtual-machines/)
* [Spot VMs](https://cloud.google.com/spot-vms/)
* [Batch](https://cloud.google.com/batch/)
* [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes/)
* [Bare Metal](https://cloud.google.com/bare-metal/)
* [Recommender](https://cloud.google.com/recommender/)
* [VMware Engine](https://cloud.google.com/vmware-engine/)
* [Cloud Run](https://cloud.google.com/run/)
* [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
* [Containers](https://cloud.google.com/containers/)
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/)
* [Cloud Run](https://cloud.google.com/run/)
* [Cloud Build](https://cloud.google.com/build/)
* [Artifact Registry](https://cloud.google.com/artifact-registry/)
* [Cloud Code](https://cloud.google.com/code/)
* [Cloud Deploy](https://cloud.google.com/deploy/)
* [Migrate to Containers](https://cloud.google.com/migrate/containers/)
* [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/)
* [Knative](https://cloud.google.com/knative/)
* [Data Analytics](https://cloud.google.com/solutions/smart-analytics/)
* [BigQuery](https://cloud.google.com/bigquery/)
* [Looker](https://cloud.google.com/looker/)
* [Dataflow](https://cloud.google.com/dataflow/)
* [Pub/Sub](https://cloud.google.com/pubsub/)
* [Dataproc](https://cloud.google.com/dataproc/)
* [Cloud Data Fusion](https://cloud.google.com/data-fusion/)
* [Cloud Composer](https://cloud.google.com/composer/)
* [BigLake](https://cloud.google.com/biglake/)
* [Dataplex](https://cloud.google.com/dataplex/)
* [Dataform](https://cloud.google.com/dataform/)
* [Analytics Hub](https://cloud.google.com/analytics-hub/)
* [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
* [Databases](https://cloud.google.com/products/databases/)
* [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb/)
* [Cloud SQL](https://cloud.google.com/sql/)
* [Firestore](https://cloud.google.com/firestore/)
* [Spanner](https://cloud.google.com/spanner/)
* [Bigtable](https://cloud.google.com/bigtable/)
* [Datastream](https://cloud.google.com/datastream/)
* [Database Migration Service](https://cloud.google.com/database-migration/)
* [Bare Metal Solution](https://cloud.google.com/bare-metal/)
* [Memorystore](https://cloud.google.com/memorystore/)
* [Developer Tools](https://cloud.google.com/products/tools/)
* [Artifact Registry](https://cloud.google.com/artifact-registry/)
* [Cloud Code](https://cloud.google.com/code/)
* [Cloud Build](https://cloud.google.com/build/)
* [Cloud Deploy](https://cloud.google.com/deploy/)
* [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs/)
* [Cloud SDK](https://cloud.google.com/sdk/)
* [Cloud Scheduler](https://cloud.google.com/scheduler/)
* [Cloud Source Repositories](https://cloud.google.com/source-repositories/)
* [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/)
* [Cloud Workstations](https://cloud.google.com/workstations/)
* [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist/)
* [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
* [Distributed Cloud](https://cloud.google.com/distributed-cloud/)
* [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-edge/)
* [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-hosted/)
* Hybrid and Multicloud
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/)
* [Apigee API Management](https://cloud.google.com/apigee/)
* [Migrate to Containers](https://cloud.google.com/migrate/containers/)
* [Cloud Build](https://cloud.google.com/build/)
* [Observability](https://cloud.google.com/products/observability/)
* [Cloud Service Mesh](https://cloud.google.com/products/service-mesh/)
* [Google Distributed Cloud](https://cloud.google.com/distributed-cloud/)
* Industry Specific
* [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai/)
* [Cloud Healthcare API](https://cloud.google.com/healthcare-api/)
* [Device Connect for Fitbit](https://cloud.google.com/device-connect/)
* [Telecom Network Automation](https://cloud.google.com/telecom-network-automation/)
* [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric/)
* [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights/)
* [Spectrum Access System (SAS)](https://cloud.google.com/spectrum-access-system/)
* [Integration Services](https://cloud.google.com/integration-services/)
* [Application Integration](https://cloud.google.com/application-integration/)
* [Workflows](https://cloud.google.com/workflows/)
* [Apigee API Management](https://cloud.google.com/apigee/)
* [Cloud Tasks](https://cloud.google.com/tasks/)
* [Cloud Scheduler](https://cloud.google.com/scheduler/)
* [Dataproc](https://cloud.google.com/dataproc/)
* [Cloud Data Fusion](https://cloud.google.com/data-fusion/)
* [Cloud Composer](https://cloud.google.com/composer/)
* [Pub/Sub](https://cloud.google.com/pubsub/)
* [Eventarc](https://cloud.google.com/eventarc/docs/)
* [Management Tools](https://cloud.google.com/products/management/)
* [Cloud Shell](https://cloud.google.com/shell/)
* [Cloud console](https://cloud.google.com/cloud-console/)
* [Cloud Endpoints](https://cloud.google.com/endpoints/)
* [Cloud IAM](https://cloud.google.com/iam/)
* [Cloud APIs](https://cloud.google.com/apis/)
* [Service Catalog](https://cloud.google.com/private-catalog/)
* [Cost Management](https://cloud.google.com/cost-management/)
* [Observability](https://cloud.google.com/products/observability/)
* [Carbon Footprint](https://cloud.google.com/carbon-footprint/)
* [Config Connector](https://cloud.google.com/config-connector/docs/overview/)
* [Active Assist](https://cloud.google.com/solutions/active-assist/)
* [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
* [Maps and Geospatial](https://cloud.google.com/solutions/geospatial/)
* [Earth Engine](https://cloud.google.com/earth-engine/)
* [Google Maps Platform](https://mapsplatform.google.com/)
* Media Services
* [Cloud CDN](https://cloud.google.com/cdn/)
* [Live Stream API](https://cloud.google.com/livestream/docs/)
* [OpenCue](https://cloud.google.com/opencue/)
* [Transcoder API](https://cloud.google.com/transcoder/docs/)
* [Video Stitcher API](https://cloud.google.com/video-stitcher/)
* [Migration](https://cloud.google.com/products/cloud-migration/)
* [Migration Center](https://cloud.google.com/migration-center/docs/)
* [Application Migration](https://cloud.google.com/solutions/application-migration/)
* [Migrate to Virtual Machines](https://cloud.google.com/migrate/virtual-machines/)
* [Cloud Foundation Toolkit](https://cloud.google.com/foundation-toolkit/)
* [Database Migration Service](https://cloud.google.com/database-migration/)
* [Migrate to Containers](https://cloud.google.com/migrate/containers/)
* [BigQuery Data Transfer Service](https://cloud.google.com/bigquery-transfer/docs/introduction/)
* [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program/)
* [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/)
* [Storage Transfer Service](https://cloud.google.com/storage-transfer-service/)
* [VMware Engine](https://cloud.google.com/vmware-engine/)
* Mixed Reality
* [Immersive Stream for XR](https://cloud.google.com/immersive-stream/xr/)
* [Networking](https://cloud.google.com/products/networking/)
* [Cloud Armor](https://cloud.google.com/armor/)
* [Cloud CDN and Media CDN](https://cloud.google.com/cdn/)
* [Cloud DNS](https://cloud.google.com/dns/)
* [Cloud Load Balancing](https://cloud.google.com/load-balancing/)
* [Cloud NAT](https://cloud.google.com/nat/)
* [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity/)
* [Network Connectivity Center](https://cloud.google.com/network-connectivity-center/)
* [Network Intelligence Center](https://cloud.google.com/network-intelligence-center/)
* [Network Service Tiers](https://cloud.google.com/network-tiers/)
* [Virtual Private Cloud](https://cloud.google.com/vpc/)
* [Private Service Connect](https://cloud.google.com/private-service-connect/)
* [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
* [Operations](https://cloud.google.com/products/operations/)
* [Cloud Logging](https://cloud.google.com/logging/)
* [Cloud Monitoring](https://cloud.google.com/monitoring/)
* [Error Reporting](https://cloud.google.com/error-reporting/)
* [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus/)
* [Cloud Trace](https://cloud.google.com/trace/)
* [Cloud Profiler](https://cloud.google.com/profiler/docs/)
* [Cloud Quotas](https://cloud.google.com/docs/quotas)
* Productivity and Collaboration
* [AppSheet](https://about.appsheet.com/home/)
* [AppSheet Automation](https://cloud.google.com/appsheet/automation/)
* [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
* [Google Workspace Essentials](https://workspace.google.com/essentials/)
* [Gemini for Workspace](https://workspace.google.com/solutions/ai/)
* [Cloud Identity](https://cloud.google.com/identity/)
* [Chrome Enterprise](https://cloud.google.com/chrome-enterprise/)
* [Security and Identity](https://cloud.google.com/products/security-and-identity/)
* [Cloud IAM](https://cloud.google.com/security/products/iam/)
* [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection/)
* [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense/)
* [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence/)
* [Security Command Center](https://cloud.google.com/security/products/security-command-center/)
* [Cloud Key Management](https://cloud.google.com/security/products/security-key-management/)
* [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services/)
* [Chrome Enterprise Premium](https://chromeenterprise.google/products/chrome-enterprise-premium/)
* [Assured Workloads](https://cloud.google.com/security/products/assured-workloads/)
* [Google Security Operations](https://cloud.google.com/security/products/security-operations/)
* [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services/)
* [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
* [Serverless](https://cloud.google.com/serverless/)
* [Cloud Run](https://cloud.google.com/run/)
* [Cloud Functions](https://cloud.google.com/functions/)
* [App Engine](https://cloud.google.com/appengine/)
* [Workflows](https://cloud.google.com/workflows/)
* [API Gateway](https://cloud.google.com/api-gateway/)
* [Storage](https://cloud.google.com/products/storage/)
* [Cloud Storage](https://cloud.google.com/storage/)
* [Block Storage](https://cloud.google.com/products/block-storage/)
* [Filestore](https://cloud.google.com/filestore/)
* [Persistent Disk](https://cloud.google.com/persistent-disk/)
* [Cloud Storage for Firebase](https://firebase.google.com/products/storage/)
* [Local SSD](https://cloud.google.com/local-ssd/)
* [Storage Transfer Service](https://cloud.google.com/storage-transfer-service/)
* [Parallelstore](https://cloud.google.com/parallelstore/)
* [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes/)
* [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery/)
* [Web3](https://cloud.google.com/web3/)
* [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine/)
* [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc/)

* Save money with our transparent approach to pricing
* [Request a quote](https://cloud.google.com/contact/?direct=true)
* Pricing overview and tools
* [Google Cloud pricing](https://cloud.google.com/pricing/)
* [Pricing calculator](https://cloud.google.com/products/calculator/)
* [Google Cloud free tier](https://cloud.google.com/free/)
* [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization/)
* [Cost management tools](https://cloud.google.com/cost-management/)
* Product-specific Pricing
* [Compute Engine](https://cloud.google.com/compute/all-pricing/)
* [Cloud SQL](https://cloud.google.com/sql/pricing/)
* [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing/)
* [Cloud Storage](https://cloud.google.com/storage/pricing/)
* [BigQuery](https://cloud.google.com/bigquery/pricing/)
* [See full price list with 100+ products](https://cloud.google.com/pricing/list/)

* Learn & build
* [Google Cloud Free Program](https://cloud.google.com/free/)
* [Solution Generator](https://cloud.google.com/solution-generator/)
* [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
* [Blog](https://cloud.google.com/blog)
* [Learning Hub](https://cloud.google.com/learn/)
* [Google Cloud certification](https://cloud.google.com/certification/)
* [Cloud computing basics](https://cloud.google.com/discover/)
* [Cloud Architecture Center](https://cloud.google.com/architecture/)
* Connect
* [Innovators](https://cloud.google.com/innovators/innovatorsplus/)
* [Developer Center](https://cloud.google.com/developers/)
* [Events and webinars](https://cloud.google.com/events/)
* [Google Cloud Community](https://cloud.google.com/communities/)
* Consulting and Partners
* [Google Cloud Consulting](https://cloud.google.com/consulting/)
* [Google Cloud Marketplace](https://cloud.google.com/marketplace/)
* [Google Cloud partners](https://cloud.google.com/partners/)
* [Become a partner](https://partners.cloud.google.com/)

* ### Why Google
  
  + [Choosing Google Cloud](https://cloud.google.com/why-google-cloud/)
  + [Trust and security](https://cloud.google.com/trust-center/)
  + [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure/)
  + [Multicloud](https://cloud.google.com/multicloud/)
  + [Global infrastructure](https://cloud.google.com/infrastructure/)
  + [Customers and case studies](https://cloud.google.com/customers/)
  + [Analyst reports](https://cloud.google.com/analyst-reports/)
  + [Whitepapers](https://cloud.google.com/whitepapers/)
  + [Blog](https://cloud.google.com/blog)
* ### Products and pricing
  
  + [Google Cloud pricing](https://cloud.google.com/pricing/)
  + [Google Workspace pricing](https://workspace.google.com/pricing.html)
  + [See all products](https://cloud.google.com/products/)
* ### Solutions
  
  + [Infrastructure modernization](https://cloud.google.com/solutions/infrastructure-modernization/)
  + [Databases](https://cloud.google.com/solutions/databases/)
  + [Application modernization](https://cloud.google.com/solutions/application-modernization/)
  + [Smart analytics](https://cloud.google.com/solutions/smart-analytics/)
  + [Artificial Intelligence](https://cloud.google.com/solutions/ai/)
  + [Security](https://cloud.google.com/solutions/security/)
  + [Productivity & work transformation](https://workspace.google.com/enterprise/)
  + [Industry solutions](https://cloud.google.com/solutions/#industry-solutions)
  + [DevOps solutions](https://cloud.google.com/devops/)
  + [Small business solutions](https://cloud.google.com/solutions/#section-14)
  + [See all solutions](https://cloud.google.com/solutions/)
* ### Resources
  
  + [Google Cloud Affiliate Program](https://cloud.google.com/affiliate-program/)
  + [Google Cloud documentation](https://cloud.google.com/docs/)
  + [Google Cloud quickstarts](https://cloud.google.com/docs/get-started/)
  + [Google Cloud Marketplace](https://cloud.google.com/marketplace/)
  + [Learn about cloud computing](https://cloud.google.com/discover/)
  + [Support](https://cloud.google.com/support-hub/)
  + [Code samples](https://cloud.google.com/docs/samples)
  + [Cloud Architecture Center](https://cloud.google.com/architecture/)
  + [Training](https://cloud.google.com/learn/training/)
  + [Certifications](https://cloud.google.com/learn/certification)
  + [Google for Developers](https://developers.google.com)
  + [Google Cloud for Startups](https://cloud.google.com/startup/)
  + [System status](https://status.cloud.google.com)
  + [Release Notes](https://cloud.google.com/release-notes)
* ### Engage
  
  + [Contact sales](https://cloud.google.com/contact/)
  + [Find a Partner](https://cloud.google.com/find-a-partner)
  + [Become a Partner](https://cloud.google.com/partners/become-a-partner/)
  + [Events](https://cloud.google.com/events/)
  + [Podcasts](https://cloud.google.com/podcasts/)
  + [Developer Center](https://cloud.google.com/developers/)
  + [Press Corner](https://www.googlecloudpresscorner.com/)
  + [Google Cloud on YouTube](https://www.youtube.com/googlecloud)
  + [Google Cloud Tech on YouTube](https://www.youtube.com/googlecloudplatform)
  + [Follow on X](https://x.com/googlecloud)
  + [Join User Research](https://userresearch.google.com/?reserved=1&utm_source=website&Q_Language=en&utm_medium=own_srch&utm_campaign=CloudWebFooter&utm_term=0&utm_content=0&productTag=clou&campaignDate=jul19&pType=devel&referral_code=jk212693)
  + [We're hiring. Join Google Cloud!](https://careers.google.com/cloud)
  + [Google Cloud Community](https://www.googlecloudcommunity.com/)

* [About Google](https://about.google)
* [Privacy](https://policies.google.com/privacy)
* [Site terms](https://policies.google.com/terms)
* [Google Cloud terms](https://cloud.google.com/product-terms/)
* [Cookies management controls](#)
* [Our third decade of climate action: join us](https://cloud.google.com/sustainability)
* Sign up for the Google Cloud newsletter[Subscribe](https://cloud.google.com/newsletter/)

*language*‪English‬

* ‪English‬
* ‪Deutsch‬
* ‪Español‬
* ‪Español (Latinoamérica)‬
* ‪Français‬
* ‪Indonesia‬
* ‪Italiano‬
* ‪Português (Brasil)‬
* ‪简体中文‬
* ‪繁體中文‬
* ‪日本語‬
* ‪한국어‬
