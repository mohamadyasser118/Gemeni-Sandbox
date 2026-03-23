# 📚 Learning Project Statement

## What This Is

This is an **educational project** created to learn and practice:
- Autonomous AI agent patterns (agentic loops)
- Secure file and code operations
- LLM function calling integration with Gemini API
- Python software engineering best practices

## What This Is NOT

This project is **NOT production-ready** and should **NOT** be used for:
- Production systems or critical infrastructure
- Untrusted code execution in real environments
- Security-sensitive operations without additional hardening
- Handling sensitive data without encryption

## Educational Value

### Core Learning Areas

**1. AI/ML Concepts**
- How LLMs can invoke external functions (function calling)
- Building agentic loops that make decisions autonomously
- Prompt engineering and system instructions
- Multi-turn reasoning and conversation history

**2. Software Security**
- Path validation and preventing directory traversal
- Sandboxing code execution environments
- Input validation and sanitization
- Resource limiting (timeouts, file size limits)

**3. Python Development**
- Subprocess management and process control
- File I/O operations safely
- Exception handling and error recovery
- API integration patterns

**4. System Design**
- Function dispatcher architecture
- Configuration management
- Testing strategies (unit and integration)
- Error handling patterns

## Sandbox Limitations

### What the Sandbox Protects Against
- Directory traversal attacks (reading files outside allowed directories)
- Unbounded file reads (limited to 10K characters)
- Infinite code execution (30-second timeout)
- Unauthorized file writes (limited to allowed directory)

### What the Sandbox Does NOT Protect Against
- CPU intensive operations
- Memory exhaustion
- Integer overflow attacks
- Network-based attacks
- Side-channel attacks
- Privilege escalation

## How to Use This for Learning

### Module 1: Understanding File Operations (Weeks 1-2)
1. Read `functions/get_files_info.py`
2. Modify it to add new features
3. Write tests for your changes
4. Run the tests
5. Try the agent using your modified function

### Module 2: Building the Agentic Loop (Weeks 2-3)
1. Read `main.py` and understand the iteration pattern
2. Trace through a complete agent execution with `--verbose`
3. Add logging to understand decision-making
4. Modify the system prompt in `prompts.py`
5. Observe how the agent behaves differently

### Module 3: Security Patterns (Week 3-4)
1. Try to escape the sandbox (read files outside allowed dir)
2. Observe how path validation prevents this
3. Modify the validation logic and test what breaks
4. Understand why each security check exists

### Module 4: Integration & API (Week 4)
1. Replace Gemini API with a local model (ollama, llama.cpp)
2. Modify function calling to work with your model
3. Observe differences in agent behavior
4. Experiment with different LLM instructions

## Key Files to Study

| File | Focus | Learning Goal |
|------|-------|----------------|
| `main.py` | Agentic Loop | Understand iterative decision-making |
| `prompts.py` | Instructions | Learn prompt engineering |
| `functions/*.py` | Safety | See security patterns in action |
| `call_functions.py` | Dispatcher | Understand function routing |
| `calculator/` | Example | See agent in action with a real task |

## Experiment Ideas

### Easy (1-2 hours)
- [ ] Add a new function (e.g., `get_system_info`)
- [ ] Modify the system prompt to change agent behavior
- [ ] Add logging to trace agent decisions
- [ ] Run tests with different Python versions

### Medium (3-5 hours)
- [ ] Integrate local LLM instead of Gemini API
- [ ] Add database operations (read-only)
- [ ] Create new calculator features
- [ ] Build comprehensive test suite

### Advanced (1-2 weeks)
- [ ] Replace subprocess with Docker-based sandboxing
- [ ] Add web server that runs the agent
- [ ] Implement persistent conversation history (database)
- [ ] Create visualization of agent decision-making

## Important Reminders

⚠️ **Before using in ANY environment:**
1. Never run agent on untrusted prompts
2. Always use isolated, controlled environments
3. Never expose API keys in public repositories
4. Never run this with elevated privileges

✅ **For safe learning:**
1. Use in local environment only
2. Create test cases before experimenting
3. Review code changes before running agent
4. Document your experiments

## Moving to Production

If you want to build a production system based on these concepts:

1. **Add authentication & authorization**
   - User identity management
   - Role-based access control
   - Audit logging

2. **Enhance security**
   - OS-level sandboxing (containers)
   - Network isolation
   - Code signing and verification
   - Rate limiting and DDoS protection

3. **Improve monitoring**
   - Error tracking (Sentry)
   - Performance monitoring (monitoring tools)
   - Usage analytics
   - Alert systems

4. **Operational requirements**
   - Deployment pipelines (CI/CD)
   - Database persistence
   - Backup and recovery
   - Disaster planning

5. **Compliance**
   - Security audits
   - Penetration testing
   - Documentation and SLAs
   - Legal review

## Resources for Next Steps

- [OWASP: Secure Coding](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Python Security Docs](https://python.readthedocs.io/)
- [Container Security Best Practices](https://www.cisecurity.org/)
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist)

## Questions?

This is a learning project, so questions are encouraged!
- Read the source code
- Modify and test
- Write your own functions
- Share your experiments with others

---

**Remember:** The goal is to learn. Make mistakes. Fix them. Understand why. That's how we grow.

Happy learning! 🚀
