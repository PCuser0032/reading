import json
import os


def determine_prefix_length(max_number):
    """Определяет длину самого длинного числа в списке"""
    return len(str(max_number))


def generate_list_items(length, formatted):
    """Генерирует элементы списка с нужным количеством пробелов для выравнивания"""
    if formatted:
        max_prefix = determine_prefix_length(length)
        items = []
        for i in range(1, length + 1):
            prefix = str(i) + "."
            padding = " " * (max_prefix - len(str(i)) + 1)
            items.append(f"{padding}{prefix} []()")
        return items
    else:
        return [f"{i}. []()" for i in range(1, length + 1)]


def create_markdown_file(settings):
    """Создает markdown-файл на основе настроек"""
    lines = [
        f"# {settings['title']}",
        "",
        f"## {settings['description']}",
        ""
    ]

    lines.extend(generate_list_items(
        settings["list-length"], settings["formatted"]))

    filename = f"{settings['name']}.md"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Файл '{filename}' успешно создан.")


def main():
    """Основная функция"""
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)

        # Проверка структуры JSON
        required_fields = ["name", "title",
                           "description", "list-length", "formatted"]
        for field in required_fields:
            if field not in settings:
                raise ValueError(
                    f"Отсутствует обязательное поле '{field}' в файле settings.json")

        if not isinstance(settings["list-length"], int) or settings["list-length"] <= 0:
            raise ValueError(
                "Поле 'list-length' должно быть положительным целым числом")

        if not isinstance(settings["formatted"], bool):
            raise ValueError(
                "Поле 'formatted' должно иметь логическое значение (true/false)")

        create_markdown_file(settings)

    except FileNotFoundError:
        print("Файл 'settings.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Файл 'settings.json' содержит некорректный JSON.")
    except ValueError as e:
        print(f"Ошибка в настройках: {e}")


if __name__ == "__main__":
    main()
