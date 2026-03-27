# 🧩 AI Pipeline Builder — Backend

The powerful execution engine for the AI Pipeline Builder. Built with **FastAPI** and **Python**, this backend handles complex DAG (Directed Acyclic Graph) validation and processes node-based AI workflows.

✨ Features

* ⚡ **FastAPI Performance** — High-performance asynchronous API endpoints.
* 🔄 **DAG Validation** — Real-time cycle detection to prevent infinite loops.
* 🧠 **Extensible Logic** — Supports LLM, Input, Output, and Text node processing.
* 🛡️ **Pydantic Schemas** — Strict data validation for incoming pipeline JSON.
* 🌐 **CORS Middleware** — Seamless integration with the Next.js frontend.

🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **FastAPI** | Modern, fast web framework for Python |
| **Pydantic** | Data validation and settings management |
| **Uvicorn** | Lightning-fast ASGI server |
| **Python 3.9+** | Core programming language |

🚀 Getting Started

```bash
# Clone and navigate
git clone [https://github.com/Iamhc/Ai-pipeline-backend.git](https://github.com/Iamhc/Ai-pipeline-backend.git)
cd Ai-pipeline-backend

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install and run
pip install -r requirements.txt
uvicorn main:app --reload
