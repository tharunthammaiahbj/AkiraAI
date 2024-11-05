"""
This module contains advanced prompts for data extraction and summarization nodes in the ScrapeGraphAI application.
"""

DATA_EXTRACTION_SUMMARY_PROMPT = """
As an AI data analyst, you have retrieved the following content from a website. 
Your task is to analyze and summarize the key information in a clear and concise manner. 
Please provide a structured summary that captures the essence of the content in no more than 30 words, highlighting important facts or insights relevant to product demand, competition analysis, or trends. 
Ensure the summary is actionable and suitable for inclusion in a report or dashboard.

WEBSITE CONTENT: {content}
"""
