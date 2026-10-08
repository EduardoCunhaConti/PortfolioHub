const API_URL = "http://localhost:8001/api";


// ── Media ───────────────────────────────────────────────────────────────────

async function getMedia() {
    try {
        const response = await fetch(`${API_URL}/media`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching medias:", error);
        return [];
    }
}

async function getMediaById(id) {
    try {
        const response = await fetch(`${API_URL}/media/${id}`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching media:", error);
        return null;
    }
}

async function deleteMedia(id) {
    try {
        const response = await fetch(`${API_URL}/media/${id}`, {
            method: "DELETE"
        });
        return await response.json();
    } catch (error) {
        console.error("Error deleting media:", error);
        return null;
    }
}


// ── History ─────────────────────────────────────────────────────────────────

async function saveHistory(mediaId, progress) {
    try {
        const response = await fetch(`${API_URL}/history`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ media_id: mediaId, progress })
        });
        return await response.json();
    } catch (error) {
        console.error("Error saving history:", error);
        return null;
    }
}

async function getHistory(mediaId) {
    try {
        const response = await fetch(`${API_URL}/history/${mediaId}`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching history:", error);
        return null;
    }
}


// ── Settings ─────────────────────────────────────────────────────────────────

async function getSettings() {
    try {
        const response = await fetch(`${API_URL}/settings`);
        return await response.json();
    } catch (error) {
        console.error("Error fetching settings:", error);
        return null;
    }
}

async function saveSettings(directory) {
    try {
        const response = await fetch(`${API_URL}/settings`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ directory })
        });
        return await response.json();
    } catch (error) {
        console.error("Error saving settings:", error);
        return null;
    }
}