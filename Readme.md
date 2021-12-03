# Description of commands

Before starting, it is necessary to rename "default.env.dev" to ".env.dev"

For building project, it can be used the command:
> docker build . --no-cache --force-rm  

For starting project as a daemon, it can be used the command:
> docker-compose up -d --build

For connection to database:
> docker-compose exec db psql --username=postgres --dbname=task_db

Command for preparing migrations:
> docker-compose exec web python manage.py makemigrations data

Command for migration:
> docker-compose exec web python manage.py migrate --noinput

Command for starting autotests:
> docker-compose exec web python manage.py test

Command for creation superuser:
> docker-compose exec web python manage.py createsuperuser

or:
> docker-compose exec web ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); 
> User.objects.create_superuser('admin', 'admin@admin.ru', 'admin12345')"

# For removing

Get info about available volumes:
> docker volume ls

For deleting database:
> docker volume rm task-django_postgres_data

If there is a mistake "Error response from daemon: remove task-django_postgres_data: volume is in use - [1e7edab8698f7ef40731dc5044436b0ba26dde492f0a374c4b34785da569c803]":
> docker rm 1e7edab8698f7ef40731dc5044436b0ba26dde492f0a374c4b34785da569c803

For getting info about containers:
> docker ps

For deleting docker container with CONTAINER_ID=c3195dfb08e9:
> docker rm c3195dfb08e9
