.PHONY: help install dev-install test coverage lint format clean run docs

help:
	@echo "TUYUL-FX-HYBRID v5.4.0 - Makefile Commands"
	@echo "==========================================="
	@echo "install        - Install production dependencies"
	@echo "dev-install    - Install with development dependencies"
	@echo "test           - Run tests"
	@echo "coverage       - Run tests with coverage report"
	@echo "lint           - Run linters (flake8, mypy)"
	@echo "format         - Format code with black"
	@echo "clean          - Clean build artifacts"
	@echo "run            - Run the application"
	@echo "docs           - Generate API documentation"

install:
	pip install -r requirements.txt
	pip install -e .

dev-install:
	pip install -r requirements.txt
	pip install -e ".[dev]"

test:
	pytest tests/ -v

coverage:
	pytest tests/ --cov=src/tuyul_fx_hybrid --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

lint:
	flake8 src/tuyul_fx_hybrid --max-line-length=100 --exclude=__pycache__
	mypy src/tuyul_fx_hybrid --ignore-missing-imports

format:
	black src/tuyul_fx_hybrid tests/
	@echo "Code formatted with black"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/
	@echo "Cleaned build artifacts"

run:
	python -m uvicorn src.tuyul_fx_hybrid.main:app --reload --host 0.0.0.0 --port 8000

run-prod:
	python -m uvicorn src.tuyul_fx_hybrid.main:app --host 0.0.0.0 --port 8000 --workers 4

docs:
	@echo "API documentation available at:"
	@echo "  Swagger UI: http://localhost:8000/docs"
	@echo "  ReDoc:      http://localhost:8000/redoc"
