import os


def group_rename_files(dest_name, num_digits, src_ext, dest_ext, name_range=None):
    # Получаем список файлов в текущем каталоге
    files = os.listdir()
    # Фильтруем только файлы с нужным расширением
    files = [f for f in files if os.path.isfile(f) and f.endswith(src_ext)]

    # Проверяем, есть ли диапазон сохраняемого оригинального имени
    if name_range:
        files = [f[name_range[0] - 1:name_range[1]] for f in files]

    # Создаем счетчик для порядкового номера
    count = 1

    # Переименовываем каждый файл
    for file in files:
        # Генерируем новое имя файла
        new_file_name = dest_name + str(count).zfill(num_digits) + dest_ext
        # Переименовываем файл
        os.rename(file, new_file_name)
        count += 1


group_rename_files("new_file_", 4, ".txt", ".jpg", [3, 6])