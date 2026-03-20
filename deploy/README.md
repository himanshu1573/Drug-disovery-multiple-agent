# Deployment package (recommended layout)

This folder is a **deployment wrapper** around the repo. It’s designed so you can deploy by copying/cloning the repo and only managing one runtime directory: `deploy/`.

## What you deploy

On a server/VPS, you can deploy the full stack using Docker Compose:

- `api` (FastAPI/Uvicorn): agent runtime + MCP dispatch
- `web` (Next.js): UI
- `nginx` (reverse proxy): routes `/` → `web`, `/api` → `api` (includes SSE support)

## Quick start (VPS)

1) Copy repo to the server (git clone or rsync).
2) Create `deploy/.env` (start from `deploy/.env.example`).
3) Start:

```bash
cd deploy
cp .env.example .env
# edit deploy/.env and set OPENAI_API_KEY (recommended) or GOOGLE_API_KEY
docker compose up -d --build
```

Open:

- UI: `http://<your-domain>/`
- Health: `http://<your-domain>/api/health`

### If port 80 is already in use (common on laptops)

Run nginx on a different port, for example 8080:

```bash
cd deploy
A4T_HTTP_PORT=8080 docker compose up -d
```

Then open:

- UI: `http://localhost:8080/`
- Health: `http://localhost:8080/api/health`

## Files in this folder

- `deploy/docker-compose.yml`: production compose entrypoint (builds from repo root)
- `deploy/nginx/default.conf`: nginx routing config (Docker DNS resolver enabled)
- `deploy/.env.example`: minimal environment template
