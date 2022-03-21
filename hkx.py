from hkx_file import HKXFile

file = open('examples/c2250-behbnd-dcx_/Action/c2250/Export/Behaviors/c2250.hkx', 'rb').read()

hk = HKXFile()
hk.read(file)
print(hk)

