makemigrations:
	docker exec -it cuemby ./manage.py makemigrations

migrate:
	docker exec -it cuemby ./manage.py migrate

populate_db:
	docker exec -it cuemby ./manage.py populate_db

load_fixtures:
	docker exec -it cuemby ./manage.py loadfixtures 

test:
	docker exec -it cuemby ./manage.py test
