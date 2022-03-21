from hkx_data import HKXData
from inspect import currentframe


class SimpleArray:
    def __init__(self, data: HKXData, description):
        from hkx_object import HKXObject
        prev_frame_vars = currentframe().f_back.f_back.f_back.f_locals
        self.size = prev_frame_vars['self'].__dict__[description['name'] + '_size']
        self.data_type = description['data_type'] if description['data_type'] != 'T' else prev_frame_vars['metadata']['data_type']
        self.data = []
        for i in range(self.size):
            self.data.append(HKXObject(data, {'type': self.data_type}))

    def write_converted(self, data: HKXData):
        for data_particle in self.data:
            data_particle.write_converted(data)

    def __str__(self):
        return str(self.data)
