# 🚀 API Flask com Flasgger

Este projeto é uma API REST desenvolvida com **Flask**, utilizando **Flasgger** para documentação interativa (Swagger) e **PostgreSQL** com Docker.

---

## 📦 Como rodar o projeto

Siga os passos abaixo para executar a aplicação localmente:

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Andreilna/AT1-Api-em-flask-com-flasgger.git
```

### 2️⃣ Acessar a pasta do backend

```bash
cd AT1-Api-em-flask-com-flasgger/apps/backend
```

### 3️⃣ Configurar o arquivo `.env`

Crie um arquivo `.env` com base no `.env.example`:

```bash
cp .env.example .env
```

Depois, edite o `.env` conforme necessário.

---

### 4️⃣ Subir o banco de dados com Docker

```bash
docker compose up -d
```

---

### 5️⃣ Rodar a aplicação Flask

```bash
uv run flask --app src/app run
```

---

## 📚 Acessar a documentação da API

Após iniciar o servidor, acesse:

👉 http://127.0.0.1:5000/apidocs/

Você verá a documentação interativa da API (Swagger), onde é possível testar todas as rotas.

---

## 🛠 Tecnologias utilizadas

* Python
* Flask
* Flasgger (Swagger)
* PostgreSQL
* Docker
* Docker Compose

---

## ✅ Observações

* Certifique-se de que o Docker está rodando antes de executar o `docker compose`.
* O comando `uv run` requer o `uv` instalado no ambiente.
* Todas as rotas da API podem ser testadas diretamente pela interface Swagger.

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos.
