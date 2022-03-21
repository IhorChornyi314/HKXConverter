from hkx_data import HKXData
from hkx_classes import *


class HKXDataSection:
    def __init__(self, classnames_data: HKXData):
        self.data = b''
        self.classnames_data = classnames_data
        self.absolute_data_start = 0
        self.local_fixups_offset = 0
        self.global_fixups_offset = 0
        self.virtual_fixups_offset = 0
        self.exports_offset = 0
        self.imports_offset = 0
        self.end_offset = 0

        self.local_fixups = []
        self.global_fixups = []
        self.virtual_fixups = []
        self.objects = []

    def read_metadata(self, data: HKXData):
        data.position = data.bytes.find(b'__data__\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff') + 20
        self.absolute_data_start = data.get_int32()
        self.local_fixups_offset = data.get_int32()
        self.global_fixups_offset = data.get_int32()
        self.virtual_fixups_offset = data.get_int32()
        self.exports_offset = data.get_int32()
        self.imports_offset = data.get_int32()
        self.end_offset = data.get_int32()

    def read_fixups(self, data: HKXData):
        data.position = self.absolute_data_start + self.local_fixups_offset
        self.local_fixups = [
            (data.get_int32(), data.get_int32()) for _ in range(self.local_fixups_offset, self.global_fixups_offset, 8)
        ]

        data.position = self.absolute_data_start + self.global_fixups_offset
        self.global_fixups = [
            (data.get_int32(), data.get_int32(), data.get_int32()) for _ in range(self.global_fixups_offset, self.virtual_fixups_offset, 12)
        ]

        data.position = self.absolute_data_start + self.virtual_fixups_offset
        self.virtual_fixups = [
            (data.get_int32(), data.get_int32(), data.get_int32()) for _ in range(self.virtual_fixups_offset, self.exports_offset, 12)
        ]

    def read_objects(self, data: HKXData):
        for i in range(len(self.virtual_fixups)):
            object_end = self.virtual_fixups[i + 1][0] if i < len(self.virtual_fixups) - 1 else self.local_fixups_offset
            object_class = self.classnames_data.get_str(self.virtual_fixups[i][2])
            if object_class not in globals():
                object_class = 'hkxGeneric'
            object_bytes = data.bytes[self.absolute_data_start + self.virtual_fixups[i][0]:self.absolute_data_start + object_end]
            self.objects.append(globals()[object_class](object_bytes))

    def read(self, data: HKXData):
        self.read_metadata(data)

        self.data = data.bytes[self.absolute_data_start:self.absolute_data_start + self.local_fixups_offset]

        self.read_fixups(data)
        # data.assert_data(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
        self.read_objects(data)

    def convert(self):
        for hkx_object in self.objects:
            hkx_object.convert()






