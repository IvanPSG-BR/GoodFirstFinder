# GoodFirstFinder

> Engine de busca curada para facilitar a contribuição Open Source por desenvolvedores Júniores.

## Sobre o Projeto

O **GoodFirstFinder** é uma plataforma que ajuda desenvolvedores Júniores e Estagiários a encontrar projetos Open Source ideais para sua primeira contribuição. Em vez de navegar por um mar de repositórios, o sistema pré-analisa e classifica projetos por um **Score de Amigabilidade ao Contribuidor**, tornando a descoberta mais simples e menos intimidadora.

## Problema Resolvido

- **Ruído na busca:** Muitos repositórios, difíceis de filtrar por relevância real para iniciantes.
- **Medo de rejeição:** Projetos com baixa receptividade desanimam primeiros contribuidores.
- **Documentação pobre:** Falta de guias de setup e contribuição claros.
- **Falta de orientação:** Dificuldade em saber por onde começar.

## Público-Alvo

Desenvolvedores Júniores (foco inicial em BR, sem barreira de idioma inglês técnico).

## Como Funciona

### Ingestão (script CLI)

1. **Extração:** Varredura de repositórios via API do GitHub.
2. **Pré-filtro:** Descarte de projetos arquivados, inativos ou sem documentação mínima.
3. **Curadoria IA:** Análise semântica via LLM — gera score e justificativa por repositório.
4. **Indexação:** Score de Amigabilidade e metadados salvos no PostgreSQL.

### Consulta (API)

1. **Filtros:** Linguagem, score mínimo/máximo, presença de docs, busca textual.
2. **Consulta:** Busca no índice pré-curado — sem chamadas de IA em tempo real.
3. **Resultados:** Paginados e ordenados pelo Score (decrescente).
4. **Detalhe:** Justificativa da IA acessível por repositório individual.

## Stack Tecnológica

| Camada       | Tecnologia                              |
|--------------|-----------------------------------------|
| API          | FastAPI + Uvicorn                       |
| Auth         | API Key estática (`X-API-Key` header)   |
| Banco        | PostgreSQL 16 + SQLAlchemy 2.x (async)  |
| Ingestão     | Script CLI (`python -m app.ingest`)     |
| IA / LLM     | OpenAI-compatible (via `OPENAI_BASE_URL`) |
| Migrations   | Alembic                                 |
| Containers   | Docker + Docker Compose                 |
| Testes       | Pytest + pytest-asyncio                 |

## Estrutura do Projeto

```
GoodFirstFinder/
├── app/
│   ├── core/           # Configurações globais (settings, DB, logging, auth)
│   ├── common/         # Entidades compartilhadas (models base, schemas, exceções)
│   ├── modules/        # Domínios de negócio
│   │   ├── repositories/   # CRUD de repositórios Open Source
│   │   ├── scoring/        # Cálculo do Score de Amigabilidade
│   │   ├── search/         # Busca e filtros
│   │   └── integrations/   # Clientes GitHub API e LLM
│   └── api/            # Entry point FastAPI
├── migrations/         # Alembic (versionamento de banco)
├── tests/              # Testes automatizados (unit + integration)
├── docker/             # Dockerfile da API
├── docs/               # Documentação do projeto
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

## Início Rápido

```bash
# 1. Copie e preencha as variáveis de ambiente
cp .env.example .env

# 2. Suba os serviços (PostgreSQL + API)
docker compose up --build

# 3. Execute as migrations
docker compose exec api alembic upgrade head

# 4. Rode a ingestão inicial de repositórios
docker compose exec api python -m app.ingest

# 5. Acesse a documentação interativa
# http://localhost:8000/docs
```

## Autenticação

A API não é pública. Todos os endpoints sob `/api/v1/` exigem o header:

```
X-API-Key: <valor configurado em API_KEY>
```

Em desenvolvimento local, deixe `API_KEY` vazio no `.env` para desabilitar a autenticação.

Para gerar uma key segura:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## Documentação

Consulte o diretório [`docs/`](./docs/) para:

- [MVP](./docs/MVP.md)
- [Contexto de Produto](./docs/ContextoDeProduto.md)
- [Contexto Técnico](./docs/ContextoTecnico.md)
- [Regras de Negócio](./docs/RegrasDeNegocio.md)
- [Requisitos](./docs/Requisitos.md)
- [Progresso](./docs/Progresso.md)

## Licença

Veja o arquivo [LICENSE](./LICENSE) para detalhes.
