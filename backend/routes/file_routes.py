# backend/routes/file_routes.py

from fastapi import APIRouter, UploadFile, File, Form
from services.openai_service import process_prompt
from utils.pdf_exporter import generate_pdf
from models.database import save_to_db
from services.email_service import send_pdf_email  # ✅ Ensure this is defined properly

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    email: str = Form(...),
    prompt: str = Form(...)
):
    # Save file to disk
    file_path = f"static/uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # ⛔ Don't use await — process_prompt is now sync
    response = process_prompt(prompt, file_path)

    # Save info to DB
    save_to_db(email, file.filename, prompt, response)

    return {"file": file.filename, "answer": response}


@router.post("/export")
async def export_pdf_and_email(email: str = Form(...)):
    pdf_path = generate_pdf(email)

    # ⛔ Remove await if send_pdf_email is not async
    send_pdf_email(email, pdf_path)

    return {"status": "PDF sent to email", "pdf": pdf_path}
