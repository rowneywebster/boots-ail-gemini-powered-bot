# 🧠 Build an AI Agent (Mini Claude Code)

If you've ever used **Cursor** or **Claude Code** as an "agentic" AI editor, you'll understand what we're building in this project.

We're making a **toy version of Claude Code** using **Google's free Gemini API**!  
As long as you have an LLM at your disposal, it's surprisingly simple to build a (somewhat) effective custom agent.

---

## 🚀 What Does the Agent Do?

The program is a **CLI tool** that:

1. Accepts a coding task (e.g.,  
   `"strings aren't splitting in my app, pweeze fix 🥺👉🏽👈🏽"`)

2. Chooses from a set of predefined functions to work on the task:
   - Scan the files in a directory
   - Read a file's contents
   - Overwrite a file's contents
   - Execute the python interpreter on a file

3. Repeats step 2 until the task is complete (or fails miserably 😅).

---

### 🛠 Example Run

Imagine I have a buggy calculator app.  
I run the agent like this:

```bash
uv run main.py "fix my calculator app, its not starting correctly"
```
### Output:

```bash
# Calling function: get_files_info       # Scanning project files
# Calling function: get_file_content     # Reading file contents
# Calling function: write_file           # Writing fixes into file
# Calling function: run_python_file      # Running Python to test
# Calling function: write_file           # Applying another fix
# Calling function: run_python_file      # Running again to confirm
# Final response:
# Great! The calculator app now seems to be working correctly. 
# The output shows the expression and the result in a formatted way.
```

## 📦 Prerequisites

- Python **3.10+** installed  
- [uv project and package manager](https://github.com/astral-sh/uv)  
- Access to a Unix-like shell (e.g. **zsh** or **bash**)  
- (Optional) **Go installed** – if you have Go on your machine from a past install, that's fine.   

---

## 🎯 Learning Goals

- Introduce you to **multi-directory Python projects**  
- Understand how **AI tools work under the hood** (not just from the UI)  
- Practice your **Python** and **functional programming** skills  

> ⚡ The goal is **NOT** to build an LLM from scratch,  
> but to use a pre-trained LLM to build an **agent** from scratch.  

---

## 🐍 Python Setup

We’ll use `uv` to manage the project and dependencies.

1. **Initialize a new project**
   ```bash
   uv init your-project-name
   cd your-project-name
   ```
## 🔧 Environment Setup

1. **Create a virtual environment**
   ```bash
   uv venv
   ```
2. **Activate the virtual environment**

   ```bash
   source .venv/bin/activate
   ```
3. **Add dependencies**

   ```bash
   uv add google-genai==1.12.1
   uv add python-dotenv==1.1.0
   ```
## 🔑 Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)  
2. Copy your API key.  
3. Create a `.env` file in your project root and add:  

  ```env
   GEMINI_API_KEY="your_api_key_here"
  ```
## ▶️ Run the Agent

```bash
uv run main.py "your coding task here"
```

Example
```bash
uv run main.py "fix my calculator app, its not starting correctly"
```

## 🏁 Wrap-Up

You now have the building blocks for a **toy AI agent** that:

- 📝 Takes natural language coding requests  
- 📂 Interacts with your local project files  
- 🤖 Uses **Gemini API** under the hood to decide what to do  

✨ Think of it as your **mini Claude Code**, running locally.  
---



