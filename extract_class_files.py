from glob import glob
from json import dumps

diff_classes = {}
all_classes = set()
wanted_class = 'hknpCapsuleShape'
pc_class_files = [_ for _ in glob('output\\*_pc.hkc') if wanted_class in _][:15]

for pc_class_file in pc_class_files:
    pc_class = open(pc_class_file, 'rb').read()
    ps4_class = open(pc_class_file.replace('_pc', '_ps4'), 'rb').read()
    class_name = pc_class_file.split('\\')[-1].split('_')[0]
    all_classes.add(class_name)
    if pc_class != ps4_class:
        open(pc_class_file.replace('output', 'extracted'), 'wb').write(pc_class)
        open(pc_class_file.replace('output', 'extracted').replace('_pc', '_ps4'), 'wb').write(ps4_class)
