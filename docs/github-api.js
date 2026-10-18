/* ============================================================
   PortfolioHub — integração com a API pública do GitHub
   Lê projetos, atividade recente e contribuidores, e exibe no site.
   Usa cache local (30 min) para respeitar o limite de requisições.
   ============================================================ */
(function () {
  "use strict";

  var USUARIO = "EduardoCunhaConti";          // dono dos projetos
  var REPO_HUB = USUARIO + "/PortfolioHub";   // repositório do hub
  var API = "https://api.github.com";
  var TTL = 30 * 60 * 1000;                   // 30 minutos

  function el(tag, classe, texto) {
    var e = document.createElement(tag);
    if (classe) e.className = classe;
    if (texto !== undefined) e.textContent = texto;
    return e;
  }

  function link(texto, url) {
    var a = el("a", "", texto);
    a.href = url;
    a.target = "_blank";
    a.rel = "noopener";
    return a;
  }

  function data(iso) {
    return new Date(iso).toLocaleDateString("pt-BR");
  }

  function ler(chave) {
    try { return JSON.parse(localStorage.getItem(chave)); } catch (e) { return null; }
  }

  function guardar(chave, dados) {
    try { localStorage.setItem(chave, JSON.stringify({ t: Date.now(), d: dados })); } catch (e) { /* sem cache */ }
  }

  function buscar(caminho) {
    var chave = "gh:" + caminho;
    var cache = ler(chave);
    if (cache && Date.now() - cache.t < TTL) return Promise.resolve(cache.d);
    return fetch(API + caminho, { headers: { Accept: "application/vnd.github+json" } })
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (d) { guardar(chave, d); return d; })
      .catch(function (erro) {
        if (cache) return cache.d;   // usa o cache antigo se a API falhar
        throw erro;
      });
  }

  function mensagem(alvo, texto) {
    alvo.textContent = "";
    alvo.appendChild(el("p", "muted", texto));
  }

  function mostrarRepos(alvo, repos) {
    var lista = repos.filter(function (r) { return !r.fork; })
      .sort(function (a, b) { return new Date(b.pushed_at) - new Date(a.pushed_at); });
    alvo.textContent = "";
    if (!lista.length) return mensagem(alvo, "Nenhum repositório público encontrado.");
    lista.forEach(function (r) {
      var c = el("article", "cartao");
      c.appendChild(el("h3", "", r.name));
      c.appendChild(el("p", "", r.description || "Sem descrição."));
      var tags = [r.language].concat(r.topics || []).filter(Boolean).join(" · ");
      if (tags) c.appendChild(el("p", "tags", tags));
      c.appendChild(el("p", "", "Última atualização: " + data(r.pushed_at)));
      var l = el("div", "links");
      l.appendChild(link("Ver no GitHub →", r.html_url));
      c.appendChild(l);
      alvo.appendChild(c);
    });
  }

  function mostrarCommits(alvo, commits) {
    alvo.textContent = "";
    if (!commits.length) return mensagem(alvo, "Nenhuma atividade encontrada.");
    commits.forEach(function (c) {
      var li = el("li");
      var msg = c.commit.message.split("\n")[0];
      li.appendChild(link(msg, c.html_url));
      var autor = (c.commit.author && c.commit.author.name) || "autor desconhecido";
      li.appendChild(el("span", "meta", autor + " · " + data(c.commit.author.date)));
      alvo.appendChild(li);
    });
  }

  function mostrarContribuidores(alvo, pessoas) {
    alvo.textContent = "";
    if (!pessoas.length) return mensagem(alvo, "Nenhum contribuidor encontrado.");
    pessoas.forEach(function (p) {
      var a = link("", p.html_url);
      a.className = "membro";
      var img = el("img");
      img.src = p.avatar_url + (p.avatar_url.indexOf("?") > -1 ? "&" : "?") + "s=72";
      img.alt = "Foto de " + p.login;
      img.width = 36;
      img.height = 36;
      a.appendChild(img);
      a.appendChild(el("span", "", p.login + " · " + p.contributions + " commits"));
      alvo.appendChild(a);
    });
  }

  function carregar(id, caminho, desenhar) {
    var alvo = document.getElementById(id);
    if (!alvo) return;
    buscar(caminho).then(function (d) { desenhar(alvo, d); })
      .catch(function () { mensagem(alvo, "Não foi possível carregar os dados do GitHub agora. Tente novamente mais tarde."); });
  }

  carregar("gh-repos", "/users/" + USUARIO + "/repos?per_page=100", mostrarRepos);
  carregar("gh-commits", "/repos/" + REPO_HUB + "/commits?per_page=5", mostrarCommits);
  carregar("gh-contribuidores", "/repos/" + REPO_HUB + "/contributors?per_page=10", mostrarContribuidores);
})();