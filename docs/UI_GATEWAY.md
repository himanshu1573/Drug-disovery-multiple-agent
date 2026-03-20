# UI Gateway (FastAPI) + Frontend (Next.js)

This repo now includes a minimal human-in-the-loop web UI:

- Backend: `ui_api/app.py` (FastAPI) streams run events over SSE and accepts plan/review decisions.
- Frontend: `frontend/` (Next.js) renders a 2-panel UI (events + plan approval / report).

## 1) Start the backend API

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Enable plan approval interrupt
export A4T_REQUIRE_PLAN_APPROVAL=1

uvicorn ui_api.app:app --reload --port 8000
```

## 2) Start the frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

Open `http://localhost:3000`.

## Notes

- SSE endpoint: `GET /api/runs/{run_id}/events`
- To complete a run, the UI submits a plan decision, resumes, then submits the final review decision when prompted.
