mig:
	alembic revision --autogenerate -m "Create a baseline migrations"

custom_mig:
	alembic revision -m "Create trigger on students table"

up:
	alembic upgrade head

downup:
	alembic downgrade head

extract:
	pybabel extract --input-dirs=. -o locales/messages.pot

init:
	pybabel init -i locales/messages.pot -d locales -D messages -l en
	pybabel init -i locales/messages.pot -d locales -D messages -l ru
	pybabel init -i locales/messages.pot -d locales -D messages -l uz

compile:
	pybabel compile -d locales -D messages

update:
	pybabel update -d locales -D messages -i locales/messages.pot

web_command:
	uvicorn web.app:app --host localhost --port 8001
