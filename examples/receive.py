#! /usr/bin/env python3
import asyncio
import logging

import aiomqtt

from meshage.config import MQTTConfig
from meshage.messages import MeshtasticTextMessage
from meshage.parser import MeshtasticMessageParser


async def main():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO
    )

    config = MQTTConfig()
    async with aiomqtt.Client(**config.aiomqtt_config) as client:
        await client.subscribe(config.receive_topic)
        parser = MeshtasticMessageParser(config)
        async for message in client.messages:
            parsed_message = parser.parse_message(message.payload)
            if isinstance(parsed_message, MeshtasticTextMessage):
                logging.info(f"Received text message: {parsed_message.text}")


if __name__ == "__main__":
    asyncio.run(main())
