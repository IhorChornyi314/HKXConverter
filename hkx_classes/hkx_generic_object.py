from hkx_data import HKXData


class HKXGenericObject:
    def __init__(self, data: HKXData, metadata: dict):
        from hkx_object import HKXObject
        self.__dict__ = HKXObject(data, metadata).__dict__


