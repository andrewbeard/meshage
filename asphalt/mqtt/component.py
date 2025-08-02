import logging
from collections.abc import AsyncGenerator
from typing import Any

import aiomqtt
from asphalt.core import Component, Context, context_teardown

logger = logging.getLogger(__name__)

class MQTTComponent(Component):
    def __init__(
        self,
        *,
        resource_name: str = "default",
        **kwargs: Any,
    ):
        self.client = aiomqtt.Client(**kwargs)
        self.resource_name = resource_name

    @context_teardown
    async def start(self, ctx: Context) -> AsyncGenerator[None, Any]:
        async with self.client as client:
            ctx.add_resource(client, self.resource_name)

        yield
        logger.info("MQTT client shut down")
