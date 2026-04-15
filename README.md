# LangChain Chain Architectures 🦜🔗

This repository contains a collection of Python scripts demonstrating various chain patterns in **LangChain**. Each script is designed to showcase a specific way to orchestrate Large Language Models (LLMs) using the LangChain Expression Language (LCEL).

---

## 📂 Project Structure

### 1. Simple Chain (`simple_chain.py`)
The foundational building block. It connects a prompt directly to an LLM and parses the result into a string.
* **Logic:** `Prompt` ➔ `LLM` ➔ `OutputParser`
* **Example:** Generating basic facts about a topic (e.g., cricket).

### 2. Sequential Chain (`sequential_chain.py`)
Demonstrates a linear pipeline where the output of the first task is passed as the input to the second.
* **Logic:** `Task 1 (Summary)` ➔ `Task 2 (Translation)`

### 3. Parallel Chain (`parallel_chains.py`)
Shows how to run multiple chains at the same time for efficiency.
* **Logic:** `Input` ➔ `(Chain A + Chain B + Chain C)` ➔ `Combined Output`
* **Benefit:** Great for getting multiple perspectives (e.g., Pros vs. Cons) simultaneously.

### 4. Conditional Chain (`conditional_chains.py`)
Implements "routing" logic. The LLM decides which path to take based on the user's input.
* **Logic:** `Router` ➔ `If X then Chain 1, else Chain 2`

---

## 🛠️ Getting Started

### Prerequisites
* **Python 3.13**
* **OpenAI API Key** (Stored in `.env`)

### Installation
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/philicamit/LangChain_Chain.git](https://github.com/philicamit/LangChain_Chain.git)

2. **Setup Environment:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. **Install Libraries:**
    ```Bash
    pip install -r requirements.txt

**🔒 Security Note**
The .env file containing your API keys is excluded from this repository via .gitignore to prevent unauthorized usage.

🚀 Technologies
Framework: LangChain

Language: Python 3.13

Environment: VS Code / Powershell

## 📊 Author
**Amit Rastogi** 