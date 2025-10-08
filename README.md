###Akira.ai 🤖
###Intelligent Web-to-Markdown ML Pipeline

Convert messy web HTML into clean, LLM-ready markdown using ML-powered processing and intelligent web scraping.

Why Akira.ai?
Web scraping breaks on anti-bot detection. HTML is messy with ads and clutter. Manual cleaning doesn't scale.
Akira.ai solves this with:

Multi-engine scraping (Playwright, Selenium, undetected-chromedriver)
Anti-bot bypass and intelligent retry logic
Dual-stage HTML cleaning (html2text + markdownify)
ML-powered text processing using transformers (MiniLM-V6)
LLM integration for post-processing (Vertex AI, Hugging Face)


Features
✅ Reliable Scraping - Multiple engines with anti-bot detection bypass
✅ Clean Output - Transforms raw HTML into structured markdown
✅ ML-Powered - Uses sentence transformers for semantic understanding
✅ Docker Ready - Fully containerized for easy deployment
✅ Multi-LLM Support - Integrate with OpenAI, Vertex AI, Hugging Face
✅ 50+ Samples - Includes dataset of HTML/markdown pairs for testing

Tech Stack
Scraping: Playwright, Selenium, undetected-chromedriver, BeautifulSoup
ML/NLP: Transformers, sentence-transformers (MiniLM-V6), LangChain
Processing: html2text, markdownify, semchunk
LLMs: Vertex AI, Hugging Face, OpenAI, Mistral
Infrastructure: Docker, Python 3.11+

Use Cases

Build RAG systems with web content
Create training datasets from websites
Extract clean text for LLM fine-tuning
Archive documentation as markdown
Content analysis and research


Project Structure
akiraai/
├── akiraai/              # Main codebase
│   ├── data_preprocessing/
│   ├── web_doc_loader/
│   ├── models/
│   └── utils/
├── Dataset/
│   └── dataset_collection/  # 50+ HTML/markdown samples
├── tests/                # Test scripts
└── requirements.txt

Sample Dataset
Includes 50+ curated pairs of raw HTML and clean markdown from:

News articles
E-commerce pages (Airbnb, travel)
Documentation
Blog posts

Located in: Dataset/dataset_collection/

Author
Tharun Thammaiah B.J
GitHub: @tharunthammaiahbj
LinkedIn: linkedin.com/in/tharun-thammaiah-b-j-08546425a

License
MIT License - Use responsibly and respect website terms of service.

Built for developers who need reliable web scraping + ML-powered text extraction
