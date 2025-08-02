import random

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from meshtastic import BROADCAST_NUM
from meshtastic.protobuf import mesh_pb2, mqtt_pb2, portnums_pb2

from config import MQTTConfig


class MeshtasticMessage:
    def __init__(self, payload: bytes | str, config: MQTTConfig):
        self.config = config
        if isinstance(payload, str):
            self.payload = payload.encode("utf-8")
        else:
            self.payload = payload
        self.message_id = self.generate_message_id()

    def generate_message_id(self) -> int:
        return random.getrandbits(32)

    def encrypt_packet(self, packet: mesh_pb2.MeshPacket) -> bytes:
        # Wrap payload in Data protobuf message
        data_msg = mesh_pb2.Data()
        data_msg.portnum = portnums_pb2.TEXT_MESSAGE_APP
        data_msg.payload = self.payload
        data_msg.bitfield = 1

        nonce_packet_id = packet.id.to_bytes(8, "little")
        nonce_from_node = getattr(packet, "from").to_bytes(8, "little")
        nonce = nonce_packet_id + nonce_from_node
        cipher = Cipher(algorithms.AES(self.config.key), modes.CTR(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(data_msg.SerializeToString()) + encryptor.finalize()

    def packet(self) -> mesh_pb2.MeshPacket:
        packet = mesh_pb2.MeshPacket()
        packet.id = self.message_id
        setattr(packet, "from", self.config.config["userid"])  # from is a reserved keyword
        packet.to = BROADCAST_NUM
        packet.want_ack = False
        packet.channel = self.config.encoded_channel
        packet.hop_limit = 3
        packet.hop_start = 3
        packet.encrypted = self.encrypt_packet(packet)
        return packet

    def service_envelope(self, packet: mesh_pb2.MeshPacket) -> mqtt_pb2.ServiceEnvelope:
        envelope = mqtt_pb2.ServiceEnvelope()
        envelope.packet.CopyFrom(packet)
        envelope.channel_id = self.config.config["channel"]
        envelope.gateway_id = self.config.userid
        return envelope

    def __bytes__(self) -> bytes:
        return self.service_envelope(self.packet()).SerializeToString()