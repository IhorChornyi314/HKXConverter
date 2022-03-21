from hkx_data import HKXData
from hkx_section import HKXDataSection


class HKXFile:
    def __init__(self):
        self.data = None
        self.classnames = b''
        self.data_section = None

    def read(self, hkx_bytes):
        self.data = HKXData(hkx_bytes)
        self.data.position = hkx_bytes.find(b'__classnames__') + 20
        classnames_start = self.data.get_int32()
        classnames_length = self.data.get_int32()
        self.classnames = hkx_bytes[classnames_start:classnames_start + classnames_length]
        self.data_section = HKXDataSection(HKXData(self.classnames))
        self.data_section.read(self.data)

    def convert(self):
        self.data_section.convert()


