.PHONY: help bootstrap test lint typecheck quality frontend-install frontend-build docker-build docker-up docker-down docker-logs deploy-up deploy-down deploy-logs

help:
	@echo "Targets:"
	@echo "  bootstrap        Create venv + install deps"
	@echo "  test             Run pytest"
	@echo "  quality          Ruff + mypy + coverage gates"
	@echo "  frontend-install Install frontend deps"
	@echo "  frontend-build   Build Next.js frontend"
	@echo "  docker-build     Build production docker images"
	@echo "  docker-up        Start prod stack (nginx+api+web)"
	@echo "  docker-down      Stop stack"
	@echo "  docker-logs      Tail stack logs"
	@echo "  deploy-up        Start stack via deploy/ (recommended)"
	@echo "  deploy-down      Stop deploy/ stack"
	@echo "  deploy-logs      Tail deploy/ stack logs"

bootstrap:
	./scripts/bootstrap_dev.sh

test:
	./scripts/test_smoke.sh

lint:
	./venv/bin/python -m ruff check agents cli mcps tests

typecheck:
	./venv/bin/python -m mypy agents cli mcps --ignore-missing-imports

quality:
	./scripts/ci_quality_gates.sh

frontend-install:
	cd frontend && npm ci

frontend-build:
	cd frontend && npm run build

docker-build:
	docker compose build

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f --tail=200

deploy-up:
	cd deploy && cp -n .env.example .env && docker compose up -d --build

deploy-down:
	cd deploy && docker compose down

deploy-logs:
	cd deploy && docker compose logs -f --tail=200
