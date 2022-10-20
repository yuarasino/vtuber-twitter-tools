.PHONY: run
run:
	poetry run python src/main.py

.PHONY: lint
lint:
	poetry run black --check .
	poetry run isort --check-only .

.PHONY: fix
fix:
	poetry run black .
	poetry run isort .
