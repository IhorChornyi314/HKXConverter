from hkx_classes.hkx_abstract import HKXData, HKXAbstractObject
from inspect import currentframe


class HKXSection(HKXAbstractObject):
    def __init__(self, data: HKXData, metadata: dict):
        prev_frame_vars = currentframe().f_back.f_locals
        section_metadata = prev_frame_vars['self'].__dict__[metadata['section_name'] + '_section_header']

        self.local_fixups_size = section_metadata.local_fixups_size
        self.global_fixups_size = section_metadata.global_fixups_size
        self.virtual_fixups_size = section_metadata.virtual_fixups_size
        super().__init__(data, metadata)

        self.section_data.read_objects(data, section_metadata)

