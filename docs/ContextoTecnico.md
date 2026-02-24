# Contexto Técnico — GoodFirstFinder

## Stack Principal

| Camada         | Tecnologia                              | Justificativa                                    |
|----------------|-----------------------------------------|--------------------------------------------------|
| API            | **FastAPI** + Uvicorn                   | Alto desempenho, async-first, OpenAPI automático |
| ORM / Banco    | **SQLAlchemy 2.x (async)** + PostgreSQL | Type-safe, async nativo, migrations com Alembic  |
| Task Queue     | **Celery** + Redis                      | Processamento assíncrono robusto e escalável     |
| HTTP Client    | **HTTPX**                               | Async/sync, ideal para GitHub API e LLMs         |
| IA / LLM       | **OpenAI API** / **Ollama** (HTTPX)     | Flexível: nuvem ou local                         |
| Migrations     | **Alembic**                             | Versionamento de schema integrado ao SQLAlchemy  |
| Validação      | **Pydantic v2**                         | Schemas rápidos, type-safe, integrados ao FastAPI|
| Configuração   | **pydantic-settings**                   | Env vars validadas com type safety               |
| Containers     | **Docker** + Docker Compose             | Ambiente reproduzível de desenvolvimento         |
| Testes         | **Pytest** + pytest-asyncio             | Padrão Python, suporte async, fixtures poderosas |

## Arquitetura

### Fluxo Assíncrono (Background)

```
GitHub API ──► GitHubClient ──► Celery Task (fetch_repo_data)
                                      │
                                      ▼
                              Pre-filter (Regras Booleanas)
                                      │
                                      ▼
                              LLMClient (analyze_repository)
                                      │
                                      ▼
                              Score calculado e salvo no PostgreSQL
```

### Fluxo Síncrono (Request/Response)

```
Usuário ──► GET /api/v1/search?language=Python&min_score=7
                │
                ▼
        SearchService (query builder)
                │
                ▼
        PostgreSQL (índice pré-curado)
                │
                ▼
        SearchResponse (JSON) ──► Usuário
```

## Estrutura de Módulos

```
app/
├── core/           # Configurações globais (Settings, DB, Celery, Logging, Security)
├── common/         # Modelos base, schemas Pydantic base, exceções customizadas
├── modules/
│   ├── repositories/   # CRUD de repositórios (Model, Schema, API, Service, Task)
│   ├── scoring/        # Score de Amigabilidade (Model, Schema, API, Service, Task)
│   ├── search/         # Busca e filtros (Schema, API, Service)
│   └── integrations/   # Clientes externos (GitHub, LLM)
└── api/            # FastAPI app + router principal
```

## Banco de Dados

### Tabelas Principais

#### `repositories`
| Coluna              | Tipo       | Descrição                          |
|---------------------|------------|------------------------------------|
| id                  | UUID (PK)  | Identificador interno              |
| github_id           | INTEGER    | ID único do GitHub                 |
| full_name           | VARCHAR    | `owner/repo`                       |
| language            | VARCHAR    | Linguagem principal                |
| stars_count         | INTEGER    | Número de stars                    |
| has_contributing    | BOOLEAN    | Possui CONTRIBUTING.md             |
| has_code_of_conduct | BOOLEAN    | Possui CODE_OF_CONDUCT.md          |
| is_archived         | BOOLEAN    | Repositório arquivado              |
| is_active           | BOOLEAN    | Ativo na plataforma                |
| created_at          | TIMESTAMPTZ| Data de criação                    |
| updated_at          | TIMESTAMPTZ| Última atualização                 |

#### `scores`
| Coluna                      | Tipo      | Descrição                          |
|-----------------------------|-----------|-----------------------------------|
| id                          | UUID (PK) | Identificador interno             |
| repository_id               | UUID (FK) | Referência ao repositório         |
| total_score                 | FLOAT     | Score total (0–10)                |
| documentation_score         | FLOAT     | Sub-score documentação            |
| community_score             | FLOAT     | Sub-score comunidade              |
| activity_score              | FLOAT     | Sub-score atividade               |
| beginner_friendliness_score | FLOAT     | Sub-score para iniciantes         |
| justification               | TEXT       | Justificativa gerada pela IA      |

## Decisões de Arquitetura

1. **Módulos por domínio:** Cada módulo contém seu próprio `models.py`, `schemas.py`, `api.py`, `services.py` e `tasks.py`. Facilita escalabilidade e manutenção.
2. **IA nos bastidores:** LLM chamada apenas em tasks Celery (assíncronas), nunca no request path do usuário.
3. **Score pré-calculado:** A consulta de busca opera sobre scores já persistidos no banco — sem latência de IA em tempo real.
4. **SQLite em testes:** Uso de `aiosqlite` para testes rápidos sem necessidade de PostgreSQL rodando.
