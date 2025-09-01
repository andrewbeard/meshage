#! /usr/bin/env python3
import asyncio

import aiomqtt

from meshage.config import MQTTConfig
from meshage.messages import MeshtasticNodeInfoMessage, MeshtasticTextMessage


async def main():
    config = MQTTConfig()
    async with aiomqtt.Client(**config.aiomqtt_config) as client:
        message = MeshtasticNodeInfoMessage(config)
        await client.publish(config.publish_topic, bytes(message))
        message = MeshtasticTextMessage("Hello, world!", config)
        await client.publish(config.publish_topic, bytes(message))


if __name__ == "__main__":
    asyncio.run(main())
