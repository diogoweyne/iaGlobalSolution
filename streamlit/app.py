import streamlit as st
import requests

st.set_page_config(page_title="OzConnect IA", page_icon="🌐", layout="centered")

st.markdown("""
# OzConnect IA  
### Gerador Inteligente de Trilhas de Carreira  
""")

nome = st.text_input("Seu nome")
area = st.text_input("Área atual")
objetivo = st.text_input("Objetivo de carreira")
nivel = st.selectbox("Seu nível atual", ["Iniciante", "Intermediário", "Avançado"])

if st.button("Gerar Trilha"):
    dados = {
        "nome": nome,
        "area_atual": area,
        "objetivo_carreira": objetivo,
        "nivel": nivel
    }

    resp = requests.post("http://127.0.0.1:8000/api/trilhas", json=dados)

    if resp.status_code == 200:
        trilha = resp.json()

        st.markdown("## Resumo da Trilha")
        st.write(trilha.get("resumo", ""))

        st.markdown("## Objetivos de Curto Prazo")
        for item in trilha.get("curto_prazo", []):
            st.markdown(f"- {item}")

        st.markdown("## Objetivos de Médio Prazo")
        for item in trilha.get("medio_prazo", []):
            st.markdown(f"- {item}")

        st.markdown("## Objetivos de Longo Prazo")
        for item in trilha.get("longo_prazo", []):
            st.markdown(f"- {item}")

        st.markdown("## Habilidades-Chave")
        for item in trilha.get("habilidades_chave", []):
            st.markdown(f"- {item}")

    else:
        st.error("Erro ao gerar trilha. Verifique o backend.")
