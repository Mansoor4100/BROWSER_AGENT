🤖 Autonomous Browser Agent
<p align="center"> <img src="https://raw.githubusercontent.com/microsoft/playwright/main/docs/src/images/playwright-logo.svg" width="120" alt="Browser Agent Logo"/> </p> <p align="center"> <b>An LLM-powered autonomous browser agent that can plan, navigate, interact, and extract information from the web.</b> </p> <p align="center"> Built using <b>Playwright</b>, <b>HuggingFace LLMs</b>, and <b>Python</b> — fully CPU-based. </p>
🚀 Key Features

🌐 Autonomous web browsing using Playwright

🧠 LLM-driven task planning (JSON-based action plans)

⌨️ Browser actions: OPEN, TYPE, PRESS, CLICK, WAIT

🔍 Dynamic content extraction from real websites

🔗 Multi-link traversal and data extraction

🛡️ Robust handling of invalid actions and malformed LLM outputs

💻 Runs entirely on CPU (no GPU required)

📄 Saves extracted data to structured JSON files

🏗️ Tech Stack
Layer	Technology
Browser Automation	Playwright
LLM	google/flan-t5-base (HuggingFace)
Planning	JSON-based LLM action planning
Language	Python 3.10+
Runtime	CPU-only
Environment	Virtualenv
📁 Project Structure
autonomous-browser-agent/
│
├── agent.py                  # Main controller (planner + executor)
├── agent_planner.py          # LLM-based action planner
├── browser_agent.py          # Playwright browser wrapper
├── extracted_results.json    # Single-page extraction output
├── multi_extracted_results.json  # Multi-link extraction output
├── venv/
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/autonomous-browser-agent.git
cd autonomous-browser-agent

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
playwright install

▶️ Running the Agent
python agent.py


The agent will:

Generate a JSON plan using the LLM

Open the browser (visible mode)

Perform search and navigation

Extract content

Save results to JSON files

🧠 How the Agent Works

User defines a task (e.g., Search for Python latest version)

LLM converts the task into structured JSON actions

Agent parses and validates the plan

Browser executes actions step-by-step

Agent extracts text, links, and page content

Results are saved for later use

🧩 Supported Actions
Action	Description
OPEN	Navigate to a URL
TYPE	Type text into input fields
PRESS	Keyboard actions (Enter, etc.)
CLICK	Click page elements
WAIT	Dynamic wait for page load
EXTRACT	Extract text or attributes
DONE	End task execution
🛠️ Challenges Faced & Solutions
❌ Invalid URLs from LLM

Problem: LLM generated malformed URLs
Solution: Added strict validation and action filtering

❌ LLM returning plain text instead of JSON

Problem: Planner output was not executable
Solution: Enforced JSON-only planning format

❌ Pages closing too quickly

Problem: Browser exited before observation
Solution: Added dynamic waits and execution control

❌ Selector mismatches across sites

Problem: Different DOM structures
Solution: Used selector fallbacks (article p, main p, etc.)

❌ Over-extraction (YouTube, StackOverflow noise)

Problem: Irrelevant content captured
Solution: Scoped extraction to meaningful page sections

📸 Demo (Add to GitHub)

You can include:

Browser opening and searching

Clicking top results

Extracted content JSON

Demo GIF

Example:

![Demo](demo.gif)

📌 Future Improvements

Memory across multiple tasks

Task chaining (multiple searches in one run)

Page summarization using LLM

Vision-based DOM understanding

Tool-based agent framework (LangGraph / CrewAI)

Headless cloud deployment

Rate-limit and CAPTCHA handling

👨‍💻 Author

Shaik Nabi Mansoor
AI | LLM Agents | Browser Automation | Full-Stack Development

⭐ Why This Project Matters

This project demonstrates:

Real-world agentic AI systems

LLM-driven decision making

Practical browser automation

Handling unreliable LLM outputs

Production-style error handling

Strong foundation for AI agents and RPA systems
