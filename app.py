from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


templates = Jinja2Templates(directory=BASE_DIR / "templates")


nomes = ["Ana", "Carlos", "Daniel", "Pedro", "Renato", "Sandro"]


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/")
async def home(request: Request):
    context = {f"Nome_{i}": nome for i, nome in enumerate(nomes, start=1)}
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"context": context},
    )


@app.post("/")
async def add_nome(request: Request, nome: str = Form(...)):
    nomenovo = nome
    if nomenovo:
        nomes.append(nomenovo)

    context = {f"Nome_{i}": nome_item for i, nome_item in enumerate(nomes, start=1)}
    return templates.TemplateResponse( request=request,
        name="index.html",
        context={"context": context},
    )

