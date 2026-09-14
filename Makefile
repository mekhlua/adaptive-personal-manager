.PHONY: setup up down test lint

setup:
	cp -n .env.example .env || true
	docker compose build

up:
	docker compose up

down:
	docker compose down

test:
	docker compose run --rm backend pytest --cov=app

lint:
	docker compose run --rm backend ruff check .
