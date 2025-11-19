# 🌐 OzConnect IA — Gerador Inteligente de Trilhas de Carreira

## 🧩 Problema

O mercado de trabalho está em constante mudança, e muitos profissionais têm dificuldade em identificar **qual caminho seguir** para evoluir na carreira.  
Mesmo com abundância de cursos e conteúdos, falta **clareza**, **priorização** e **direcionamento personalizado**.

Isso gera:
- indecisão,
- escolhas aleatórias,
- desperdício de tempo,
- e dificuldade em alcançar o objetivo profissional desejado.

---

## 💡 Nossa Solução — OzConnect IA

O **OzConnect IA** foi criado para resolver exatamente esse problema.

Utilizando **Inteligência Artificial**, o sistema gera **trilhas de carreira totalmente personalizadas**, com base no perfil do usuário.  
A solução analisa:

- Nome  
- Área atual  
- Objetivo profissional  
- Nível de experiência  

E produz automaticamente uma trilha contendo:

- ✔ Resumo do plano  
- ✔ Objetivos de curto prazo  
- ✔ Objetivos de médio prazo  
- ✔ Objetivos de longo prazo  
- ✔ Habilidades-chave a desenvolver  

Tudo isso é exibido no **frontend em Streamlit** e armazenado no **MongoDB Atlas**, permitindo histórico e evolução futura.

---

# 📁 Estrutura do Projeto

```
globalSolution_ia/
│
├── backend/
│   ├── main.py
│   ├── ia_service.py
│   ├── mongodb_service.py
│   ├── requirements.txt
│   └── .env  (não vai para o GitHub)
│
├── streamlit/
│   ├── app.py
│
└── README.md
```

---

# ⚙️ Tecnologias Utilizadas

### **Backend**
- FastAPI  
- Uvicorn  
- OpenAI API  
- pymongo  
- python-dotenv  

### **Frontend**
- Streamlit  
- Requests  

### **Banco de Dados**
- MongoDB  

---

# 🔑 Variáveis de Ambiente (.env)

Dentro da pasta **backend**, crie o arquivo:

```
OPENAI_API_KEY=SEU_TOKEN_AQUI
MONGO_URI="sua-string-de-conexao"
MONGO_DB_NAME="ozconnect"
```

# ▶️ Como rodar o Backend (FastAPI)

Abra o terminal na raiz do projeto:

```bash
cd backend
```

Ative o ambiente virtual:

```bash
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o servidor:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Documentação Swagger:

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Como rodar o Frontend (Streamlit)

Abra outro terminal:

```bash
cd streamlit
```

Execute o Streamlit:

```bash
streamlit run app.py
```

O frontend ficará disponível em:

```
http://localhost:8501
```

---

# 🗂️ Salvando no MongoDB

Toda trilha gerada é salva na collection:

```
Database: ozconnect
Collection: trilhas
```

Cada documento inclui:

```json
{
  "usuario": {
    "nome": "...",
    "area_atual": "...",
    "objetivo": "...",
    "nivel": "..."
  },
  "trilha": {
    "resumo": "...",
    "curto_prazo": ["..."],
    "medio_prazo": ["..."],
    "longo_prazo": ["..."],
    "habilidades_chave": ["..."]
  },
  "timestamp": "2025-11-19T12:00:00"
}
```

---

# 🧪 Testes via Swagger

Acesse:

```
http://127.0.0.1:8000/docs
```

# 👨‍💻 Autores

**Diogo Weyne - RM558380**

**Gustavo Tonato - RM555393**

**João Victor de Souza - RM555290**  

FIAP — DISRUPTIVE ARCHITECTURES: IOT, IOB & GENERATIVE IA | OzConnect  

