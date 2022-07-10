# django_study_seventh

My another practice project in Django and HTML


This is typical project on Django.


Features:
1) Some kind of game portal with posts from authorized users (with Bootstrap already-in);
2) Custom logging (need to uncomment LOGGING option in settings.py)
3) Created category with at least 1 news will be added in sidebar automatically (with counter of amount of news);
4) Reworked auth: unique and required email for each account;
5) Account verification via email;
6) Personal page for each account;
7) Commentary for each news;
8) Comment shows up after author accept;
9) Email notification for author about new comment;
10) Weekly user notification about some news on portal.

Requirements: 
1) In requirements.txt file (Docker install everything automatically);
2) Create file "keys.py" in root project directory with parameters: 
- DJANGO_KEY (put your own pre-made Django token in it)
- SMTP_SERVER = *smtp.smtp_server.com*
- MAIL_USER = *mail_login*
- MAIL_SERVICE = *@mail_domain.com*
- MAIL_PASSWORD = *mail_password*
3) Create file ".env" in root project directory with parameters:
- DJANGO_PORT=*port number*
- DOCKER_EXPOSE_PORT=*port number*
- DJANGO_ALLOWED_HOSTS=*host list* (f.e. "127.0.0.1")

properly installed docker on your machine
For starting server use command in project root directory:
*docker-compose up*
After properly started cluster of three containers (Django, Redis and Celery) you can access project web-interface on localhost address with standard port 8000 (127.0.0.1:8000).


Made for final practice exercise in chapter "Django and backend" for SkillFactory

Superuser:
~~login: 
password:~~ (don't need anymore)

Just create superuser by yourself after first migration.


For education purpose only. Workability is not guarantee.

If you'll have suggestions or encounter errors in project, do not hesitate to contact me, please.

Made by IvanDamNation (a.k.a. IDN) GNU General Public License v3, 2022
