import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def gerar_trilha_ia(perfil):
    prompt = f"""
Você é um orientador profissional especializado em criar trilhas de carreira.

Gere uma trilha completa para o usuário com base nas informações:

Nome: {perfil.nome}
Área atual: {perfil.area_atual}
Objetivo: {perfil.objetivo_carreira}
Nível atual: {perfil.nivel}

RETORNE SOMENTE UM JSON VÁLIDO, SEM QUALQUER TEXTO EXPLICATIVO, NO FORMATO:

{{
  "resumo": "texto...",
  "curto_prazo": ["item1", "item2", ...],
  "medio_prazo": ["item1", "item2", ...],
  "longo_prazo": ["item1", "item2", ...],
  "habilidades_chave": ["item1", "item2", ...]
}}

O JSON deve ser sempre válido, sem emojis e sem comentários.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    conteudo = response.choices[0].message.content

    print("\n===== RESPOSTA BRUTA DA OPENAI =====")
    print(conteudo)
    print("====================================\n")

    # Se vier código markdown, removemos
    conteudo = conteudo.replace("```json", "").replace("```", "").strip()

    try:
        trilha = json.loads(conteudo)
    except json.JSONDecodeError:
        print("ERRO: IA não retornou JSON válido.")
        return {
            "resumo": "Não foi possível gerar a trilha.",
            "curto_prazo": [],
            "medio_prazo": [],
            "longo_prazo": [],
            "habilidades_chave": []
        }

    return trilha
