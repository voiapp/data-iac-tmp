PYTHON_MODULE=porter

default: help

help:
	@echo 'usage: make [target] ...'
	@echo
	@echo 'targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

.PHONY: format
format: ## Format code
	black $(PYTHON_MODULE)
	isort -m3 --tc $(PYTHON_MODULE)

.PHONY: lint
lint: ## Lint code
	black $(PYTHON_MODULE) --check 
	isort -m3 --tc -c $(PYTHON_MODULE)
	mypy $(PYTHON_MODULE)
	pylint --rcfile=pyproject.toml -j 4 ${PYTHON_MODULE}
	
.PHONY: test	
test: ## Run unit tests
	pytest --cov=porter tests

.PHONY: install
install: ## Install dependencies via pipenv
	pipenv install --dev
	pipenv run pip install -e .
