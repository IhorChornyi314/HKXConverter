from hkx_classes.hkx_abstract import HKXData, HKXAbstractObject
from hkx_classes.primitives.string import String
from inspect import currentframe


class HKXClassnamesSection(HKXAbstractObject):
    def __init__(self, data: HKXData, metadata: dict):
        prev_frame_vars = currentframe().f_back.f_locals
        section_metadata = prev_frame_vars['self'].__dict__['classnames_section_header']
        self.classnames = {}
        while data.position < section_metadata.absolute_data_start.value + section_metadata.local_fixups_offset.value:
            data.position += 5
            offset = data.position - section_metadata.absolute_data_start.value
            if data.bytes[data.position] == 255:
                break
            self.classnames[offset] = String(data, {'type': 'String'})
        data.position = section_metadata.absolute_data_start.value + section_metadata.local_fixups_offset.value
        self.bytes = data.bytes[section_metadata.absolute_data_start.value:
                                section_metadata.absolute_data_start.value + section_metadata.local_fixups_offset.value]

    def write_converted(self, data: HKXData):
        data.bytes += self.bytes

