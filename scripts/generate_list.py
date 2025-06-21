import json
import os

def generate_numbered_list(settings):
    max_width = len(str(settings["list-length"]))  # ширина самого большого числа
    output = []

    # Заголовок и описание
    output.append(f'# {settings["title"]}')
    output.append('')
    output.append(f'## {settings["description"]}')
    output.append('')

    for i in range(1, settings["list-length"] + 1):
        number_str = str(i)
        padding_needed = max_width - len(number_str)
        padding = ' ' * padding_needed
        if not settings["formatted"]:
            line = f'{i}. {settings["list-content-template"]}'
        else:
            line = f'{padding}{i}. {settings["list-content-template"]}'

        output.append(line)

    return '\n'.join(output)

def main():
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)

        filename = settings.get("name")
        if not filename:
            raise ValueError("Отсутствует обязательное поле 'name' в файле settings.json")

        content = generate_numbered_list(settings)

        output_file = f"{filename}.md"
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Файл '{output_file}' успешно создан.")

    except FileNotFoundError:
        print("Файл 'settings.json' не найден.")
    except json.JSONDecodeError:
        print("Ошибка: Файл 'settings.json' содержит некорректный JSON.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()