import os


def directory(main_dir):
    for root, dirs, files in os.walk(main_dir):
        for rand_dir in dirs:
            print(f'Имя: {str(rand_dir)}; Тип: dir')
        # print(f'Root: {root}')
        # print(f'Dirs: {dirs}')
        # print(f'Files: {files}')

        for file in files:
            file_p = os.path.join(root, file)
            weight = os.path.getsize(file_p)
            print(f'Имя: {str(file)}; Тип: file; Размер: {weight} bytes')


directory(r'..\Work')