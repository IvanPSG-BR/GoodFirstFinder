# GoodFirstFinder 🔍

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

### Plano de Fundo (Assíncrono)
1. **Extração:** Varredura de repositórios via API do GitHub.
2. **Pré-filtro:** Descarte de projetos abandonados ou sem arquivos básicos.
3. **Curadoria IA:** Análise semântica de documentação, histórico de PRs e issues.
4. **Indexação:** Salvamento do Score de Amigabilidade e metadados para consulta.

### No Momento (Síncrono)
1. **Filtros:** Usuário aplica filtros (Linguagem, Nível, Tipo de Tarefa).
2. **Consulta:** Busca no índice pré-curado — sem chamadas de IA em tempo real.
3. **Exibição:** Resultados instantâneos ordenados pelo Score.
4. **Detalhe:** Justificativas da IA exibidas por repositório.

## Stack Tecnológica

| Camada       | Tecnologia                          |
|--------------|-------------------------------------|
| API          | FastAPI + Uvicorn                   |
| Banco        | PostgreSQL + SQLAlchemy (Async)     |
| Tarefas      | Celery + Redis                      |
| IA / LLM     | OpenAI / Ollama (via HTTPX)         |
| Migrations   | Alembic                             |
| Containers   | Docker + Docker Compose             |
| Testes       | Pytest + pytest-asyncio             |

## Estrutura do Projeto

```
good-first-finder/
├── app/
│   ├── core/           # Configurações globais (settings, DB, Celery, logging)
│   ├── common/         # Entidades compartilhadas (models base, schemas, exceções)
│   ├── modules/        # Domínios de negócio
│   │   ├── repositories/   # CRUD de repositórios Open Source
│   │   ├── scoring/        # Cálculo do Score de Amigabilidade
│   │   ├── search/         # Busca e filtros
│   │   └── integrations/   # Clientes GitHub API e LLM
│   └── api/            # Entry point FastAPI
├── worker/             # Entry point Celery
├── migrations/         # Alembic (versionamento de banco)
├── tests/              # Testes automatizados (unit + integration)
├── docker/             # Dockerfiles específicos
├── docs/               # Documentação do projeto
├── docker-compose.yml
├── uv.toml
└── .env.example
```

## Início Rápido

```bash
# 1. Copie o arquivo de variáveis de ambiente
cp .env.example .env

# 2. Suba os serviços com Docker Compose
docker compose up --build

# 3. Execute as migrations
docker compose exec api alembic upgrade head

# 4. Acesse a documentação interativa
# http://localhost:8000/docs
```

## Documentação

Consulte o diretório [`docs/`](./docs/) para:
- [Contexto de Produto](./docs/ContextoDeProduto.md)
- [Contexto Técnico](./docs/ContextoTecnico.md)
- [Regras de Negócio](./docs/RegrasDeNegocio.md)
- [Requisitos](./docs/Requisitos.md)
- [Progresso](./docs/Progresso.md)

## Licença

Veja o arquivo [LICENSE](./LICENSE) para detalhes.
