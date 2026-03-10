# Progresso do Projeto — GoodFirstFinder

## Status Atual

> **Fase:** Estrutura Base / Scaffolding Inicial

---

## ✅ Concluído

### Infraestrutura

- [x] Estrutura de diretórios do projeto criada
- [x] `docker-compose.yml` com serviços: PostgreSQL e API
- [x] `Dockerfile` para API
- [x] `.env.example` com todas as variáveis necessárias
- [x] `requirements.txt` com dependências do projeto

### Core

- [x] `app/core/config.py` — Pydantic Settings com todas as env vars
- [x] `app/core/database.py` — SQLAlchemy async engine + session factory
- [x] `app/core/logging.py` — Configuração de logs estruturados

### Domínios

- [x] `repositories` — Model, Schema, API, Service, Task (stub)
- [x] `scoring` — Model, Schema, API, Service, Task (stub)
- [x] `search` — Schema, API, Service (query builder)
- [x] `integrations` — GitHubClient, LLMClient, Schemas

### API

- [x] `app/api/main.py` — FastAPI app com CORS e exception handler
- [x] `app/api/router.py` — Inclusão de todos os routers

### Migrations

- [x] `migrations/env.py` — Alembic async configurado
- [x] `migrations/script.py.mako` — Template de migration

### Testes

- [x] `tests/conftest.py` — Fixtures pytest (DB in-memory, client)
- [x] `tests/unit/test_scoring_service.py` — Testes da função `calculate_total_score`
- [x] `tests/unit/test_github_client.py` — Testes do GitHubClient (mocked)
- [x] `tests/integration/test_repos_api.py` — Testes da API de repositórios
- [x] `tests/integration/test_search_api.py` — Testes da API de busca

### Documentação

- [x] `README.md` — Resumo geral do projeto
- [x] `docs/ContextoDeProduto.md`
- [x] `docs/ContextoTecnico.md`
- [x] `docs/RegrasDeNegocio.md`
- [x] `docs/Requisitos.md`
- [x] `docs/Progresso.md`

---

## 🔄 Em Andamento

- [ ] Implementação completa do pipeline de scoring (LLM + heurísticas)
- [ ] Migration inicial do banco de dados
- [ ] Testes de integração com banco PostgreSQL real

---

## 📋 Backlog

### Funcionalidades

- [ ] Seção "Featured" (repositórios mais bem pontuados da semana)
- [ ] Filtro por tipo de tarefa (bug fix, documentation, feature)
- [ ] Detalhe do repositório com justificativa completa da IA
- [ ] Paginação cursor-based para buscas grandes

### Infraestrutura

- [ ] CI/CD (GitHub Actions)
- [ ] Healthcheck endpoints detalhados
- [ ] Métricas (Prometheus + Grafana)
- [ ] Rate limiting na API

### Qualidade

- [ ] Cobertura de testes > 80%
- [ ] Linting com Ruff
- [ ] Type checking com mypy

---

## Histórico

| Data       | Versão | Descrição                              |
|------------|--------|----------------------------------------|
| 2026-02-24 | 0.1.0  | Scaffolding inicial do projeto         |
| 2026-03-10 | 0.2.0  | Remoção de Celery/Redis/Auth/Ollama; stack enxuta |
