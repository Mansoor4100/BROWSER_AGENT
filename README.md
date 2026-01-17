Autonomous Browser Agent (LLM-Powered)
Overview

This project is an Autonomous Browser Agent that uses a Large Language Model (LLM) to plan and execute browser actions such as searching, clicking links, waiting for page loads, and extracting content from web pages.

Unlike rule-based scrapers, this agent:

Dynamically plans actions in JSON

Executes them using a real browser (Playwright)

Handles multi-step web tasks autonomously

Example task:

“Search for Python latest version and extract content from top results.”

Key Features

LLM-based JSON action planning

Real browser automation using Playwright

Supports actions:

OPEN

TYPE

PRESS

CLICK

WAIT

EXTRACT

DONE

Extracts content from multiple websites

Stores structured results in JSON files

CPU-only execution (no GPU required)

Project Structure
autonomous-browser-agent/
│
├── agent.py                  # Main execution loop
├── agent_planner.py          # LLM → JSON plan generator
├── browser_agent.py          # Playwright browser wrapper
├── extracted_results.json    # Single-page extraction output
├── multi_extracted_results.json # Multi-page extraction output
├── requirements.txt
├── README.md
└── .gitignore

Technologies Used

Python

Playwright (browser automation)

Hugging Face Transformers

LLM (text generation model)

JSON-based agent planning

DuckDuckGo (search engine)

How It Works

User provides a natural language task

LLM converts the task into a JSON action plan

Agent executes actions step-by-step in the browser

Extracted content is saved into structured JSON files

Agent stops automatically when the task is complete

Demo
Example Task
Search for Python latest version and extract top 3 results content

What Happens

Opens DuckDuckGo

Types the query

Presses Enter

Extracts result links

Opens links one by one

Extracts headings and paragraphs

Saves results to JSON

Demo Screenshots / GIF

📸 Add screenshots here

Browser opening DuckDuckGo

Search results page

Extracted JSON output

📽️ Optional GIF

Screen recording of python agent.py execution

Output Example
{
  "url": "https://www.python.org/",
  "content": [
    "Welcome to Python.org",
    "Python is a programming language..."
  ]
}

Challenges Faced & Solutions

Invalid URL errors

Fixed by separating LLM planning from execution logic

LLM generating non-action text

Enforced strict JSON-only output

Dynamic page loading

Added wait and timeout handling

Different page structures

Used multiple fallback selectors

Large content extraction

Limited extraction scope and stored results incrementally

Future Improvements

Add headless / non-headless toggle

Improve content summarization using LLM

Add multi-task chaining

Support file downloads

Add retry logic for failed steps

Integrate vector database (RAG) for extracted content

Add UI dashboard for task monitoring

How to Run
pip install -r requirements.txt
python agent.py

Use Cases

Web research automation

Data collection for AI pipelines

Autonomous web testing

Content aggregation

AI agent experimentation

Author

Shaik Nabi Mansoor
AI / ML | Agentic Systems | Automation