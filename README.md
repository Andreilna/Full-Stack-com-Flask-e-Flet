# 🎬 Streaming API - Catálogo de Entretenimento

Este projeto é uma API desenvolvida em Flask para gerenciamento de um catálogo de filmes, séries, atores e gêneros. A aplicação utiliza Docker para o banco de dados e Flasgger para a documentação interativa via Swagger.

## 🚀 Tecnologias Utilizadas

* **Python 3.12+** (Gerenciador de pacotes `uv`)
* **Flask** (Framework Web)
* **Flasgger** (Documentação Swagger)
* **SQLAlchemy** (ORM para banco de dados)
* **Pydantic v2** (Validação de Schemas)
* **MySQL/MariaDB** (Banco de Dados)
* **Docker & Docker Compose** (Containerização)

## 📂 Estrutura de Pastas (4 Blueprints)

A API está dividida nos seguintes módulos:
1.  **Movies**: Gerenciamento de filmes.
2.  **Series**: Gerenciamento de séries.
3.  **Actors**: Gerenciamento de atores e atrizes.
4.  **Genres**: Gerenciamento de categorias/gêneros.

Cada módulo possui as operações de **GET, POST, PUT e DELETE**.

## 🛠️ Como Rodar o Projeto

### 1. Clonar o Repositório
```bash
git clone <LINK_DO_SEU_REPO>
cd AT1-Api-em-flask-com-flasgger/apps/backend