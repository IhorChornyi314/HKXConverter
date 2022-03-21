from hkx_classes.hkx_abstract import HKXData, HKXAbstractObject
from inspect import currentframe


class SectionData(HKXAbstractObject):
    def __init__(self, data: HKXData, metadata: dict):
        self.data_objects = []
        prev_frame_vars = currentframe().f_back.f_back.f_back.f_locals
        data.position += prev_frame_vars['self'].local_fixups_offset

    def read_objects(self, data, section_metadata, virtual_fixups, classnames):
        data.position = section_metadata.absolute_data_start.value
        for i in range(section_metadata.virtual_fixups_size):
            if i < section_metadata.virtual_fixups_size - 1:
                object_size = virtual_fixups[i + 1].src.value - virtual_fixups[i].src.value
            else:
                object_size = section_metadata.exports_offset.value - virtual_fixups[i].src.value
            object_type = classnames[virtual_fixups[i].name_offset.value].value
            self.data_objects.append(HKXAbstractObject(data, {'type': object_type, 'size': object_size}))
