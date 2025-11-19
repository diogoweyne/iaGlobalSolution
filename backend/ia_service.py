import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

import json
import re
from datetime import datetime
from openai import OpenAI
from pymongo import MongoClient
import os
from dotenv import load_dotenv




# --------------------------
# OPENAI
# --------------------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------------
# MONGO
# --------------------------
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB_NAME")

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[MONGO_DB]
colecao_trilhas = db["trilhas"]


def limpar_json(texto):
    """
    Limpa qualquer texto vindo antes ou depois do JSON.
    Se a IA gerar código ruim, isso tenta extrair somente o JSON.
    """
    match = re.search(r"\{.*\}", texto, re.DOTALL)
    if match:
        return match.group(0)
    return texto  # fallback


def gerar_trilha_ia(perfil):
    # Normaliza nível (evita bug com acentos)
    nivel_normalizado = (
        perfil.nivel.lower()
        .replace("í", "i")
        .replace("ê", "e")
        .replace("é", "e")
        .replace("â", "a")
        .replace("ã", "a")
        .replace("ç", "c")
    )

    prompt = f"""
Você é um orientador profissional especializado em criar trilhas de carreira.

Gere uma trilha completa para o usuário com base nas informações:

Nome: {perfil.nome}
Área atual: {perfil.area_atual}
Objetivo: {perfil.objetivo_carreira}
Nível atual: {nivel_normalizado}

RETORNE SOMENTE UM JSON VÁLIDO, SEM QUALQUER TEXTO EXPLICATIVO, NO FORMATO:

{{
  "resumo": "texto...",
  "curto_prazo": ["item1", "item2"],
  "medio_prazo": ["item1", "item2"],
  "longo_prazo": ["item1", "item2"],
  "habilidades_chave": ["item1", "item2"]
}}
    """

    # --------------------------
    # CHAMADA À IA
    # --------------------------
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    conteudo = response.choices[0].message.content

    # Remove marcas tipo ```json
    conteudo = conteudo.replace("```json", "").replace("```", "").strip()

    # Limpa texto fora do JSON
    conteudo = limpar_json(conteudo)

    # --------------------------
    # PARSE DO JSON (com fallback)
    # --------------------------
    try:
        trilha = json.loads(conteudo)
    except:
        trilha = {
            "resumo": "Não foi possível gerar a trilha completa, mas criamos um rascunho.",
            "curto_prazo": [],
            "medio_prazo": [],
            "longo_prazo": [],
            "habilidades_chave": []
        }

    # --------------------------
    # SEMPRE SALVA NO MONGO
    # --------------------------
    documento = {
        "perfil": {
            "nome": perfil.nome,
            "area_atual": perfil.area_atual,
            "objetivo_carreira": perfil.objetivo_carreira,
            "nivel": perfil.nivel
        },
        "trilha": trilha,
        "criado_em": datetime.now()
    }

    colecao_trilhas.insert_one(documento)

    # --------------------------
    # RETORNA PARA O FRONT
    # --------------------------
    return trilha
