# Changelog

Todas as mudanças relevantes deste projeto são registradas aqui.
O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o versionamento segue o [SemVer](https://semver.org/lang/pt-BR/).

## [2.0.0] — Implantação em produção

### Adicionado
- Integração do site com a API do GitHub: projetos, atividade recente e contribuidores.
- Política de segurança (`SECURITY.md`), com 2FA na conta do mantenedor e canal de relato de vulnerabilidades.
- Práticas de colaboração: `CONTRIBUTING.md`, `CODEOWNERS` e modelos de issue e Pull Request.
- Verificação automática (GitHub Actions e `scripts/verificar_site.py`) em cada Pull Request.
- Página 404 personalizada e metadados Open Graph.
- Cópias em PDF da documentação em `documentacao/`.

## [1.1.1] — Ajuste do site

### Removido
- Seção "Apresentação em vídeo" do site, que não será utilizada.

## [1.1.0] — Projetos no portfólio

### Adicionado
- Pastas dos projetos: `projetos-academicos/`, `projetos-pessoais/` e `projetos-de-cursos/`, cada uma com README próprio.
- Seção "Projetos" no site, com um cartão para cada projeto.
- Índice dos projetos, estrutura e fluxo de versionamento no `README.md`.

### Alterado
- `README.md` reescrito para refletir o conteúdo completo do hub.

## [1.0.0] — Site base e estrutura do repositório

### Adicionado
- Página inicial no GitHub Pages (`docs/index.html` e `docs/style.css`) com apresentação, documentos e contato.
- `README.md` com a descrição do repositório.
- `.gitignore` para Python, Jupyter e arquivos de sistema.