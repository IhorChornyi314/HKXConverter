from hkx_data import HKXData


class Int:
    def __init__(self, data: HKXData, metadata: dict):
        self.size = metadata['size']
        self.value = int.from_bytes(data.get_data(self.size), data.endian)

    def write_converted(self, data: HKXData):
        data.bytes += self.value.to_bytes(self.size, data.endian)

    def __str__(self):
        return str(self.value)


