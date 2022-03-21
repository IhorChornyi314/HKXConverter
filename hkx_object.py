from hkx_data import HKXData
from hkx_classes import *
import json


class HKXObject:
    def __init__(self, data: HKXData, metadata: dict):
        self.type = metadata['type']
        try:
            read_manifest = json.load(open('manifests/ps4/%s.json' % self.type))
        except FileNotFoundError:
            read_manifest = json.load(open('manifests/ps4/HKXGenericObject.json'))
        for var, description in read_manifest.items():
            description['name'] = var
            if description['type'] != 'Padding' and description['type'] != 'Literal':
                hk_class = globals()[description['type']] if description['type'] in globals() else HKXObject
                self.__dict__[var] = hk_class(data, description)
            else:
                globals()[description['type']].read(data, description)

    def write_converted(self, data: HKXData):
        write_manifest = json.load(open('manifests/pc/%s.json' % self.type))
        for var, description in write_manifest.items():
            if description['type'] != 'Padding' and description['type'] != 'Literal':
                self.__dict__[var].write_converted(data)
            else:
                globals()[description['type']].write(data, description)




