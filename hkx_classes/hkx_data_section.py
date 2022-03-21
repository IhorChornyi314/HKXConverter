from hkx_classes.hkx_abstract import HKXData, HKXAbstractObject
from inspect import currentframe


class HKXDataSection(HKXAbstractObject):
    def __init__(self, data: HKXData, metadata: dict):
        prev_frame_vars = currentframe().f_back.f_locals
        section_metadata = prev_frame_vars['self'].data_section_header
        classnames = prev_frame_vars['self'].classnames_section.classnames

        self.local_fixups_offset = section_metadata.local_fixups_offset.value
        self.local_fixups_size = section_metadata.local_fixups_size
        self.global_fixups_size = section_metadata.global_fixups_size
        self.virtual_fixups_size = section_metadata.virtual_fixups_size

        super().__init__(data, {'type': 'HKXSection'})
        self.data_objects.read_objects(data, section_metadata, self.virtual_fixups.data, classnames)

    def write_converted(self, data: HKXData):
        self.data_objects.write_objects(data)
        

