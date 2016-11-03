
help:
	@echo "  clean       remove unwanted stuff"
	@echo "  info 	     show information on current sys config"
	@echo "  lint        run precommit hooks"
	@echo "  migrate     make migrations and migrate all apps"
	@echo "  shell       starts a django ipython shell"
	@echo "  work        run server & gulp"

clean:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' ! -name '*.un~' -exec rm -f {} \;

info:
	python --version
	pyenv --version
	pip --version

lint:
	pre-commit run -a

migrate:
	cd ostrich; python manage.py makemigrations; python manage.py migrate

shell:
	cd ostrich; python manage.py shell -i ipython

client:
	cd static/client; npm start

server:
	python manage.py runserver 0.0.0.0:8000

work:
	python manage.py runserver 0.0.0.0:8000 & cd static/client && npm start
