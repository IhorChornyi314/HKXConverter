from os import system


class BNDConverter:
    def __init__(self, bnd_path):
        self.bnd_file_name = bnd_path.replace('\\', '/').split('/')[-1]
        self.bdn_path = bnd_path

    def unpack_bnd(self):
        system('BinderTool ' + self.bdn_path)

    def repack_folder(self):
        system('BinderTool ' + self.bnd_file_name)

    def convert(self):
        self.unpack_bnd()




