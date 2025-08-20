import os


def merge_files(files, output_filename='result.txt'):
    """
    Объединяет файлы в один с сортировкой по количеству строк

    :param files: список имен файлов для объединения
    :param output_filename: имя результирующего файла
    """
    # Создаем список для хранения информации о файлах
    file_info = []

    # Считываем информацию о каждом файле
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_info.append({
                'name': filename,
                'line_count': len(lines),
                'content': lines
            })

    # Сортируем файлы по количеству строк (по возрастанию)
    file_info.sort(key=lambda x: x['line_count'])

    # Записываем отсортированные файлы в результирующий файл
    with open(output_filename, 'w', encoding='utf-8') as result_file:
        for info in file_info:
            # Записываем служебную информацию (имя файла и количество строк)
            result_file.write(f"{info['name']}\n")
            result_file.write(f"{info['line_count']}\n")

            # Записываем содержимое файла
            for line in info['content']:
                result_file.write(line)

            # Добавляем пустую строку между файлами (если это не последний файл)
            if info != file_info[-1]:
                result_file.write("\n")


# Пример использования
if __name__ == "__main__":
    # Список файлов для объединения (замените на реальные имена файлов)
    files_to_merge = ['1.txt', '2.txt', '3.txt']

    # Проверяем существование файлов
    existing_files = []
    for file in files_to_merge:
        if os.path.exists(file):
            existing_files.append(file)
        else:
            print(f"Предупреждение: файл {file} не найден")

    if existing_files:
        # Объединяем файлы
        merge_files(existing_files)
        print(f"Файлы успешно объединены в result.txt")
    else:
        print("Нет файлов для объединения")
