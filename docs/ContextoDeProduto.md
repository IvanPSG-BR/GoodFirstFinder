# Contexto de Produto — GoodFirstFinder

## Visão Geral

O **GoodFirstFinder** é uma plataforma de busca curada que conecta desenvolvedores Júniores e Estagiários a projetos Open Source adequados para suas primeiras contribuições.

## Problema

Contribuir para projetos Open Source pela primeira vez é intimidador:

- **Ruído na busca:** Milhares de repositórios sem filtro de receptividade real para iniciantes.
- **Medo de rejeição:** PRs ignorados ou mantainers agressivos desmotivam contribuidores iniciantes.
- **Documentação pobre:** Projetos sem CONTRIBUTING.md, guias de setup ou padrões claros.
- **Falta de orientação:** Não saber se a issue escolhida é adequada para o seu nível.

## Proposta de Valor

> *Curadoria inteligente focada na "Amigabilidade ao Contribuidor", não apenas na qualidade do código.*

O sistema atribui um **Score de Amigabilidade** a cada repositório, baseado em critérios como:

- Qualidade da documentação (README, CONTRIBUTING.md, CODE_OF_CONDUCT.md)
- Histórico de receptividade a PRs de iniciantes
- Atividade e saúde do projeto
- Clareza das issues abertas

## Público-Alvo

- **Primário:** Desenvolvedores Júniores e Estagiários (foco inicial no Brasil).
- **Secundário:** Desenvolvedores intermediários migrando para Open Source.
- **Idioma:** Interface em português, mas sem barreira para projetos em inglês técnico.

## Modelo de Interação (UX)

- **Busca por Filtros e Categorias** — não um chatbot.
  - Motivo: Mais familiar, rápido e sem ambiguidade de intenção.
- **IA Invisível:** A IA não interage com o usuário em tempo real; ela pré-analisa e enriquece os dados.
- **Seção "Featured":** Destaque semanal para os repositórios com maior Score de Amigabilidade.

## Métricas de Sucesso

| Métrica | Meta (3 meses) |
|---------|---------------|
| Usuários ativos mensais | 500+ |
| Repositórios indexados | 1.000+ |
| Taxa de conversão (busca → PR) | > 5% |
| NPS dos usuários | > 40 |
