# Smart File QA

A full-stack AI application that lets users upload documents and query their content using natural language. Generates formatted PDF reports from AI answers and delivers them via email.

## Features

- **Multi-format Support** — upload PDF, DOCX, and TXT files
- **AI-powered Q&A** — ask questions about document content and get contextual answers
- **PDF Report Generation** — export Q&A results as clean, formatted PDF reports
- **Email Delivery** — send generated reports directly via email
- **Query History** — all queries and responses stored in SQLite

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js + Vite |
| Backend | FastAPI (Python) |
| AI | OpenAI API / AIMLAPI |
| PDF | ReportLab |
| Database | SQLite |
| HTTP | Axios |

## Getting Started

```bash
git clone https://github.com/tanmay0922/smart-file-qa.git
cd smart-file-qa

# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

## How It Works

```
Upload File → Extract Text → AI processes query → Answer returned
                                                        ↓
                                              Generate PDF Report → Email delivery
```

## Author

**Tanmay Upadhyay** — [GitHub](https://github.com/tanmay0922) · [LinkedIn](https://www.linkedin.com/in/tanmay-upadhyay-0b884b203/) · [Portfolio](https://tanmay0922.github.io)
