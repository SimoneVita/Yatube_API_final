### Привет!
Данный проект разработан, чтобы усовершенствовать работу проекта Yatube и добавить в его функционал возможность работы с API.
Доступны API для публикаций, групп, комментариев и подписок.
Лимит запросов к API пока не установлен.

### Примеры запросов.

Доступные эндпоинты:
```
GET: /api/v1/posts/
POST: /api/v1/posts/
GET: /api/v1/posts/{id}/
PUT: /api/v1/posts/{id}/
PATCH: /api/v1/posts/{id}/
DELETE: /api/v1/posts/{id}/
GET: /api/v1/posts/{post_id}/comments/
POST: /api/v1/posts/{post_id}/comments/
GET: /api/v1/posts/{post_id}/comments/{id}/
PUT: /api/v1/posts/{post_id}/comments/{id}/
PATCH: /api/v1/posts/{post_id}/comments/{id}/
DELETE: /api/v1/posts/{post_id}/comments/{id}/
GET: /api/v1/groups/
GET: /api/v1/groups/{id}/
GET: /api/v1/follow/
POST: /api/v1/follow/
POST: /api/v1/jwt/create/
POST: /api/v1/jwt/refresh/
POST: /api/v1/jwt/verify/
```

Пример POST запроса для получения токена:
```
/api/v1/jwt/create
{
    "username": "username",
    "password": "password"
}
```

Пример POST запроса к api/v1/posts:
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:SimoneVita/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate 
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
