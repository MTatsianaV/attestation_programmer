import json
from datetime import datetime

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('notes.json', 'r') as file:
            data = file.read()
            if not data:
                notes = []
            else:
                notes = json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError):
        notes = []
    return notes

# Функция для записи заметок в файл
def write_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': str(datetime.now())
    }
    notes.append(note)
    write_notes(notes)
    print("Заметка успешно сохранена")

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = str(datetime.now())
            write_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным ID не найдена")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            write_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным ID не найдена")

# Функция для вывода списка заметок
def display_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")
        print()

# Функция для фильтрации заметок по дате
def filter_notes_by_date():
    date_str = input("Введите дату (в формате ГГГГ-ММ-ДД): ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S.%f") >= date]
        if filtered_notes:
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Тело: {note['body']}")
                print(f"Дата/время: {note['timestamp']}")
                print()
        else:
            print("Заметки за указанную дату не найдены")
    except ValueError:
        print("Некорректный формат даты")

# Основной код программы
notes = read_notes()

while True:
    command = input("Введите команду (add, edit, delete, display, filter, exit): ")

    if command == 'add':
        add_note()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'display':
        display_notes()
    elif command == 'filter':
        filter_notes_by_date()
    elif command == 'exit':
        break
    else:
        print("Некорректная команда")