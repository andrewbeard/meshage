from meshtastic.protobuf import portnums_pb2

from .config import MQTTConfig
from .message import MeshtasticMessage


class MeshtasticTextMessage(MeshtasticMessage):
    def __init__(self, payload: str, config: MQTTConfig):
        self.type = portnums_pb2.TEXT_MESSAGE_APP
        super().__init__(payload.encode("utf-8"), config)
