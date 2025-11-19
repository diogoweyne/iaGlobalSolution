import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# 📌 Lê variáveis do .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "ozconnect")

# 📌 Conexão com o MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# 📌 Collection onde vamos salvar as trilhas
trilhas_collection = db["trilhas"]

def salvar_trilha(perfil, trilha_gerada):
    """
    Salva a trilha gerada no MongoDB.
    """
    dado = {
        "nome": perfil.nome,
        "area_atual": perfil.area_atual,
        "objetivo_carreira": perfil.objetivo_carreira,
        "nivel": perfil.nivel,
        "trilha": trilha_gerada
    }

    resultado = trilhas_collection.insert_one(dado)
    return str(resultado.inserted_id)

def listar_trilhas():
    """
    Retorna todas as trilhas salvas.
    """
    trilhas = list(trilhas_collection.find({}, {"_id": 0}))  # remove o _id
    return trilhas
