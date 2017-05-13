deps:
	@pip install -r requirements.txt
	@npm install --prefix vue_blog/

makemigrations:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

run:
	@python manage.py runserver

shell:
	@python manage.py shell_plus

urls:
	@python manage.py show_urls