# Restaurant reservation backend

FastAPI service and **Strands Agents** orchestrator for The Gourmet Grill hackathon demo.

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env
python run_server.py
```

- Health: `http://localhost:8000/health`
- Create reservation: `POST http://localhost:8000/api/reservations/`

## Test agent only (CLI)

```bash
python -m src.agents.reservation_agent
```

Requires AWS credentials and Bedrock model access in `.env`.

## Knowledge base setup

See `prereqs/knowledge_base.py` and JSONL files in `prereqs/kb_files/`. Full provisioning is AWS-account specific.

Parent project documentation: [../../README.md](../../README.md)
