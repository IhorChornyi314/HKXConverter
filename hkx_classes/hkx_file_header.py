from hkx_classes.hkx_abstract import HKXData, HKXAbstractObject


class HKXFileHeader(HKXAbstractObject):
    def __init__(self, data: HKXData, metadata: dict):
        super().__init__(data, metadata)
        data.endian = 'little' if self.endian.value == 1 else 'big'
        data.position = self.class_name_section_offset.value + 64


