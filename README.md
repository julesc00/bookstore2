# Project from book Django for Professionals
Django 4 version, I used the 4.2 LTS

## Chapter 4 | Bookstore Project
docker-compose command: `docker-compose exec web python manage.py startapp accounts`

### Set a custom default user model

**NOTE:** When needing to install dependencias with:  
```aiignore
docker-compose down
docker-compose up -d --build
```

Making migrations to an already existing model, but early development stages  
**Note:** Do this from the model start rather.
```aiignore
docker-compose exec web rm -r books/migrations
docker-compose down
docker-compose up -d --build
docker volume rm books_postgres_data
docker-compose up -d
docker-compose exec web python manage.py makemigrations books
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```