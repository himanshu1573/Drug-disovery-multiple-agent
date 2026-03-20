# Deployment (Beginner-friendly: Single VPS, Single Domain)

This repo can be deployed as three Docker services on one VPS:

- `nginx` (reverse proxy): routes `/` → Next.js, `/api` → FastAPI (includes SSE support)
- `web` (Next.js): UI
- `api` (FastAPI/Uvicorn): agent runtime + MCP dispatch

## Where can I deploy this?

Recommended for beginners (works best with this repo’s Docker Compose setup):

- A small VPS with a public IPv4 + a domain name:
  - DigitalOcean Droplet, Hetzner Cloud, AWS Lightsail, Linode/Akamai, etc.

Possible but more advanced (you’ll need to split services or adapt networking):

- “Platform” hosts (Render/Railway/Fly.io) can run Docker, but multi-service + reverse-proxy + SSE tends to require extra setup.
- Vercel is great for the **frontend**, but this repo also needs the **API** runtime; the simplest path is a single VPS.

## 1) VPS prerequisites

- Docker + Docker Compose installed
- A domain pointing to the VPS (A record)

### Example: Ubuntu 22.04/24.04 one-time setup

SSH into your server, then:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl git
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
newgrp docker
docker --version
docker compose version
```

If `docker compose` is not found, install the Compose plugin for your distro.

## 2) Configure environment

On the VPS, create `deploy/.env` (copy from `deploy/.env.example`) and set:

- `OPENAI_API_KEY` (recommended) **or** `GOOGLE_API_KEY` / `GEMINI_API_KEY`
- Optional model defaults:
  - `A4T_SYSTEM_LLM_PROVIDER=auto|openai|google` (default: `auto`, probes OpenAI first)
  - `A4T_SYSTEM_REASONING_MODEL`
  - `A4T_SYSTEM_FAST_MODEL`

The backend writes run artifacts/state under `A4T_ARTIFACT_DIR` (mounted as a Docker volume).

### How to set your API key (beginner steps)

1) Get a provider key:
   - OpenAI: create an API key in your OpenAI account dashboard.
   - Google: create a Gemini API key in Google AI Studio / Google Cloud.
2) Edit the env file on the server:

```bash
cd /path/to/Drugagent/deploy
cp .env.example .env
nano .env
```

3) Put your key in **exactly one** of these:

```bash
OPENAI_API_KEY=your_key_here
# or
GOOGLE_API_KEY=your_key_here
```

Tip: keep `.env` private. Do not commit it to git or paste it in screenshots.

More knobs (models, fallbacks, rate limits): `docs/CONFIGURATION_POLICY.md`.

## 3) Start the stack

Recommended: run Compose from `deploy/` so the deployment-specific config (nginx + env) is self-contained.

```bash
cd deploy
docker compose up -d --build
```

Open:

- UI: `http://<your-domain>/`
- API: `http://<your-domain>/api/runs/<run_id>/state`

## 4) TLS (recommended)

The included Nginx config is HTTP-only. For HTTPS, choose one:

1) Put Cloudflare in front (easy) and keep origin HTTP.
2) Add a TLS terminator (Caddy) in front of Nginx.
3) Add Certbot + Nginx TLS config.

## 5) Persistence and restarts

The API keeps a `latest.json` snapshot per run under:

- `artifacts/working_memory/<run_id>/latest.json`

This allows the UI to reload run state after the API container restarts.

## 6) Troubleshooting

- Check logs:
  - `docker compose logs -f api`
  - `docker compose logs -f web`
  - `docker compose logs -f nginx`
- This UI API is configured in **strict mode** (no silent deterministic fallbacks). If LLM configuration is missing
  or the provider errors, the run will fail and the UI will show the error message.
