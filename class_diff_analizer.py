from glob import glob
from json import dumps

diff_classes = {}
all_classes = set()
pc_class_files = glob('output/*_pc.hkc')
for pc_class_file in pc_class_files:
    pc_class = open(pc_class_file, 'rb').read()
    ps4_class = open(pc_class_file.replace('_pc', '_ps4'), 'rb').read()
    class_name = pc_class_file.split('\\')[-1].split('_')[0]
    all_classes.add(class_name)
    if pc_class != ps4_class:
        if class_name not in diff_classes:
            print('Diff class', class_name)
            sum_equal = sum(list(pc_class)) == sum(list(ps4_class))
            len_equal = len(pc_class) == len(ps4_class)
            diff_classes[class_name] = {
                'sum_equal': sum_equal,
                'len_equal': len_equal
            }
        else:
            sum_equal = sum(list(pc_class)) == sum(list(ps4_class))
            len_equal = len(pc_class) == len(ps4_class)
            if not sum_equal and diff_classes[class_name]['sum_equal']:
                diff_classes[class_name]['sum_equal'] = False
            if not len_equal and diff_classes[class_name]['len_equal']:
                diff_classes[class_name]['len_equal'] = False

print(dumps(diff_classes, indent=4))
print('Total classes: %d, diff classes: %d' % (len(all_classes), len(diff_classes.keys())))
open('result.json', 'w').write(dumps(diff_classes, indent=4))




