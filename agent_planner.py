from transformers import pipeline
import json

# Use FLAN-T5 for plan generation
planner = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_plan(task, observation=""):
    """
    Generates a multi-step JSON plan from task description.
    Returns list of actions.
    """
    prompt = f"""
You are a browser automation agent.
Break the task into JSON steps. Output only valid JSON.

Task: {task}
Current observation: {observation}

Use actions: OPEN, TYPE, PRESS, CLICK, EXTRACT, DONE.
Example output:
[
  {{"type": "OPEN", "url": "https://duckduckgo.com"}},
  {{"type": "TYPE", "selector": "input[name='q']", "value": "Python latest version"}},
  {{"type": "PRESS", "value": "Enter"}},
  {{"type": "EXTRACT", "selector": "a.result__a", "attribute": "href"}},
  {{"type": "CLICK", "selector": "a.result__a:first-child"}},
  {{"type": "EXTRACT", "selector": "h1", "attribute": "innerText"}},
  {{"type": "DONE"}}
]
"""
    result = planner(prompt, max_length=500)
    try:
        plan = json.loads(result[0]["generated_text"])
    except json.JSONDecodeError:
        # fallback: minimal plan
        plan = [
    {"type": "OPEN", "url": "https://duckduckgo.com"},
    {"type": "TYPE", "selector": "input[name='q']", "value": task},
    {"type": "PRESS", "value": "Enter"},
    {"type": "EXTRACT", "selector": "a[data-testid='result-title-a']", "attribute": "href"},
    {"type": "CLICK", "selector": "a[data-testid='result-title-a']:first-child"},
    {"type": "EXTRACT", "selector": "h1", "attribute": "innerText"},
    {"type": "EXTRACT", "selector": "p", "attribute": "innerText"},
    {"type": "DONE"}
]
    return plan
