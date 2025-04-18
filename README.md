# kraken_rabbit_api

Проба работы krakend с rabbitmq

## 🚀 Технологии

- Python 3.12
- FastAPI
- SQLAlchemy
- Krakend
- Rabbitmq

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/aMironoV365/kraken_rabbit_api.git
cd kraken_rabbit_api
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## 🐳 Docker

1. Разворачивание проекта через Docker-compose:
```bash
docker-compose up --build
```

2. Открываем постман и делаем POST запрос с такой командой:
```bash
http://localhost:8080/products
```
```bash
{
  "name": "Shampoo",
  "price": 12.99,
  "description": "Nice one"
}
```


## 📊 API Endpoints

- POST /products - Создание продукта


Вывод:

1. Без KrakenD Enterprise отправлять сообщения в Rabbitmq он не будет, если верить сетке, то получив KrakenD Enterprise,
у нас появляются расширенные функции(async/amqp-producer и async/producer плагин), как раз то что нам нужно.

2. На данный момент реализовано отправление сообщений в рэббит костыльно через ручку, в RabbitMQ Management UI отображается,
что сообщения принимаются.