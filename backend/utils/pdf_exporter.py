# backend/utils/pdf_exporter.py

from fpdf import FPDF
import sqlite3
import os

def generate_pdf(email):
    conn = sqlite3.connect("qa_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT filename, prompt, answer, timestamp FROM qa_data WHERE email = ?", (email,))
    rows = cursor.fetchall()

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Smart File QA Summary", ln=1, align="C")

    for row in rows:
        filename, prompt, answer, timestamp = row
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, f"\nFile: {filename}\nPrompt: {prompt}\nAnswer: {answer}\nTimestamp: {timestamp}\n")

    output_path = f"static/{email.replace('@', '_')}_qa_summary.pdf"
    pdf.output(output_path)
    return output_path
