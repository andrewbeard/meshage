import asyncio

import aiomqtt

from config import MQTTConfig
from message import MeshtasticMessage


async def main():
    config = MQTTConfig()
    async with aiomqtt.Client(
        hostname=config.config["host"],
        port=config.config["port"],
        username=config.config["username"],
        password=config.config["password"],
    ) as client:
        message = MeshtasticMessage("Hello, world!", config)
        await client.publish(config.topic, bytes(message))


if __name__ == "__main__":
    asyncio.run(main())
