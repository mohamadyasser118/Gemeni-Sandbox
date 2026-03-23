# AI Agent with Sandbox-Protected File Operations

> **📚 Learning Project** — This is an educational project designed to demonstrate autonomous AI agent patterns, secure file operations, and LLM function calling. Not intended for production use.

## Overview

A Python-based autonomous AI agent powered by Google's Gemini API that performs sandboxed file operations and Python code execution. The agent autonomously analyzes tasks, calls appropriate functions, and iterates to complete complex operations.

**Key Learning Objectives:**
- Understanding agentic loops and multi-turn reasoning
- Implementing security guardrails for file/code operations
- Integrating LLM function calling with custom tools
- Building sandbox patterns for safe code execution

## ✨ Features

### 🔒 Sandbox-Protected Operations
- **`get_files_info`** — List directory contents with metadata (recursively)
- **`get_file_content`** — Read file contents with character limits and truncation detection
- **`write_file`** — Create/overwrite files with automatic directory creation
- **`run_python_file`** — Execute Python scripts safely with timeout protection

### 🤖 Autonomous AI Capabilities
- **20-iteration agentic loop** — Agent independently plans and executes multi-step tasks
- **Conversation history** — Persistent context across iterations
- **Function calling** — LLM seamlessly invokes tools and interprets results
- **Error handling** — Graceful failures with clear feedback to the agent

### 🛡️ Security Model
- **Path validation** — Prevents directory traversal attacks
- **Character limits** — Restricts file read size (10K chars max)
- **Subprocess timeout** — Prevents infinite execution (30 second limit)
- **Sandboxed working directory** — All operations confined to `./calculator`

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- `uv` package manager ([install here](https://github.com/astral-sh/uv))
- Google Gemini API key (free tier available at [ai.google.dev](https://ai.google.dev))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-Agent.git
   cd AI-Agent
   ```

2. **Create `.env` file with your API key**
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

### Usage

Ask the agent to perform a task:

```bash
uv run main.py "List all files in the calculator directory"
```

**More examples:**
```bash
# Calculate complex expressions
uv run main.py "Evaluate: 15 + 3 * (8 - 2)"

# Fix bugs autonomously
uv run main.py "The calculator gives wrong results for operator precedence. Debug and fix it."

# Run tests
uv run main.py "Execute the calculator tests and report results"

# Multi-step tasks
uv run main.py "Create a new Python file with a function that calculates factorial, then test it"
```

**Verbose mode:**
```bash
uv run main.py "your task here" --verbose
```

## 📁 Project Structure

```
AI-Agent/
├── main.py                    # Agentic loop entry point
├── prompts.py                 # System prompt for the agent
├── call_functions.py          # Function dispatcher
├── config.py                  # Configuration constants
│
├── functions/
│   ├── get_files_info.py      # List directory contents
│   ├── get_file_content.py    # Read file with limits
│   ├── write_file.py          # Create/write files
│   └── run_python_file.py     # Execute Python scripts
│
├── calculator/                # Sandboxed working directory
│   ├── main.py
│   ├── tests.py
│   ├── test_parentheses.py
│   └── pkg/
│       ├── calculator.py      # Expression evaluator
│       └── render.py
│
├── test_*.py                  # Function tests
├── pyproject.toml             # Project metadata
├── .env                       # API key (local only)
├── .gitignore                 # Git ignore patterns
└── README.md                  # This file
```

## 🏗️ Architecture

### Agentic Loop Pattern
```
User Input
    ↓
[Iteration 1-20]
├─ Send messages + functions to Gemini
├─ Agent decides which function(s) to call
├─ Execute function(s)
├─ Return results to agent
├─ Agent interprets and plans next step
└─ Continue if task incomplete
    ↓
Final Response
```

### Security Layers
1. **Path Validation** — `os.path.normpath()` + `os.path.commonpath()` to detect escapes
2. **Type Checking** — Function arguments validated before execution
3. **Resource Limits** — Character limits (10K), timeout limits (30s)
4. **Working Directory Isolation** — All operations confined to `./calculator`

## 🧪 Testing

Run the test suite:
```bash
# Test get_files_info function
python test_get_files_info.py

# Test get_file_content function
python test_get_file_content.py

# Test write_file function
python test_write_file.py

# Test run_python_file function
uv run test_run_python_file.py

# Test calculator (in calculator directory)
cd calculator && python tests.py
```

## 🔧 Configuration

Edit `config.py` to adjust:
```python
MAX_CHARS = 10000        # Maximum characters to read from a file
MAX_ITERATIONS = 20      # Maximum agentic loop iterations
TIMEOUT = 30             # Subprocess timeout in seconds
```

## 📚 Learning Resources

### What This Project Teaches

**AI/ML Concepts:**
- Function calling with LLMs (how Claude/Gemini invoke tools)
- Agentic loops and multi-turn reasoning
- Prompt engineering and system instructions
- Error recovery and graceful degradation

**Software Engineering:**
- Security: Path validation, sandboxing, input validation
- Testing: Unit tests, integration testing
- Error handling: Try-except patterns, custom error messages
- API integration: Working with external APIs and managing keys

**Python Patterns:**
- Working with `subprocess` module
- File I/O operations and safety
- Type hints and validation
- Argument parsing with `argparse`

## 🎯 Example Walkthrough

**Task:** "Debug the calculator's operator precedence bug"

**Agent's autonomous process:**
1. **Iteration 1:** Reads files to understand calculator structure
2. **Iteration 2:** Writes test to expose the bug
3. **Iteration 3:** Identifies wrong precedence in calculator.py
4. **Iteration 4:** Fixes the bug by reordering operations
5. **Iteration 5:** Verifies fix by running tests

Result: ✅ Bug fixed in 5 iterations without human intervention

## 🚫 Security Concerns (Learning Focus)

This project intentionally demonstrates:
- ✅ What NOT to do in production (sandbox for learning, not security guarantee)
- ✅ How to add guardrails incrementally
- ✅ The importance of defense-in-depth
- ⚠️ **NOT suitable for untrusted code execution** (for education only)

## 🤔 FAQ

**Q: Is this production-ready?**
A: No. It's educational. For production, you'd need additional security hardening, monitoring, and compliance features.

**Q: Can I run arbitrary code with this?**
A: Yes, that's the point — it demonstrates an agentic loop. But the sandbox is for learning, not security.

**Q: How do I get the API key?**
A: Visit [ai.google.dev](https://ai.google.dev), create a free account, and get your API key.

**Q: What if the agent gets stuck?**
A: It stops after 20 iterations by default. You can reduce this in `config.py`.

## 🔗 Resources

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Python Function Calling](https://ai.google.dev/docs/function_calling)
- [Security in Python](https://python.readthedocs.io/en/stable/library/security_warnings.html)
