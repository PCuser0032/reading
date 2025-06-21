# Укажите путь к файлу
filename = 'settings.json'

try:
    # Открываем файл для чтения
    with open(filename, 'r', encoding='utf-8') as file:
        # Читаем и выводим содержимое файла построчно
        for line in file:
            print(line, end='')  # end='', чтобы избежать двойных переносов строк
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")