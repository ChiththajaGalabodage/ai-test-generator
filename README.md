<div align="center">

# AI Test Generator — Python Prototype
**Source-code analysis, Gemini-generated pytest tests and execution reports**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/Testing-pytest-0A9EDC?logo=pytest&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-4285F4)

[Source repository](https://github.com/ChiththajaGalabodage/ai-test-generator)

</div>

## Overview

An exploratory Python command-line prototype that converts source code into generated pytest test cases, executes them, and summarizes the result. The implementation uses the Gemini API and modular local utilities.

This repository represents **early test-generation exploration**, not the final OpenAPI-driven TestGenAgent or the thesis's full two-agent CI/CD evaluation.

## Pipeline

```text
Target Python file
       ↓
src/analyzer.py — extract code structure
       ↓
src/generator.py — prompt Gemini for pytest tests
       ↓
generated_test.py — write model output
       ↓
src/runner.py — execute generated tests
       ↓
src/reporter.py — summarize results
```

The repository also has `src/healer.py`; however, the inspected `main.py` executes the four steps above and does **not** invoke the healer in that entry-point flow.

## Files

| File | Role |
|---|---|
| `main.py` | CLI pipeline entry point |
| `src/analyzer.py` | Source analyzer |
| `src/generator.py` | Gemini test generator |
| `src/runner.py` | pytest test executor |
| `src/reporter.py` | Test-run summary |
| `src/healer.py` | Additional experimental repair helper |
| `requirements.txt` | `google-generativeai`, `pytest`, `pytest-json-report` |

## Setup

```bash
git clone https://github.com/ChiththajaGalabodage/ai-test-generator.git
cd ai-test-generator
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Configure the environment variable expected by `main.py`:

```bash
# macOS / Linux
export GOOGLE_API_KEY="your-key-from-a-secure-source"
```

```powershell
# Windows PowerShell
$env:GOOGLE_API_KEY = "your-key-from-a-secure-source"
```

**Run:**

```bash
python main.py path/to/your_python_module.py
```

The program writes `generated_test.py` in the working directory and runs it through the local runner. Gemini connectivity and API quotas are required; this entry point does not implement an offline fallback.

## Research and safety notes

- Generated Python code should be **reviewed** and executed in an isolated environment before use on sensitive projects.
- A passing generated test does not prove behavioral correctness or unique defect detection.
- The model in `src/generator.py` is currently configured for `gemini-2.0-flash`; hosted model availability can change.
- The repository's previous README contained Git merge-conflict markers; this replacement restores valid Markdown.
- The thesis's reported selection, repair and final-gate results must be attributed to the separate FastAPI case study, not this CLI prototype.

**Research context:** *Enhancing Continuous Testing in DevOps and CI/CD Pipelines Using Large Language Models*.

**Author:** [Chiththaja Galabodage](https://github.com/ChiththajaGalabodage)
