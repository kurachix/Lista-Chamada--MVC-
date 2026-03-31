from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")


templates = Jinja2Templates(directory=BASE_DIR / "templates")


nomes = {
    "Nome_1": "Ana",
    "Nome_2": "Carlos",
    "Nome_3": "Daniel",
    "Nome_4": "Pedro",
    "Nome_5": "Renato",
    "Nome_6": "Sandro",
}


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"context": nomes},
    )


@app.post("/")
async def add_nome(request: Request, nome: str = Form(...)):
    if nome:
        novo_id = len(nomes) + 1
        nomes[f"Nome_{novo_id}"] = nome

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"context": nomes},
    )

