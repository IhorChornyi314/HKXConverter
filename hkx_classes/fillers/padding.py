from hkx_data import HKXData


class Padding:
    @staticmethod
    def read(data: HKXData, description):
        if data.position % description['align'] != 0:
            data.assert_data(b'\x00' * (description['align'] - data.position % description['align']))

    @staticmethod
    def write(data: HKXData, description):
        if data.position % description['align'] != 0:
            data.bytes += b'\x00' * (description['align'] - data.position % description['align'])



