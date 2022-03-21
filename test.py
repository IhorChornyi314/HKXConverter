from hkx_data import HKXData
from hkx_object import HKXObject

read_data = HKXData()
read_data.read_file('c3040_c.hkx')
obj = HKXObject(read_data, {'type': 'HKXFile'})

read_data = HKXData()
read_data.read_file('c3040_c_conv.hkx')
obj_onv = HKXObject(read_data, {'type': 'HKXFile'})

print('1')

