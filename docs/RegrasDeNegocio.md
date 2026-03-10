# Regras de Negócio — GoodFirstFinder

## 1. Indexação de Repositórios

### RN-01: Elegibilidade de Repositório

Um repositório é elegível para indexação se atender a **todos** os critérios abaixo:

- Não está arquivado (`is_archived = false`)
- Possui pelo menos **1 commit nos últimos 6 meses** (projeto ativo)
- Possui ao menos **1 issue aberta** com a label `good first issue`
- Possui no mínimo **2 stars** (validação da comunidade)
- Possui um `README.md` (documentação mínima)

### RN-02: Frequência de Atualização

- Repositórios são reavaliados a cada execução do script de ingestão.
- A frequência de execução do script é configurada externamente (cron, agendador do servidor, etc.).
- Uma reavaliação de repositório individual pode ser forçada com intervalo mínimo de **1 hora** entre execuções.

---

## 2. Score de Amigabilidade

### RN-03: Composição do Score Total

O Score Total (0–10) é calculado pela média ponderada de quatro sub-scores:

| Critério                    | Peso | Descrição                                               |
|-----------------------------|------|---------------------------------------------------------|
| `documentation_score`       | 30%  | README, CONTRIBUTING.md, CODE_OF_CONDUCT.md             |
| `community_score`           | 20%  | Receptividade histórica a PRs de iniciantes             |
| `activity_score`            | 20%  | Frequência de commits e responses em issues             |
| `beginner_friendliness_score` | 30% | Presença de labels, issues bem descritas, guias de setup|

### RN-04: Limites do Score

- O Score Total é sempre um valor entre **0.0** e **10.0**.
- Valores fora desse intervalo são truncados (`clamp`).

### RN-05: Score Mínimo para Exibição

- Repositórios com `total_score < 3.0` não são exibidos nos resultados de busca padrão.
- Podem ser acessados diretamente pelo ID se o usuário souber a URL.

### RN-06: Seção "Featured"

- Os **3 repositórios** com maior `total_score` na semana são destacados na seção Featured.
- Em caso de empate, o repositório com maior número de issues `good first issue` abertas tem prioridade.

---

## 3. Busca e Filtros

### RN-07: Ordenação Padrão

- Os resultados de busca são ordenados por `total_score` (decrescente) por padrão.
- Repositórios sem score são exibidos ao final (nulls last).

### RN-08: Filtros Disponíveis

| Filtro              | Tipo    | Descrição                                  |
|---------------------|---------|--------------------------------------------|
| `language`          | string  | Linguagem principal do repositório         |
| `min_score`         | float   | Score mínimo de amigabilidade (0–10)       |
| `max_score`         | float   | Score máximo de amigabilidade (0–10)       |
| `has_contributing`  | boolean | Possui CONTRIBUTING.md                     |
| `has_code_of_conduct` | boolean | Possui CODE_OF_CONDUCT.md                |
| `query`             | string  | Busca textual em nome e descrição          |

### RN-09: Paginação

- O tamanho máximo de página é **100 itens**.
- O tamanho padrão de página é **20 itens**.
- Páginas além do total disponível retornam lista vazia, não erro.

---

## 4. Integrações Externas

### RN-11: Rate Limiting do GitHub

- O cliente GitHub respeita o rate limit da API.
- Em caso de limite atingido (`429`), o script de ingestão aguarda o período indicado no header `Retry-After` antes de continuar.

### RN-12: Fallback de LLM

- Se a chamada ao LLM falhar, o repositório recebe `justification = null` e um score estimado pelas heurísticas booleanas.
- O score heurístico é marcado como `is_ai_scored = false` para transparência.

---

## 5. Dados e Privacidade

### RN-13: Dados Públicos Apenas

- A plataforma indexa **apenas** repositórios públicos.
- Nenhum dado pessoal de usuários do GitHub é armazenado.
