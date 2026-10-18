# Política de Segurança

## Versões suportadas

Somente a versão mais recente (branch `main` e a última tag `vX.Y.Z`) recebe correções.

## Como reportar uma vulnerabilidade

Não abra uma issue pública. Envie um e-mail para eduardodacunhaconti@gmail.com informando a descrição, os passos para reproduzir e o impacto. A resposta inicial será dada em até 5 dias úteis.

## Práticas adotadas

- Autenticação em dois fatores na conta do mantenedor.
- Leitura pública; escrita somente pelo dono do repositório.
- Convenção de trabalho: toda alteração passa por Pull Request, com a verificação automática (GitHub Actions) aprovada antes do merge.
- A verificação automática confere arquivos obrigatórios, links internos do site, README em cada projeto e a ausência de arquivos sensíveis (`.env`, `.pem`, `.key`).
- Menor privilégio: o `GITHUB_TOKEN` do workflow é somente leitura.
- Nenhum segredo, token ou arquivo `.env` no repositório (`.gitignore` e verificação no CI).
- Dados pessoais limitados a e-mail e perfis públicos de contato.

## Limitações e próximos passos

- A regra "toda alteração por Pull Request" é uma convenção, ainda não imposta por proteção de branch (ruleset).
- Secret scanning e Dependabot não foram ativados nesta versão.
- Este é um repositório pessoal: só existem os papéis de dono e colaborador, sem times nem permissões granulares.