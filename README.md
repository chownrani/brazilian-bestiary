# 🇧🇷 Bestiário Brasileiro API

Uma API RESTful para catalogar e gerenciar criaturas do folclore brasileiro, desenvolvida com FastAPI e SQLAlchemy.

## 📋 Sobre o Projeto

O **Bestiário Brasileiro** é uma aplicação que permite gerenciar informações sobre criaturas míticas e folclóricas do Brasil, organizadas por região e nível de periculosidade. A API oferece endpoints completos para criar, listar, atualizar e remover criaturas do banco de dados.

### ✨ Funcionalidades

- ✅ **CRUD completo** de criaturas folclóricas
- 🌎 **Categorização por região** (Norte, Nordeste, Centro-Oeste, Sudeste, Sul)
- ⚡ **Busca por ID ou nome** da criatura
- 📊 **Sistema de periculosidade** (escala de 1 a 5)
- 🐳 **Containerização com Docker**
- 🧪 **Testes automatizados** com pytest
- 📚 **Documentação automática** com Swagger/OpenAPI

## 🛠️ Tecnologias Utilizadas

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para Python
- **[Alembic](https://alembic.sqlalchemy.org/)** - Migrações de banco de dados
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Validação de dados
- **[SQLite](https://www.sqlite.org/)** - Banco de dados (padrão)
- **[pytest](https://pytest.org/)** - Framework de testes
- **[Docker](https://www.docker.com/)** - Containerização

## 🚀 Como Executar

### Pré-requisitos

- Python 3.13+
- Docker e Docker Compose (opcional)

### 🐍 Execução Local

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd bestiario-brasileiro
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
```bash
# Crie um arquivo .env na raiz do projeto
echo "DATABASE_URL=sqlite+aiosqlite:///database.db" > .env
```

5. **Execute as migrações**
```bash
alembic upgrade head
```

6. **Inicie a aplicação**
```bash
python app/main.py
```

A API estará disponível em: http://localhost:8000

### 🐳 Execução com Docker

1. **Build e execute com Docker Compose**
```bash
docker-compose up --build
```

A API estará disponível em: http://localhost:8000

## 📖 Documentação da API

Após executar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 🔗 Endpoints Principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/criaturas/` | Criar uma nova criatura |
| `GET` | `/criaturas/` | Listar todas as criaturas |
| `GET` | `/criaturas/id/{id}` | Buscar criatura por ID |
| `GET` | `/criaturas/nome/{nome}` | Buscar criatura por nome |
| `PUT` | `/criaturas/id/{id}` | Atualizar criatura por ID |
| `PUT` | `/criaturas/nome/{nome}` | Atualizar criatura por nome |
| `DELETE` | `/criaturas/id/{id}` | Deletar criatura por ID |
| `DELETE` | `/criaturas/nome/{nome}` | Deletar criatura por nome |

### 📝 Exemplo de Payload

```json
{
  "nome": "Curupira",
  "regiao": "Norte",
  "periculosidade": 4,
  "lenda": "Protetor das florestas amazônicas, possui os pés virados para trás para confundir caçadores e exploradores que tentam destruir a natureza."
}
```

### 🌎 Regiões Disponíveis

- `Norte`
- `Nordeste`
- `Centro-Oeste`
- `Sudeste`
- `Sul`

## 🏗️ Arquitetura do Projeto

```
app/
├── config/          # Configurações da aplicação
├── database/        # Conexão e configuração do banco
├── exceptions/      # Exceções customizadas
├── models/          # Modelos SQLAlchemy
├── repositories/    # Camada de acesso a dados
├── routers/         # Definição das rotas da API
├── schemas/         # Schemas Pydantic para validação
├── services/        # Lógica de negócio
└── main.py         # Ponto de entrada da aplicação

alembic/            # Migrações do banco de dados
tests/              # Testes automatizados
```

### 🎯 Padrões Utilizados

- **Repository Pattern** - Abstração da camada de dados
- **Service Layer** - Lógica de negócio centralizada
- **Dependency Injection** - Injeção de dependências com FastAPI
- **Clean Architecture** - Separação clara de responsabilidades

## 🧪 Testes

Execute os testes com:

```bash
# Todos os testes
pytest -s -v

# Com coverage
pytest --cov=app

# Testes específicos
pytest tests/services/
pytest tests/repositories/
pytest tests/routers/
```

### 📊 Cobertura de Testes

Os testes cobrem:
- ✅ Repositories (acesso a dados)
- ✅ Services (lógica de negócio)
- ✅ Routes (endpoints da API)
- ✅ Casos de sucesso e falha
- ✅ Validações de dados

## 🗄️ Banco de Dados

### Migrações

```bash
# Criar nova migração
alembic revision --autogenerate -m "descrição da mudança"

# Aplicar migrações
alembic upgrade head

# Reverter migração
alembic downgrade -1
```

### Modelo de Dados

**Tabela: criaturas**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer | Chave primária |
| `nome` | String(50) | Nome da criatura (único) |
| `regiao` | String(20) | Região do Brasil |
| `periculosidade` | Integer | Nível de 1 a 5 |
| `lenda` | Text | História/lenda da criatura |

## 📄 Licença

Este projeto está sob a licença GPL v3. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🎭 Exemplos de Criaturas

Algumas criaturas que podem ser catalogadas:

- **Curupira** (Norte) - Protetor das florestas
- **Boto-cor-de-rosa** (Norte) - Encanta pessoas às margens dos rios
- **Mula-sem-cabeça** (Sudeste) - Aparece nas noites de quinta-feira
- **Caipora** (Centro-Oeste) - Protetor dos animais
- **Iara** (Norte/Nordeste) - Sereia dos rios brasileiros

---

Desenvolvido com ❤️ para preservar as lendas do folclore brasileiro
