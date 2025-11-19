from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ia_service import gerar_trilha_ia


# -----------------------------
# MODELO DE DADOS RECEBIDOS
# -----------------------------
class Perfil(BaseModel):
    nome: str
    area_atual: str
    objetivo_carreira: str
    nivel: str


# -----------------------------
# INICIALIZAÇÃO DO FASTAPI
# -----------------------------
app = FastAPI()


# -----------------------------
# CONFIGURAÇÃO DE CORS
# -----------------------------
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# ROTAS
# -----------------------------
@app.get("/")
def raiz():
    return {"status": "API OzConnect online!"}


@app.post("/api/trilhas")
def criar_trilha(perfil: Perfil):
    trilha = gerar_trilha_ia(perfil)
    return trilha
