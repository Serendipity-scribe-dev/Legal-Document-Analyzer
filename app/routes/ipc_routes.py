from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.models.ipc_model import search_ipc

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

class IPCQuery(BaseModel):
    query: str

# ✅ Route to render the IPC search page
@router.get("/ipc")
def render_ipc_page(request: Request):
    return templates.TemplateResponse("ipc_search.html", {"request": request})

@router.post("/search")
def search_ipc_route(data: IPCQuery):
    return {"results": search_ipc(data.query)}
