# django-benkyou

django ninja framework study

Database : docker postgreSQL  
Python : 3.8  
Python main lib : django, ninja framework, sqlalchemy  
etc : virtualenv, poetry etc...

### 환경

DB와 친하지도 않고, 백서버를 많이 경험할 일이 없어서, 구축 해보는데 목적.

Docker를 이용해 postgreSQL 데이터베이스 환경 구축
**_[PostgreSQL Sample Database(DVD RENTAL)](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/ "링크")_** 파일을 이용해 데이터 구축

파일은 **dvdrental.zip**로 첨부

Django , SQLAlchemy를 이용해 restful API server 세팅

### 환경설정

.env.template 형태처럼 docker postgreSQL 정보를 입력

```
DB_ENGINE = django.db.backends.postgresql
DB_HOST = 127.0.0.1
DB_PORT = 5432
DB_NAME = database name
DB_USER = database user name
DB_PASSWORD = data base user password

```

### 테이블 모델 정의

benkyou/inspact_db_models.py 파일 내부에 전체 테이블의 모델을 정의 되어있다.
또 새롭게 다시 정의를 하고 싶다면 아래의 명령어를 이용

```
$ python manage.py inspectdb > models.py
```

### 실행

```
$ poetry shell
$ cd benkyo
$ python manage.py runserver
```
