from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.routes.ipc_routes import router as ipc_router
from app.routes.summarizer_routes import router as summarizer_router
from app.routes.judgement_routes import router as judgement_router   # 👈 added
#chatbot
from app.routes.chatbot_routes import router as chatbot_router

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Include routers
app.include_router(ipc_router)
app.include_router(summarizer_router) 
app.include_router(judgement_router) # 👈 added
app.include_router(chatbot_router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
