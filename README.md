# 📂 Google Drive AI Assistant

A conversational AI agent built to help users search, filter, and discover files within a Google Drive directory using natural language. This project leverages **LangGraph** for stateful agentic orchestration and **Groq** for intelligent tool calling.

---

## 🚀 Live Demo
*   **Frontend (Streamlit):** [Insert your Streamlit URL here]
*   **Backend API (FastAPI):** [Insert your Render/Hugging Face URL here]

---

## ✨ Key Features
*   **Natural Language Discovery:** Users can ask for files in plain English (e.g., *"Find the project proposal from last Tuesday"*).
*   **Complex Query Translation:** Automatically translates user intent into optimized Google Drive API `q` parameter strings.
*   **Advanced Filtering:** Support for:
    *   **Exact & Partial Name Search** (e.g., `name = 'data.csv'` or `name contains 'report'`).
    *   **File Type Filtering** (e.g., `mimeType = 'application/pdf'`).
    *   **Content-Based Search** (Searching text within documents using `fullText`).
    *   **Date-Based Retrieval** (Filtering by `modifiedTime`).
*   **Stateful Conversations:** Uses **LangGraph** to maintain context and manage multi-step reasoning loops.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **LLM** | Groq Llama-3.3-70B |
| **Agent Framework** | LangGraph |
| **Backend** | Python, FastAPI, Uvicorn |
| **Frontend** | Streamlit |
| **API Integration** | Google Drive API v3 |
| **Deployment** | Render (Backend) & Streamlit Cloud (Frontend) |

---

## 🏗️ Architecture & Logic

The agent follows a **ReAct (Reason + Act)** pattern. When a user sends a message:
1.  The **Agent Node** determines if the query requires a file search.
2.  If a search is needed, it invokes the **DriveSearchTool**, translating the request into a precise `q` string.
3.  The **Tool Node** executes the request against the Google Drive API using a Service Account.
4.  The results are returned to the LLM to provide a conversational summary.

> **Note:** This project implements server-side filtering via the Drive API's `q` parameter to ensure high performance and accuracy, rather than fetching and filtering data in-memory.

---

## ⚙️ Setup & Installation

### 1. Environment Variables
Create a `.env` file in the `backend/` directory:
```text
GOOGLE_API_KEY="your_gemini_api_key"
GCP_SERVICE_ACCOUNT_JSON='{"your_service_account_details"}'
GROQ_API_KEY="your_groq_api_key"
```

### 2. Local Development
**Run Backend:**
```bash
cd backend
python -m uvicorn app.main:app --reload
```

**Run Frontend:**
```bash
cd frontend
streamlit run app.py
```

---

## 🚀 Deployment

### Backend (Render/Hugging Face)
*   **Root Directory:** `backend`
*   **Build Command:** `pip install -r ../requirements.txt`
*   **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend (Streamlit Cloud)
*   **Main file path:** `frontend/app.py`
*   **Requirement:** Ensure the backend URL in `app.py` is updated to your live production URL.

---

## 👨‍💻 About the Author
Developed by **Shreshth Shukla**, a 3rd-year B.Tech student at **IIT Ropar**. This project was created to explore the intersection of LLM tool-calling and cloud storage automation.
