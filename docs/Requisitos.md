# Requisitos — GoodFirstFinder

## Requisitos Funcionais

### RF-01: Indexação de Repositórios

- **RF-01.1:** O sistema deve buscar repositórios públicos do GitHub via API.
- **RF-01.2:** O sistema deve aplicar um pré-filtro automático para descartar repositórios inelegíveis (arquivados, sem atividade, forks).
- **RF-01.3:** O sistema deve armazenar metadados de cada repositório: nome, descrição, linguagem, URL, estrelas, forks, issues abertas.
- **RF-01.4:** O sistema deve verificar a existência de `CONTRIBUTING.md` e `CODE_OF_CONDUCT.md`.

### RF-02: Cálculo do Score de Amigabilidade

- **RF-02.1:** O sistema deve calcular um Score de Amigabilidade para cada repositório elegível.
- **RF-02.2:** O score deve ser composto por quatro sub-scores: documentação, comunidade, atividade e amigabilidade para iniciantes.
- **RF-02.3:** O sistema deve armazenar a justificativa gerada pela IA para cada score.
- **RF-02.4:** O cálculo de score deve ocorrer via script de ingestão (`python -m app.ingest`), fora do ciclo de request/response da API.

### RF-03: Busca e Filtros

- **RF-03.1:** O sistema deve permitir busca de repositórios por linguagem de programação.
- **RF-03.2:** O sistema deve permitir filtrar por score mínimo e máximo.
- **RF-03.3:** O sistema deve permitir filtrar por presença de CONTRIBUTING.md e CODE_OF_CONDUCT.md.
- **RF-03.4:** O sistema deve permitir busca textual por nome e descrição do repositório.
- **RF-03.5:** Os resultados devem ser ordenados por score (decrescente) por padrão.
- **RF-03.6:** O sistema deve suportar paginação nos resultados de busca.

### RF-04: Detalhe do Repositório

- **RF-04.1:** O sistema deve retornar todos os metadados de um repositório individual por ID.
- **RF-04.2:** O sistema deve retornar o score detalhado (total + sub-scores + justificativa) por ID de repositório.

### RF-05: Seção Featured

- **RF-05.1:** O sistema deve expor os 3 repositórios com maior score como "featured".
- **RF-05.2:** A seção Featured é obtida via query padrão (`ORDER BY total_score DESC LIMIT 3`), sem lógica separada no backend.

---

## Requisitos Não Funcionais

### RNF-01: Performance

- **RNF-01.1:** O tempo de resposta das endpoints de busca deve ser inferior a **500ms** (p95) em condições normais.
- **RNF-01.2:** A API deve suportar pelo menos **100 requisições por segundo** (single instance).

### RNF-02: Disponibilidade

- **RNF-02.1:** O serviço deve ter disponibilidade de **99.5%** mensalmente.
- **RNF-02.2:** Em caso de falha na conexão com o banco, a API deve retornar erro `503` com mensagem clara.

### RNF-03: Escalabilidade

- **RNF-03.1:** A arquitetura deve suportar o processamento de **10.000+ repositórios** sem degradação.
- **RNF-03.2:** O script de ingestão deve ser reexecutável de forma idempotente (sem duplicar dados).

### RNF-04: Segurança

- **RNF-04.1:** Tokens de API (GitHub, OpenAI) devem ser armazenados como variáveis de ambiente, nunca no código.
- **RNF-04.2:** Nenhum dado sensível deve ser exposto em logs ou respostas de API.
- **RNF-04.3:** A aplicação deve validar e sanitizar todos os parâmetros de entrada.

### RNF-05: Manutenibilidade

- **RNF-05.1:** A cobertura de testes deve ser superior a **70%** do código de negócio.
- **RNF-05.2:** O código deve passar em linting com Ruff sem erros.
- **RNF-05.3:** Todas as migrações de banco devem ser reversíveis (com `downgrade`).

### RNF-06: Observabilidade

- **RNF-06.1:** A aplicação deve emitir logs estruturados em formato legível.
- **RNF-06.2:** Deve existir um endpoint `/health` para verificação de saúde da API.
- **RNF-06.3:** Erros no script de ingestão devem ser registrados com stack trace completo.

---

## Restrições

| Restrição | Descrição |
|-----------|-----------|
| **Idioma** | Interface e documentação em português; código e comentários em inglês |
| **Python** | Versão mínima: 3.12 |
| **Banco** | PostgreSQL >= 15 (produção), SQLite (testes) |
| **Open Source** | O projeto deve ser distribuído sob licença permissiva |
| **Dados** | Apenas repositórios públicos do GitHub são indexados |
