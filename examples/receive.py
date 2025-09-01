#! /usr/bin/env python3
import asyncio
import logging

import aiomqtt

from meshage.config import MQTTConfig
from meshage.parser import MeshtasticMessageParser


async def main():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(message)s", level=logging.DEBUG
    )

    config = MQTTConfig()
    async with aiomqtt.Client(**config.aiomqtt_config) as client:
        await client.subscribe(config.receive_topic)
        parser = MeshtasticMessageParser(config)
        async for message in client.messages:
            parser.parse_message(message.payload)


if __name__ == "__main__":
    asyncio.run(main())
