# Тестовое задание для kt.team
## Конфигурация:
Копируем `.env.example` и меняем имя на `.env`. Настраиваем под себя.
```
API_KEY - ключ API сервиса с валютой
TASK_TIME_MINUTES - Время для задержки таски для получения котировки.
```
## Запуск:
```shell script
docker-compose build && docker-compose up
```

## Проверка:
- http://127.0.0.1:8000/ сервис доступен по этому адресу
- http://127.0.0.1:8000/docs тут вся докума(сваггер). Можно протестировать запросы.

## Сборка:
- FastAPI в качестве основного сервиса.
- PostgreSQL база данных
- Celery для тасок
- Redis как брокер

## PS
- В докер композе открыто лежат коннекты к БД. Я с докер композером не работаю, поэтому так.
- `/app/wait` спасибо докер композеру за это.
- Тесты я не стал писать, и так много времени ушло на тестовое задание.
- Документация тут тоже отдельно излишне. Есть сваггер и все названия переменных и методов говорящие.
- Исходя из написанного вами `Наше тестовое сделано таким образом, что по результату его исполнения вы изучите много нового.` нового я ничего не встретил. Поэтому FastAPI. С ним опыта меньше всего, поэтому было интересно)


```¯\_(ツ)_/¯ Вот и все.```