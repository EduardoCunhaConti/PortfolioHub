# 🎬 LocalStream

> O LocalStream é uma aplicação que cria uma plataforma de streaming pessoal, permitindo que arquivos de mídia locais sejam acessados via navegador.
---

## 🚀 Tecnologias

| Camada | Tecnologias |
|---|---|
| Backend | Python 3, FastAPI, SQLAlchemy, SQLite |
| Frontend | HTML, CSS, JavaScript |

---

## 📁 Estrutura de pastas
```
LocalStream/
│
├── 📂 backend/
│   ├── 📂 app/
│   │   ├── 📄 main.py
│   │   ├── 📄 config.py
│   │   ├── 📂 api/
│   │   │   ├── media.py
│   │   │   ├── stream.py
│   │   │   ├── history.py
│   │   │   └── settings.py
│   │   ├── 📂 services/
│   │   │   ├── scanner.py
│   │   │   └── metadata.py
│   │   ├── 📂 db/
│   │   │   ├── database.py
│   │   │   ├── models.py
│   │   │   └── crud.py
│   │   └── 📂 schemas/
│   │       ├── media.py
│   │       └── settings.py
│   └── 📄 requirements.txt
│
├── 📂 frontend/
│   ├── 📄 index.html
│   ├── 📄 player.html
│   ├── 📄 settings.html
│   ├── 📂 css/
│   │   ├── reset.css
│   │   ├── main.css
│   │   ├── catalog.css
│   │   ├── player.css
│   │   └── settings.css
│   └── 📂 js/
│       ├── api.js
│       ├── catalog.js
│       ├── player.js
│       └── settings.js
│
└── 📄 README.md
```

---

## ⚙️ Como instalar e rodar

### Pré-requisitos

- Python 3.10+
- Git

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/EduardoCunhaConti/LocalStream.git
cd LocalStream
```

**2. Crie e ative o ambiente virtual**
```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Inicie o servidor**
```bash
python -m uvicorn app.main:app --port 8001
```

**5. Acesse no navegador**
```
http://localhost:8001
```

> 💡 Na primeira execução, você será redirecionado para a tela de configuração onde deverá informar o caminho da pasta com seus arquivos de vídeo.

---

## 🗺️ Roadmap

### ✅ Fase 1 — MVP
- [x] Scanner de arquivos locais
- [x] Streaming via HTTP Range Requests
- [x] Catálogo com filtros e busca
- [x] Player com controles nativos
- [x] Histórico de reprodução com retomada automática
- [x] Alternância entre dark mode e light mode
- [x] Tela de configuração de diretório

### 🚧 Fase 2 — Enriquecimento (em desenvolvimento)
- [ ] Integração com TMDB (capas, sinopses, ano de lançamento)
- [ ] Fallback de capa extraída do próprio arquivo de vídeo
- [ ] Separação de séries por temporadas e episódios
- [ ] Suporte a múltiplos diretórios
- [ ] Filtros avançados (ano, gênero)

### 🔮 Fase 3 — Multiplataforma
- [ ] Migração do frontend para React
- [ ] Layout adaptado para tablet e SmartTV
- [ ] Deploy via Docker para acesso em rede local
- [ ] Autenticação por usuário
- [ ] Notificações de novos arquivos detectados