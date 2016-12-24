init:
	virtualenv -p python3 venv; \
	source ./venv/bin/activate; \
	pip install --upgrade --no-cache-dir -r requirements.txt; \
	pip freeze > requirements.txt; \

run:
	python3 manage.py run

update_deps:
	source ./venv/bin/activate; \
	pip install --upgrade -r requirements.txt; \

revision:
	alembic revision --autogenerate;

upgrade:
	alembic upgrade head

downgrade:
	alembic downgrade head