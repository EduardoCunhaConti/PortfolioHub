const html = document.documentElement;
const themeToggle = document.getElementById('themeToggle');

function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    themeToggle.textContent = theme === 'dark' ? '🌞' : '🌙';
    localStorage.setItem('theme', theme);
}

themeToggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    applyTheme(current === 'dark' ? 'light' : 'dark');
});

applyTheme(localStorage.getItem('theme') || 'dark');

let allMedia = [];
let activeFilter = 'all';

function getProgressPercent(progress, duration) {
    if (!duration || duration === 0) return 0;
    return Math.min((progress / duration) * 100, 100);
}

function getPlaceholderEmoji(mediaType) {
    return mediaType === 'movie' ? '🎬' : '📺';
}

function createCard(media) {
    const progressPercent = getProgressPercent(media.progress, media.duration);
    const card = document.createElement('div');
    card.className
    card.dataset.type = media.media_type;
    card.dataset.title = media.title.toLowerCase();

    card.innerHTML = `
        <div class="card__poster">
            <span class="card__poster-placeholder">${getPlaceholderEmoji(media.media_type)}</span>
            <span class="card__badge">${media.media_type === "series" ? "Series" : "Movie"}</span>
            <div class="card__poster-overlay"></div>
            <div class="card__play-btn">▶</div>
        </div>
        <div class="card__info">
            <span class="card__title" title="${media.title}">${media.title}</span>
            ${progressPercent > 0 ? `
            <div class="card__progress">
                <div class="card__progress-bar" style="width: ${progressPercent}%"></div>
            </div>` : ""}
        </div>
    `;

    card.addEventListener("click", () => {
        window.location.href = `/player?id=${media.id}`;
    });

    return card;
}

function renderCatalog(mediaList) {
    const grid = document.getElementById("catalogGrid");
    const empty = document.getElementById("catalogEmpty");

    grid.innerHTML = "";

    if (mediaList.length === 0) {
        empty.classList.remove("hidden");
        return;
    }

    empty.classList.add("hidden");
    mediaList.forEach(media => grid.appendChild(createCard(media)));
}

function applyFilters() {
    const query = document.getElementById("searchInput").value.toLowerCase().trim();

    const filtered = allMedia.filter(media => {
        const matchesFilter = activeFilter === "all" || media.media_type === activeFilter;
        const matchesSearch = media.title.toLowerCase().includes(query);
        return matchesFilter && matchesSearch;
    });

    renderCatalog(filtered);
}

document.querySelectorAll(".filter-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("filter-btn--active"));
        btn.classList.add("filter-btn--active");
        activeFilter = btn.dataset.filter;
        applyFilters();
    });
});

document.getElementById("searchInput").addEventListener("input", applyFilters);


async function init() {
    const settings = await getSettings();
    if (!settings || !settings.media_directory) {
        window.location.href = "/settings";
        return;
    }

    allMedia = await getMedia();
    renderCatalog(allMedia);
}

init();