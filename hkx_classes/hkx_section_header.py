from hkx_classes.hkx_abstract import HKXData, HKXAbstractObject


class HKXSectionHeader(HKXAbstractObject):
    def __init__(self, data: HKXData, metadata: dict):
        super().__init__(data, metadata)
        self.local_fixups_size = (self.global_fixups_offset.value - self.local_fixups_offset.value) // 8
        self.global_fixups_size = (self.virtual_fixups_offset.value - self.global_fixups_offset.value) // 12
        self.virtual_fixups_size = (self.exports_offset.value - self.virtual_fixups_offset.value) // 12



