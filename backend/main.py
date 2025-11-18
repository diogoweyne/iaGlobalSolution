from fastapi import FastAPI
from pydantic import BaseModel
from ia_service import gerar_trilha_ia
from fastapi.middleware.cors import CORSMiddleware

class Perfil(BaseModel):
    nome: str
    area_atual: str
    objetivo_carreira: str
    nivel: str

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def raiz():
    return {"status": "API OzConnect online!"}

@app.post("/api/trilhas")
def criar_trilha(perfil: Perfil):
    trilha = gerar_trilha_ia(perfil)
    return trilha
