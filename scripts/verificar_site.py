#!/usr/bin/env python3
"""Verificações automáticas do PortfolioHub.

Uso (na raiz do repositório):  python scripts/verificar_site.py
Retorna código 1 se algo falhar (usado pelo GitHub Actions).
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

# Garante saída em UTF-8 (evita erro com ✓/✗ e acentos no console do Windows)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVOS_OBRIGATORIOS = [
    "README.md", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", ".gitignore",
    "docs/index.html", "docs/style.css",
]
erros = []


def falha(msg):
    erros.append(msg)
    print(f"  ✗ {msg}")


def ok(msg):
    print(f"  ✓ {msg}")


class Coletor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links = set(), []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if d.get("id"):
            self.ids.add(d["id"])
        for chave in ("href", "src"):
            if d.get(chave):
                self.links.append(d[chave])


print("1) Arquivos obrigatórios")
for nome in ARQUIVOS_OBRIGATORIOS:
    if (RAIZ / nome).is_file():
        ok(nome)
    else:
        falha(f"arquivo ausente: {nome}")

print("2) Links internos do site (docs/index.html)")
pagina = RAIZ / "docs" / "index.html"
if pagina.is_file():
    c = Coletor()
    c.feed(pagina.read_text(encoding="utf-8"))
    for alvo in c.links:
        if re.match(r"^(https?:|mailto:|data:|tel:)", alvo):
            continue
        if alvo.startswith("#"):
            if alvo[1:] in c.ids:
                ok(f"âncora {alvo}")
            else:
                falha(f"âncora sem destino: {alvo}")
            continue
        caminho = (pagina.parent / alvo.split("#")[0].split("?")[0]).resolve()
        if caminho.is_file():
            ok(alvo)
        else:
            falha(f"arquivo referenciado não existe: {alvo}")

print("3) README em cada pasta de projeto")
for pasta in sorted(RAIZ.glob("projetos-*/*")):
    if pasta.is_dir():
        rel = pasta.relative_to(RAIZ)
        if (pasta / "README.md").is_file():
            ok(f"{rel}/README.md")
        else:
            falha(f"sem README.md: {rel}")

print("4) Arquivos sensíveis")
sensiveis = [p for p in RAIZ.rglob("*") if p.is_file() and ".git" not in p.parts
             and (p.name.startswith(".env") or p.suffix in {".pem", ".key"})]
if sensiveis:
    for p in sensiveis:
        falha(f"arquivo sensível versionado: {p.relative_to(RAIZ)}")
else:
    ok("nenhum .env, .pem ou .key encontrado")

print()
if erros:
    print(f"FALHOU: {len(erros)} problema(s) encontrado(s).")
    sys.exit(1)
print("OK: todas as verificações passaram.")