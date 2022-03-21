from hkx_data import HKXData


class String:
    def __init__(self, data: HKXData, metadata: dict):
        length = metadata['length'] if 'length' in metadata else data.bytes[data.position:].find(b'\0') + 1
        self.value = data.get_data(length).decode('utf8').replace('\x00', '')

    def write_converted(self, data: HKXData):
        data.bytes += self.value.encode('utf8')

    def __str__(self):
        return self.value

