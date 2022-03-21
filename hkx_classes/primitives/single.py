from hkx_data import HKXData
import struct


class Single:
    def __init__(self, data: HKXData, metadata: dict):
        self.value = struct.unpack('f', data.get_data(4))[0]

    def write_converted(self, data: HKXData):
        data.bytes += struct.pack('f', self.value)

    def __str__(self):
        return str(self.value)


