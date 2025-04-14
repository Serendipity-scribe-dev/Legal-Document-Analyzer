# app/routes/summarizer_routes.py
from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
import os
from app.utils.summarizer_util import generate_summary
from typing import Optional

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/summarizer")
async def summarizer_page(request: Request):
    return templates.TemplateResponse("summarizer.html", {"request": request})

@router.post("/summarizer")
async def summarize_text(
    request: Request,
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    summary = ""
    input_text = ""

    if text:
        input_text = text
    elif file and file.filename.endswith('.txt'):
        contents = await file.read()
        input_text = contents.decode('utf-8')

    if input_text.strip():
        summary = generate_summary(input_text, ratio=0.2)

    return templates.TemplateResponse(
        "summarizer.html",
        {
            "request": request,
            "input_text": input_text,
            "summary": summary
        }
    )