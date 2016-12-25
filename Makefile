init:
	python3 -m venv venv; \
	echo 'source venv/bin/activate' >> .env; \
	echo 'export DATABASE_URL=""' >> .env; \
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt; \

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