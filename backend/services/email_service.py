# backend/services/email_service.py

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi_mail.email_utils import DefaultChecker
from pydantic import EmailStr
from pathlib import Path

conf = ConnectionConfig(
    MAIL_USERNAME="your_email@gmail.com",
    MAIL_PASSWORD="your_app_password",
    MAIL_FROM="your_email@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,   # ✅ new key for TLS
    MAIL_SSL_TLS=False,   # ✅ new key for SSL
    USE_CREDENTIALS=True,
)


async def send_pdf_email(email: EmailStr, file_path: str):
    file_name = Path(file_path).name

    message = MessageSchema(
        subject="Your Smart File QA Report",
        recipients=[email],
        body=f"Hi,\n\nAttached is your generated QA PDF from Smart File QA.\n\nThank you!",
        subtype="plain",
        attachments=[file_path],
    )

    fm = FastMail(conf)
    await fm.send_message(message)
