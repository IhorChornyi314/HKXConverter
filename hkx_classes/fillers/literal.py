from hkx_data import HKXData


class Literal:
    @staticmethod
    def read(data: HKXData, description):
        data.assert_data(int(description['value'], 16).to_bytes(len(description['value']) // 2, 'big'))

    @staticmethod
    def write(data: HKXData, description):
        data.bytes += int(description['value'], 16).to_bytes(len(description['value']) // 2, 'big')



