import aio_pika
import json
import asyncio

RABBITMQ_URL = "amqp://guest:guest@rabbitmq:5672/"
EXCHANGE_NAME = "krakend_exchange"
ROUTING_KEY = "product_created"

async def send_product_to_rabbit(product: dict):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        exchange = await channel.declare_exchange(EXCHANGE_NAME, aio_pika.ExchangeType.DIRECT, durable=True)
        message = aio_pika.Message(body=json.dumps(product).encode())
        await exchange.publish(message, routing_key=ROUTING_KEY)