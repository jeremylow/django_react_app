
help:
	@echo "  build       run npm build scripts & collectstatic"
	@echo "  clean       remove unwanted stuff"
	@echo "  client      run react client server"
	@echo "  info 	     show information on current sys config"
	@echo "  lint        run precommit hooks"
	@echo "  migrate     make migrations and migrate all apps"
	@echo "  server      run django development server"
	@echo "  shell       starts a django ipython shell"

build:
	cd posts/client; npm run build ../static/posts/build/
	mv posts/client/build posts/static/posts/client/build
	python manage.py collectstatic

clean:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' ! -name '*.un~' -exec rm -f {} \;

client:
	cd posts/client; npm start

info:
	python --version
	pyenv --version
	pip --version

lint:
	pre-commit run -a

migrate:
	python manage.py makemigrations; python manage.py migrate

server:
	python manage.py runserver 0.0.0.0:8000

shell:
	python manage.py shell -i ipython
