#! /usr/bin/env python3
import asyncio

import aiomqtt

from config import MQTTConfig
from message import MeshtasticMessage


async def main():
    config = MQTTConfig()
    async with aiomqtt.Client(**config.aiomqtt_config) as client:
        message = MeshtasticMessage("Hello, world!", config)
        await client.publish(config.topic, bytes(message))


if __name__ == "__main__":
    asyncio.run(main())
