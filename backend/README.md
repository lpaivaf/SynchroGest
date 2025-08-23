# SynchroGest - Backend (FastAPI)

Este diretório contém o código-fonte do backend da aplicação SynchroGest, desenvolvido com FastAPI.

## Estrutura do Projeto

```
backend/
├── app/             # Código principal da aplicação (rotas, modelos, schemas, serviços, etc.)
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   ├── utils/
│   └── dependencies/
├── scripts/         # Scripts úteis (ex: criar admin)
│   └── criar_admin.py
├── venv/            # Ambiente virtual Python (não incluído no zip)
├── .env             # Variáveis de ambiente (ex: chave secreta, config. banco de dados)
├── alembic.ini      # Configuração do Alembic para migrações
├── migrations/      # Arquivos de migração do Alembic
└── requirements.txt # Dependências Python
```

## Configuração e Execução

Siga os passos abaixo para configurar e executar o backend em seu ambiente local ou em um servidor.

### Pré-requisitos

*   Python 3.10 ou superior
*   pip (gerenciador de pacotes Python)
*   Um servidor de banco de dados MySQL ou PostgreSQL (recomendado)
*   Opcional: Docker e Docker Compose

### 1. Configurar Ambiente Virtual e Instalar Dependências

Navegue até o diretório `backend` e crie um ambiente virtual:

```bash
cd /caminho/para/synchrogest/backend
python3 -m venv venv
```

Ative o ambiente virtual:

*   No Linux/macOS:
    ```bash
    source venv/bin/activate
    ```
*   No Windows:
    ```bash
    .\venv\Scripts\activate
    ```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do diretório `backend` (copie ou renomeie `.env.example` se existir) e configure as seguintes variáveis:

```dotenv
# Chave secreta para JWT (gere uma chave segura!)
SECRET_KEY=sua_chave_secreta_super_segura_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Configuração do Banco de Dados (exemplo para MySQL)
DATABASE_URL=mysql+pymysql://usuario:senha@host:porta/nome_banco
# Exemplo:
# DATABASE_URL=mysql+pymysql://root:password@localhost:3306/synchrogest_db
```

**Importante:** Substitua os valores de exemplo pelas suas configurações reais do banco de dados e gere uma `SECRET_KEY` forte e única.

### 3. Aplicar Migrações do Banco de Dados

Certifique-se de que o banco de dados configurado no `.env` exista. Execute as migrações para criar as tabelas:

```bash
alembic upgrade head
```

### 4. Criar Usuário Administrador (Opcional, mas recomendado)

Execute o script para criar o primeiro usuário administrador:

```bash
python scripts/criar_admin.py
```

Siga as instruções no terminal para definir o email e a senha do administrador.

### 5. Executar o Servidor

Inicie o servidor FastAPI com Uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

*   `--host 0.0.0.0`: Permite acesso de outras máquinas na rede.
*   `--port 8000`: Define a porta em que o servidor rodará.
*   `--reload`: Reinicia o servidor automaticamente ao detectar alterações no código (útil para desenvolvimento).

O backend estará acessível em `http://localhost:8000` (ou o IP da sua máquina na porta 8000).

## Frontend

O frontend React correspondente está implantado separadamente. Certifique-se de que a variável de ambiente `REACT_APP_API_URL` no frontend (ou a configuração do proxy) aponte para a URL onde o backend está rodando (ex: `http://localhost:8000/api`).

