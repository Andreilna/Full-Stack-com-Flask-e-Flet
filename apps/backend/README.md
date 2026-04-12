# 🎬 Streaming API - Catálogo de Entretenimento

API REST desenvolvida com Flask para gerenciamento de um catálogo de filmes, séries, atores e gêneros.  
A aplicação utiliza PostgreSQL com Docker e possui documentação interativa via Swagger (Flasgger).

---

## 🚀 Tecnologias Utilizadas

- Python 3.14+
- Flask
- Flasgger (Swagger UI)
- Flask-SQLAlchemy
- Flask-Migrate
- Pydantic v2
- PostgreSQL
- Docker & Docker Compose
- uv (gerenciador de pacotes moderno)

---

## 📂 Estrutura do Projeto

src/
 ├── routes/
 │    ├── movies.py
 │    ├── series.py
 │    ├── actors.py
 │    └── genres.py
 │
 ├── schemas/
 │    ├── movie_schema.py
 │    ├── series_schema.py
 │    ├── actor_schema.py
 │    └── genre_schema.py
 │
 ├── database/
 │    ├── database.py
 │    └── seed.sql
 │
 ├── models.py
 └── app.py

---

## ⚙️ Pré-requisitos

- Python 3.14+
- Docker + Docker Compose
- uv instalado

Instalar o uv (caso não tenha):

pip install uv

---

## 🛠️ Como Rodar o Projeto

### 1. Clone o repositório

git clone <LINK_DO_SEU_REPO>  
cd AT1-Api-em-flask-com-flasgger/apps/backend

---

### 2. Criar ambiente virtual

uv venv

Ativar:

Windows  
.venv\Scripts\activate  

Linux/Mac  
source .venv/bin/activate

---

### 3. Instalar dependências

uv pip install -r requirements.txt  

ou  

uv sync

---

### 4. Configurar variáveis de ambiente

Crie um arquivo .env na raiz:

DATABASE_URL=postgresql://devuser:devpassword@localhost:5432/AT1-Api-em-flask-com-flasgger

---

### 5. Subir o banco de dados (PostgreSQL)

docker-compose up -d

Isso irá:
- Criar o banco automaticamente
- Rodar o seed.sql
- Expor na porta 5432

---

### 6. Rodar a aplicação

uv run flask --app src/app run

---

## 📖 Documentação Swagger

Acesse no navegador:

http://localhost:5000/apidocs

---

## 🔥 Endpoints da API

### 🎥 Movies
GET    /movies  
POST   /movies  
PUT    /movies/{id}  
DELETE /movies/{id}  

### 📺 Series
GET    /series  
POST   /series  
PUT    /series/{id}  
DELETE /series/{id}  

### 🎭 Actors
GET    /actors  
POST   /actors  
PUT    /actors/{id}  
DELETE /actors/{id}  

### 🎬 Genres
GET    /genres  
POST   /genres  
PUT    /genres/{id}  
DELETE /genres/{id}  

---

## 🐳 Docker

Subir container  
docker-compose up -d  

Parar container  
docker-compose down  

Rebuild  
docker-compose up --build  
