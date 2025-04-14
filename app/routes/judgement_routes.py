from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from app.models.judgement import JudgementRetriever

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
retriever = JudgementRetriever()

# For loading the search page
@router.get("/judgements")
async def judgement_page(request: Request):
    return templates.TemplateResponse(
        name="judgement_search.html",  # Explicitly name the template
        context={"request": request}   # Explicit context parameter
    )

# For handling search submissions
@router.post("/judgements")
async def handle_search(request: Request, query: str = Form(...)):
    results = retriever.find_similar(query)
    return templates.TemplateResponse(
        name="judgement_search.html",  # Explicit name
        context={
            "request": request,
            "query": query,
            "results": results
        }
    )