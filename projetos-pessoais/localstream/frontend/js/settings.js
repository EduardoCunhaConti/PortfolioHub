const html = document.documentElement;
const themeToggle = document.getElementById('themeToggle');

function applyTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    themeToggle.textContent = theme === 'dark' ? '🌞' : '🌙';
}

themeToggle.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    applyTheme(current === 'dark' ? 'light' : 'dark');
});

const savedTheme = localStorage.getItem('theme') || 'dark';
applyTheme(savedTheme);

async function loadSettings() {
    try {
        const response = await fetch('/api/settings');
        const data = await response.json();
        if (data.media_directory) {
            document.getElementById('directoryInput').value = data.media_directory;
        }
    } catch (error) {
        console.error('Failed to load settings:', error);
    }
}

loadSettings();

function showMessage(text, type) {
    const el = document.getElementById('feedbackMessage');
    el.className = `message message--${type}`;
    el.textContent = text;
}

document.getElementById("saveBtn").addEventListener("click", async () => {
    const directory = document.getElementById("directoryInput").value.trim();

    if (!directory) {
        showMessage("Inform the folder path.", "error");
        return;
    }

    try {
        const response = await fetch("/api/settings", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ directory })
        });

        const data = await response.json();

        if (!response.ok) {
            showMessage(data.detail || "Error saving configuration.", "error");
            return;
        }

        showMessage(
            `Configuration saved! ${data.scan.added} file(s) added from ${data.scan.found} found. Redirecting...`,
            "success"
        );

        setTimeout(() => {
            window.location.href = "/";
        }, 2000);

    } catch (error) {
        showMessage("Error connecting to the server.", "error");
    }
});