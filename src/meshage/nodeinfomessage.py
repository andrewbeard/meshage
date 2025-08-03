from meshtastic.protobuf import mesh_pb2, portnums_pb2

from .config import MQTTConfig
from .message import MeshtasticMessage


class MeshtasticNodeInfoMessage(MeshtasticMessage):
    def __init__(self, config: MQTTConfig):
        self.type = portnums_pb2.NODEINFO_APP
        payload = mesh_pb2.User()
        payload.id = config.userid
        payload.short_name = "MQTT"
        payload.long_name = f"Meshage {config.userid}"
        payload.hw_model = mesh_pb2.HardwareModel.PRIVATE_HW
        payload.is_unmessagable = True

        super().__init__(payload.SerializeToString(), config)
