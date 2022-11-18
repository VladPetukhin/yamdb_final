# yamdb_final
yamdb_final
Описание
Проект YaMDb собирает отзывы пользователей на различные произведения.

Как он работает
Позволяет взаимодействовать с эндпоинтами api_yamdb посредством отправки и получения стандартных json GET, POST, PUT, PATCH, DELETE запросов. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором. Хранятся только ревью на произведения. В каждой категории есть произведения. Произведению может быть присвоен жанр. Любой пользователь может оставить к произведениям текстовые отзывы и оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Документация к API доступна по адресу http://127.0.0.1/redoc/

Установка
Шаг 1. Проверьте установлен ли у вас Docker

Шаг 2. Клонируйте репозиторий себе на компьютер

Шаг 3. Создайте файл .env

Пример:

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=password # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 

Шаг 4. Запустите docker-compose
Для запуска необходимо выполнить из директории infra с файлом docker-compose.yaml команду:

docker-compose up -d

Шаг 5. База данных
Создайте и примените миграции последовательными командами:

docker-compose exec web python manage.py makemigrations users
docker-compose exec web python manage.py makemigrations reviews

docker-compose exec web python manage.py migrate


Шаг 6. Подгрузите статику

docker-compose exec web python manage.py collectstatic

Шаг 7. Заполнените базу тестовыми данными
Для заполнения базы тестовыми данными можно использовать Management command  load_data_new. Выполните команду:

docker-compose exec web python manage.py load_data_new

Шаг 8. Дополнительные команды
Создание суперюзера

docker-compose exec web python manage.py createsuperuser

Остановить и удалить контейнеры

docker-compose down -v
![Push event](https://github.com/github/docs/actions/workflows/yamdb_workflow.yml/badge.svg?event=push )

