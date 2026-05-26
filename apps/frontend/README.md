# Frontend Flet

Este frontend usa Flet para consumir a API do backend Flask.

## Como executar

1. Ative o ambiente virtual em `apps/frontend`:

```powershell
cd apps/frontend
.\.venv\Scripts\Activate.ps1
```

2. Instale as dependências caso ainda não tenha feito:

```powershell
pip install flet httpx
```

3. Execute o frontend:

```powershell
python main.py
```

> Antes de abrir o frontend, certifique-se de que o backend esteja rodando em `http://127.0.0.1:5000`.
