from glob import glob
from tqdm import tqdm
from os import mkdir


def read_hkx_objects(filename):
    hkx_bytes = open(filename, 'rb').read()
    header_start = hkx_bytes.find(b'__classnames__')
    absolute_data_start = int.from_bytes(hkx_bytes[148 + header_start:152 + header_start], 'little')
    local_fixups_offset = int.from_bytes(hkx_bytes[152 + header_start:156 + header_start], 'little')
    virtual_fixups_offset = int.from_bytes(hkx_bytes[160 + header_start:164 + header_start], 'little')
    exports_offset = int.from_bytes(hkx_bytes[164 + header_start:168 + header_start], 'little')

    virtual_fixups = []

    for i in range(virtual_fixups_offset, exports_offset, 12):
        index = i + absolute_data_start
        if hkx_bytes[index:index + 4] == b'\xff\xff\xff\xff':
            continue
        virtual_fixups.append({
            'src': int.from_bytes(hkx_bytes[index:index + 4], 'little'),
            'section_index': int.from_bytes(hkx_bytes[index + 4:index + 8], 'little'),
            'name_offset': int.from_bytes(hkx_bytes[index + 8:index + 12], 'little')
        })

    objects = []

    for i, virtual_fixup in zip(range(len(virtual_fixups)), virtual_fixups):
        name_start = 192 + header_start + virtual_fixup['name_offset']
        name_length = hkx_bytes[192 + header_start + virtual_fixup['name_offset']:].find(b'\x00')
        class_name = hkx_bytes[name_start:name_start + name_length].decode()
        data = hkx_bytes[
               absolute_data_start + virtual_fixup['src']:
               (absolute_data_start + virtual_fixups[i + 1]['src'] if i < len(
                   virtual_fixups) - 1 else absolute_data_start + local_fixups_offset)
               ]

        objects.append({'class_name': class_name, 'data': data})

    return objects


def get_different_names(filename):
    pc_hkx = read_hkx_objects('files/pc/%s' % filename)
    ps4_hkx = read_hkx_objects('files/ps4/%s' % filename)
    global names, all_names
    for pc_hkx_object, ps4_hkx_object in zip(pc_hkx, ps4_hkx):
        if pc_hkx_object['data'] != ps4_hkx_object['data']:
            open('output/pc/%s.hkc' % pc_hkx_object['class_name'], 'wb').write(pc_hkx_object['data'])
            open('output/ps4/%s.hkc' % ps4_hkx_object['class_name'], 'wb').write(ps4_hkx_object['data'])
            print(filename)
            print(pc_hkx_object)
            print(ps4_hkx_object)
            print(pc_hkx_object['class_name'])
            names.add(pc_hkx_object['class_name'])
            print()
        all_names.add(pc_hkx_object['class_name'])
    return names


def get_byte_comparison(filename, bytes_comparison_data):
    pc_hkx = read_hkx_objects('files/pc/%s' % filename)
    ps4_hkx = read_hkx_objects('files/ps4/%s' % filename)
    for pc_hkx_object, ps4_hkx_object in zip(pc_hkx, ps4_hkx):
        if pc_hkx_object['data'] != ps4_hkx_object['data']:
            if pc_hkx_object['class_name'] not in bytes_comparison_data:
                bytes_comparison_data[pc_hkx_object['class_name']] = []
            bytes_comparison_data[pc_hkx_object['class_name']].append((pc_hkx_object['data'], ps4_hkx_object['data'], filename))
    return bytes_comparison_data


def populate_output():
    files = [f.split('\\')[-1] for f in glob('files/pc/*.hkx') + glob('files/pc/*.HKX')]
    output = {}
    for file in tqdm(files):
        output = get_byte_comparison(file, output)
    for class_name in tqdm(output):
        for i in range(len(output[class_name])):
            try:
                mkdir('output/%s/' % class_name)
            except:
                pass
            open('output/%s/%s_%d_pc.hkc' % (class_name, output[class_name][i][2], i), 'wb').write(output[class_name][i][0])
            open('output/%s/%s_%d_ps4.hkc' % (class_name, output[class_name][i][2], i), 'wb').write(output[class_name][i][1])


# populate_output()

a = read_hkx_objects('c9997.hkx')
print(a)
