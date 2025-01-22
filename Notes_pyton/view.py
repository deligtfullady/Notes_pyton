from notes import *


def split_string(text, max_length):
    words = text.split()
    result = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= max_length:
            current_line += " " + word if current_line else word
        else:
            result.append(current_line)
            current_line = word
    if current_line:
        result.append(current_line)
    return result


def show_note(data: dict, index: str):
    print('╒═══════════╤══════════════════════════════════════╤═════════════════════╤═════════════════════╕')
    print('│ № записи  │ Имя заметки                          │ Создана             │ Изменена            │')
    print('├───────────┼──────────────────────────────────────┼─────────────────────┼─────────────────────┤')
    print('│ ', end='')
    print("{0:<10}".format(index), end='│ ')
    print("{0:<37}".format(data[index][name]), end='│ ')
    print("{0:<20}".format(data[index][time_create][:19:]), end='│ ')
    print("{0:<20}".format(data[index][time_changed][:19:]), end='│ ')
    print()
    print('├───────────┴──────────────────────────────────────┴─────────────────────┴─────────────────────┤')
    max_line = 93
    text = split_string(data[index][body], max_line)
    for i in range(len(text)):
        print('│ ', end='')
        print("{0:<93}".format(text[i]), end='│ ')
        print()
    print('╘══════════════════════════════════════════════════════════════════════════════════════════════╛')
    print()


def show_notes_list(data: dict):
    print('Список заметок')
    print('╒═══════════╤══════════════════════════════════════╤═════════════════════╤═════════════════════╕')
    print('│ № записи  │ Имя заметки                          │ Создана             │ Изменена            │')
    print('├───────────┼──────────────────────────────────────┼─────────────────────┼─────────────────────┤')
    for k in data.keys():
        print('│ ', end='')
        print("{0:<10}".format(k), end='│ ')
        print("{0:<37}".format(data[k][name]), end='│ ')
        print("{0:<20}".format(data[k][time_create][:19:]), end='│ ')
        print("{0:<20}".format(data[k][time_changed][:19:]), end='│ ')
        print()
    print('╘══════════════════════════════════════════════════════════════════════════════════════════════╛')

