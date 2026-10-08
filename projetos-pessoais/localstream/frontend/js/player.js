const html = document.documentElement;
const themeToggle = document.getElementById("themeToggle");

function applyTheme(theme) {
    html.setAttribute("data-theme", theme);
    themeToggle.textContent = theme === "dark" ? "🌙" : "☀️";
    localStorage.setItem("theme", theme);
}

themeToggle.addEventListener("click", () => {
    const current = html.getAttribute("data-theme");
    applyTheme(current === "dark" ? "light" : "dark");
});

applyTheme(localStorage.getItem("theme") || "dark");

function formatDuration(seconds) {
    if (!seconds) return "Duração desconhecida";
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    return h > 0 ? `${h}h ${m}m` : `${m}m`;
}

function formatProgress(seconds) {
    if (!seconds) return "0m assistido";
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    return h > 0 ? `${h}h ${m}m assistido` : `${m}m assistido`;
}

const params = new URLSearchParams(window.location.search);
const mediaId = params.get("id");

if (!mediaId) {
    window.location.href = "/";
}

const video = document.getElementById("videoPlayer");
let saveInterval = null;


async function init() {
    const media = await getMediaById(mediaId);

    if (!media) {
        window.location.href = "/";
        return;
    }

    // preenche navbar e informações
    document.getElementById("mediaTitle").textContent = media.title;
    document.getElementById("infoTitle").textContent = media.title;
    document.getElementById("infoBadge").textContent = media.media_type === "series" ? "Série" : "Filme";
    document.getElementById("infoDuration").textContent = formatDuration(media.duration);

    // configura o player
    video.src = `/api/stream/${mediaId}`;

    // retoma do progresso salvo
    video.addEventListener("loadedmetadata", async () => {
        const history = await getHistory(mediaId);
        if (history && history.progress > 0) {
            const isNearEnd = history.progress >= video.duration * 0.95;
            video.currentTime = isNearEnd ? 0 : history.progress;
        }
    });

    // atualiza progresso na tela
    video.addEventListener("timeupdate", () => {
        document.getElementById("infoProgress").textContent = formatProgress(Math.floor(video.currentTime));
    });

    // salva progresso a cada 10 segundos
    video.addEventListener("play", () => {
        saveInterval = setInterval(() => {
            saveHistory(mediaId, Math.floor(video.currentTime));
        }, 10000);
    });

    // para o intervalo ao pausar e salva
    video.addEventListener("pause", () => {
        clearInterval(saveInterval);
        saveHistory(mediaId, Math.floor(video.currentTime));
    });

    // salva ao sair da página
    window.addEventListener("beforeunload", () => {
        saveHistory(mediaId, Math.floor(video.currentTime));
    });
}

init();