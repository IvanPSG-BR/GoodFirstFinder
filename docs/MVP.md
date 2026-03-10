# MVP — GoodFirstFinder

## Objetivo

Entregar uma versão funcional e utilizável do GoodFirstFinder: um motor de busca curado de repositórios OSS para desenvolvedores iniciantes, com score de amigabilidade pré-calculado por IA.

---

## Stack do MVP

| Camada      | Tecnologia                          |
|-------------|-------------------------------------|
| API         | FastAPI + Uvicorn                   |
| Auth        | API Key estática (`X-API-Key` header) |
| Banco       | PostgreSQL 16 + SQLAlchemy 2.x async |
| Migrations  | Alembic                             |
| HTTP Client | HTTPX                               |
| LLM         | OpenAI-compatible (via `OPENAI_BASE_URL`) |
| Validação   | Pydantic v2 + pydantic-settings     |
| Ingestão    | Script CLI (`python -m app.ingest`) |
| Containers  | Docker + Docker Compose (2 serviços: `db` + `api`) |
| Testes      | Pytest + pytest-asyncio + aiosqlite |

---

## O que está fora do MVP

| Removido | Motivo |
|---|---|
| Celery + Redis | Overkill para MVP; ingestão via script CLI é suficiente |
| JWT + bcrypt (Auth de usuários) | Sem cadastro de usuários; API Key estática é suficiente |
| Suporte a Ollama | Complexidade especulativa; OpenAI-compatible cobre os casos reais |
| Docker service `worker` | Consequência da remoção do Celery |
| Filtro por tipo de tarefa (bug/docs/feature) | Exige classificação individual por LLM; custo e complexidade sem validação de valor |
| Cursor-based pagination | Offset pagination resolve para o volume do MVP |
| Prometheus + Grafana | Sem SLA comercial; não entrega valor ao usuário final |

---

## Funcionalidades do MVP

### RF-01 — Indexação

- Busca repositórios no GitHub com label `good first issue`
- Aplica pré-filtro de elegibilidade (não arquivado, ativo, ≥2 stars, tem README)
- Armazena metadados: nome, descrição, linguagem, stars, forks, issues abertas, presença de `CONTRIBUTING.md` e `CODE_OF_CONDUCT.md`

### RF-02 — Score de Amigabilidade

- Calcula score total (0–10) como média ponderada de 4 sub-scores:
  - `documentation_score` (30%) — README, CONTRIBUTING.md, CODE_OF_CONDUCT.md
  - `community_score` (20%) — receptividade histórica a PRs de iniciantes
  - `activity_score` (20%) — frequência de commits e respostas em issues
  - `beginner_friendliness_score` (30%) — labels, issues bem descritas, guias de setup
- Armazena justificativa gerada pela IA
- Fallback heurístico se o LLM falhar (`is_ai_scored = false`)

### RF-03 — Busca e Filtros

- Filtros: linguagem, score mínimo/máximo, `has_contributing`, `has_code_of_conduct`, texto livre
- Ordenação padrão por score (decrescente)
- Paginação offset (padrão: 20 itens, máximo: 100)
- Repositórios com `total_score < 3.0` excluídos dos resultados padrão

### RF-04 — Detalhe do Repositório

- Endpoint individual com todos os metadados
- Score completo: total + 4 sub-scores + justificativa da IA

---

## Ingestão de Dados

A ingestão é feita fora do ciclo de request/response da API, via script:

```bash
python -m app.ingest
```

O script:

1. Busca repositórios elegíveis no GitHub
2. Analisa cada um com o LLM
3. Persiste metadados e scores no PostgreSQL

A frequência de execução é responsabilidade do operador (cron, agendador do servidor, execução manual).

---

## Ambiente de Desenvolvimento

```bash
# Subir banco
docker compose up -d db

# Rodar migrations
alembic upgrade head

# Iniciar API
uvicorn app.api.main:app --reload

# Executar ingestão
python -m app.ingest
```

Variáveis de ambiente necessárias: ver `.env.example`.

---

## Critérios de Conclusão do MVP

- [ ] Script de ingestão funcional (busca + score + persistência)
- [ ] Migration inicial criada e aplicável
- [ ] Endpoints de busca e detalhe retornando dados reais
- [ ] Testes unitários cobrindo `calculate_total_score` e `GitHubClient`
- [ ] Testes de integração para `/search` e `/repositories`
- [ ] API acessível via Docker Compose
