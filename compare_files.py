from glob import glob
from tqdm import tqdm

ps4_dir = 'C:/DS3 PS4/Image0/dvdroot_ps4\\'
pc_dir = 'D:/Steam/steamapps/common/DARK SOULS III/Game\\'
formats = []

ps4_files = [f.replace(ps4_dir, '') for f in glob(ps4_dir + '**', recursive=True) if '.' in f]
pc_files = [f.replace(pc_dir, '') for f in glob(pc_dir + '**', recursive=True) if '.' in f]

for file in ps4_files:
    if sum([1 if f in file else 0 for f in formats]) > 0:
        continue
    ps4_bytes = open(ps4_dir + file, 'rb').read()
    try:
        pc_bytes = open(pc_dir + file, 'rb').read()
    except FileNotFoundError:
        print('File %s not present in pc version\n' % file)
        continue

    if len(ps4_bytes) > len(pc_bytes):
        print('PS4 file is longer than pc!')
        print(file)

        if ps4_bytes[:len(pc_bytes)] != pc_bytes:
            print('Difference detected! PS4 longer')
            print(file)
            formats.append(file[file.index('.'):])
            print()
    else:
        if ps4_bytes != pc_bytes[:len(ps4_bytes)]:
            print('Difference detected! PC longer')
            print(file)
            formats.append(file[file.index('.'):])
            print()


