#!/usr/bin/env python3

# Фразы для пользователей
MENU_QUESTIONS = ('>> Меню:\n[1] - Удалить метаданные\n'
            '[2] - Изменить дату создания файла\n'
            '[3] - Изменить дату последнего изменения файла\n'
            '[4] - Выход\n'
            '>> Выберите пункт: ')

COMMAND_1 = '1'
COMMAND_2 = '2'
COMMAND_3 = '3'
COMMAND_4 = '4'

EXIT = 'ВЫХОД'

COMMAND_DELETE = '>> Удаление метаданных'
ASK_FILE_PATH = '>> Укажите путь к файлу: '
INVALID_PATH = '>> Файл не существует'
INVALID_EXTENSION = '>> Неподдерживаемый формат файла'
ASK_TO_MENU = '>> Хотите вернуться в главное меню(да)?\n>> '
YES = 'да'
DELETED = '>> Метаданные удалены'
COMMAND_EDIT_CREATE = '>> Изменение даты создания файла'
ASK_CREATE_DATE = '>> Укажите новую дату создания файла (ГГГГ:ММ:ДД): '
ASK_CREATE_TIME = '>> Укажите новое время создания файла (ЧЧ:ММ:СС): '
INFO_DATETIME = '>> Вы выбрали новую дату:'
ASK_DATE_TIME = '>> Хотите продолжить(да)?\n>> '
ABORT = '>> Операция прервана'
CHANGE_CREATION = '>> Дата создания файла изменена'
COMMAND_EDIT_CHANGE = '>> Изменение даты внесения последних изменнений в файл'
CHANGE_CHANGE = '>> Дата последнего доступа к файлу изменена'
OOPS = '>> Что-то пошло не так!'
