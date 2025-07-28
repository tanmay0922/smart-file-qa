# 🧠 Smart File QA

Smart File QA is a full-stack web application that enables users to **upload files (PDF, DOCX, TXT)** and ask intelligent questions about their content using an AI model. It processes uploaded files, provides responses, and even allows exporting the result as a PDF and emailing it—all in one seamless experience.

---

## 🚀 Features

- 📤 Upload files (`.pdf`, `.txt`, `.docx`)
- 🤖 Ask questions and get contextual AI-generated answers
- 📩 Enter email address to receive a downloadable PDF of responses
- 🧾 Auto-generates clean and readable answer PDFs
- 📬 Sends the report directly to your email
- 💾 Stores history in SQLite (can be extended)

---

## 🧱 Tech Stack

### 💻 Frontend:
- React.js
- Axios
- Vite
- HTML/CSS (minimal)

### ⚙️ Backend:
- FastAPI (Python)
- OpenAI / AIMLAPI (pluggable)
- ReportLab (for PDF generation)
- SQLite (for logging queries)

---

## 📁 Folder Structure

smart-file-qa/
│
├── backend/

│ ├── main.py # FastAPI app entry

│ ├── routes/ # Upload & export routes

│ ├── services/ # AI service integration

│ ├── utils/ # PDF generation, email

│ └── qa_data.db # SQLite database

│
├── frontend/

│ ├── src/

│ │ ├── components/ # Upload form

│ │ ├── pages/ # Home page

│ │ └── services/ # Axios API calls

│ └── public/

│
└── requirements.txt # Backend Python dependencies
## 🧪 How to Run Locally

### ✅ Backend

cd backend

pip install -r requirements.txt

uvicorn main:app --reload


✅ Frontend
cd frontend

npm install

npm run dev


Note
This repo does not include the .venv folder to keep it clean and lightweight.

API keys should be set via environment variables or .env files (not hardcoded).

AIMLAPI/OpenAI usage may require API key verification.

.

📬 Contact
Built by: Tanmay Upadhyay

Images:
UI:
<img width="1919" height="833" alt="image" src="https://github.com/user-attachments/assets/c7ab28f0-8bbd-4672-903c-4fb3bb03f417" />
FastAPi Doc:
<img width="1919" height="958" alt="image" src="https://github.com/user-attachments/assets/ff437939-38eb-464e-9a20-bfdfe670d3f3" />






