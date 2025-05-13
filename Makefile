build:
	docker compose up --build -d

re-build:
	docker compose down
	docker compose up --build -d

run-tests:
	docker compose exec backend poetry run pytest --cov=backend --cov-report term-missing

stop:
	docker compose down
