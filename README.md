## BookMarkIt

### Описание проекта:

Серверная часть для сервиса который хранит ссылки
пользователей(закладки) на веб-сайты.

После регистрации в сервисе пользователь может создавать различные коллекции, в которые будет добавлять свои закладки.


### Как запустить проект:

- клонировать репозиторий

```
git@github.com:ApriCotBrain/BookMarkit.git
```

- в домашней директории проекта создать файл .env по примеру .env_sample

- перейти в директорию infra

```
cd infra 
```

- запустить сборку контейнеров:

```
docker-compose up -d --build 
```

- выполнить команды:

```
docker-compose exec backend python manage.py migrate

docker-compose exec backend python manage.py collectstatic --no-input
```

После сборки контейнеров проект будет доступен по адресу:

```
http://localhost/
```

Документация доступна по адресу:

```
http://localhost/api/v1/schema/swagger-ui/
```
