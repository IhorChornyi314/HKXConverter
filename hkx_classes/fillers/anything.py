from hkx_data import HKXData
from inspect import currentframe


class Anything:
    def __init__(self, data: HKXData, description):
        prev_frame_vars = currentframe().f_back.f_locals
        self.size = prev_frame_vars['metadata']['size']
        l_offset = description['l_offset'] if 'l_offset' in description else 0
        r_offset = description['r_offset'] if 'r_offset' in description else 0
        self.bytes = data.get_data(self.size - l_offset - r_offset)

    def write_converted(self, data: HKXData):
        data.bytes += self.bytes

    def __str__(self):
        return str(self.bytes)
