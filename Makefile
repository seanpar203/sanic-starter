SHELL := /bin/bash

init:
	python3 -m venv venv; \
	source venv/bin/activate; \
	pip3 install -r requirements.txt; \

run:
	source venv/bin/activate; \
	python manage.py run

update_deps:
	source ./venv/bin/activate; \
	pip install -r requirements.txt

revision:
	source venv/bin/activate; \
	PYTHONPATH=. alembic revision --autogenerate

upgrade:
	source venv/bin/activate; \
	PYTHONPATH=. alembic upgrade head

downgrade:
	source venv/bin/activate; \
	PYTHONPATH=. alembic downgrade -1
