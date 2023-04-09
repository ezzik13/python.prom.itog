from functions import get_notes_from_json, write_notes_to_json, table
import datetime

class Client:
    commannds = {
            1: "Посмотреть список заметок",
            2: "Создать заметку",
            3: "Удалить заметку",
            4: "Изменить заметку",
            5: "Посмотреть заметку",
            6: "Отобразить заметки выбранной даты"
        }

    def add_note():
        notes = get_notes_from_json()
        notes[int(list(notes.keys())[-1]) + 1] = {
            "name": input("Введите заголовок заметки "),
            "body": input("Текст заметки: "),
            "date": str(datetime.datetime.now())
        }
        write_notes_to_json(notes)
        
    
    def remove_note(note_id):
        notes = get_notes_from_json()
        if note_id in notes.keys():
            for key, a in notes.items():
                if key  == note_id:
                    del notes[key]
                    break
            write_notes_to_json(notes)
        else: print("такой заметки нет")
        
    def print_note(note_id):
        if note_id in notes.keys():
            notes = get_notes_from_json()
            for key, a in notes.items():
                if key  == note_id:
                    print(a["body"])
        else: print("такой заметки нет")

    
    def view_notes():
        headers = {"id": "ID", "name": "Наименование",  "date": "Дата"}
        notes = get_notes_from_json()
        temp = []
        for key, value in notes.items():
            temp.append({
                "id": key,
                "name": value["name"],
                "date": value["date"],
            })
        print(table(headers, temp))

    def change_notes(note_id):

        notes = get_notes_from_json()
        if note_id in notes.keys():
            notes[note_id] = {
                "name": input("Введите заголовок заметки "),
                "body": input("Текст заметки: "),
                "date": str(datetime.datetime.now())
            }
            write_notes_to_json(notes)
        else: print("такой заметки нет")

    def print_notes_date(date_from):
        headers = {"id": "ID", "name": "Наименование",  "date": "Дата"}
        notes = get_notes_from_json()
        for key, a in notes.items():
            if date_from  in a["date"]:
                temp = []
                temp.append({
                    "id": key,
                    "name": a["name"],
                    "date": a["date"],
                })
                print(table(headers, temp))
    
    def do_command(command):
        if command in [str(item) for item in Client.commannds.keys()]:
            if command == "1":
                Client.view_notes()
            elif command == "2":
                Client.add_note()
            elif command == "3":
                Client.remove_note(input("Введите id заметки: "))
            elif command == "4":
                Client.change_notes(input("Введите id заметки: "))
            elif command == "5":
                Client.print_note(input("Введите id заметки: "))
            elif command == "6":
                Client.print_notes_date(input("Введите искомую дату(гггг-мм-дд): "))

        else:
            print("Invalid command")

    def print_commands():
        for key, command in Client.commannds.items():
            print(f"{key} - {command}")



