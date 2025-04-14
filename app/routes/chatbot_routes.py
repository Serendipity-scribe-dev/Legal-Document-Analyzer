# app/routes/chatbot_routes.py

import os
from dotenv import load_dotenv
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import google.generativeai as genai

load_dotenv()

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable not set")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

class ChatInput(BaseModel):
    message: str

# Route for rendering the Gemini chatbot UI (HTML page)
@router.get("/chatbot")
def chatbot_ui(request: Request):
    return templates.TemplateResponse("chatbot.html", {"request": request})

# Route for Gemini backend POST requests
@router.post("/chat")
async def chat_with_gemini(input: ChatInput):
    try:
        response = model.generate_content(input.message)
        reply = response.text
        return {"response": reply}
    except Exception as e:
        import traceback
        print("ERROR:", traceback.format_exc())
        return JSONResponse(content={"error": str(e)}, status_code=500)