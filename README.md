# django_celery_demo

```shell
python -m venv venv
.\venv\Scripts\activate
pip install django
django-admin startproject dcelery
cd .\dcelery\
pip install celery
pip install redis
pip freeze > requirements.txt
```
#### create files needed for Docker:
docker-compose.yml
dcelery/Dockerfile

build and start the django service
```shell
docker compose up -d --build
```
