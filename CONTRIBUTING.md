# Guia de Contribuição

Este guia descreve o fluxo de trabalho do PortfolioHub.

## Papéis

Repositórios pessoais do GitHub têm apenas dois níveis de permissão (dono e colaborador). Nesta versão não há colaboradores, então os papéis são:

| Papel | Quem | O que pode fazer |
|---|---|---|
| Dono | Conta `EduardoCunhaConti` | Configurações, segurança, merges e releases |
| Público | Qualquer pessoa | Ler o código, abrir issues e sugerir mudanças por fork e Pull Request |

## Fluxo de trabalho

1. Crie ou escolha uma **issue** (use o modelo "Tarefa de implantação").
2. Crie uma branch a partir da `main`: `feat/...`, `fix/...`, `docs/...` ou `chore/...`.
3. Faça commits pequenos no padrão *Conventional Commits* em português, por exemplo `feat(site): adiciona seção de contribuidores`.
4. Rode `python scripts/verificar_site.py` localmente.
5. Abra um **Pull Request** preenchendo o modelo e referenciando a issue (`Closes #N`).
6. Aguarde a verificação automática ficar verde, revise o próprio diff e faça o merge. Depois do merge, a branch é apagada.

## Versionamento

- [SemVer](https://semver.org/lang/pt-BR/) com tags anotadas `vX.Y.Z`.
- Toda mudança relevante entra no [CHANGELOG](CHANGELOG.md).

## Regras de segurança

- Nunca versione senhas, tokens, chaves ou arquivos `.env`.
- Relate vulnerabilidades pelo canal descrito em [SECURITY.md](SECURITY.md).

## Conduta

Seja respeitoso e objetivo. Críticas são sobre o código, não sobre as pessoas.