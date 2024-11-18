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

For troubleshooting when issues with container images:  
```aiignore
docker image prune -f
docker-compose build --no-cache
docker-compose up -d

# If the above didn't work:
docker-compose down --rmi all
docker-compose up -d --build

# Restart docker
sudo systemctl restart docker
docker-compose up -d --build

```

## Chapter 15 | Search
Search packages to enhance filtering
1. [django-watson](https://github.com/etianen/django-watson).
2. [django-haystack](https://github.com/django-haystack/django-haystack).
3. For PostgreSQL, rather use Djangos [full text search](https://docs.djangoproject.com/en/4.0/ref/contrib/postgres/search/).
4. Enterprise-level solution [Elasticsearch](https://www.elastic.co/) or [Opensearch](https://aws.amazon.com/opensearch-service/) by AWS.
5. Hosted enterprise-level solutions: [Swiftype](https://swiftype.com/) or [Algolia](https://www.algolia.com/).
