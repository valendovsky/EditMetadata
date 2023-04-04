#!/usr/bin/env python3

import os
import time
from exif import Image
from win32_setctime import setctime

import phrases as phr


# Получает путь к файлу
def get_file_path():
    file_path = input(phr.ASK_FILE_PATH)
    return file_path


# Проверяет путь к файлу
def check_file_path(file_path):
    if not os.path.exists(file_path):
        print(phr.INVALID_PATH)
        return False
    else:
        # Проверка расширения файла
        if file_path.endswith(".jpg"):
            return True
        elif file_path.endswith(".jpeg"):
            return True
        else:
            print(phr.INVALID_EXTENSION)
            return False


# Получает объект exif.Image
def get_image(file_path):
    with open(file_path, 'rb') as file:
        return Image(file)


# Сохрянет новый exif.Image в файл
def save_image(file_path, image):
    with open(file_path, 'wb') as file:
        file.write(image.get_file())


# Удаляет метаданные
def delete_metadata(file_path):
    image = get_image(file_path)
    image.delete_all()
    save_image(file_path, image)
    print(phr.DELETED)


# Получает новую дату от пользователя
def get_new_datetime():
    while True:
        new_date = input(phr.ASK_CREATE_DATE)
        new_time = input(phr.ASK_CREATE_TIME)
        new_datetime = new_date + ' ' + new_time
        print(phr.INFO_DATETIME, new_datetime)
        
        result = input(phr.ASK_DATE_TIME)
        if result.lower() == phr.YES:
            return new_datetime
        else:
            print(phr.ABORT)
            return None


# Получает время в POSIX
def get_posix_time(date_time):
    return int(time.mktime(time.strptime(date_time, '%Y:%m:%d %H:%M:%S')))


# Изменяет дату создания файла
def edit_creation_date(file_path):
    # Получаем новую дату
    new_datetime = get_new_datetime()
    if not new_datetime:
        return
    
    # Получаем объект exif.Image и изменяем дату создания
    image = get_image(file_path)
    image.datetime = new_datetime
    image.datetime_digitized = new_datetime
    image.datetime_original = new_datetime
    save_image(file_path, image)
    
    # Изменяем st_ctime
    epoch_datetime = get_posix_time(new_datetime)
    setctime(file_path, epoch_datetime)
    print(phr.CHANGE_CREATION)


# Изменяет дату последнего изменения файла
def edit_change_date(file_path):
    # Получаем новую дату
    new_datetime = get_new_datetime()
    if not new_datetime:
        return
    
    # Изменяем параметры atime и mtime
    epoch_datetime = get_posix_time(new_datetime)
    os.utime(file_path, (epoch_datetime, epoch_datetime))
    print(phr.CHANGE_CHANGE)


# Запрашивает адрес файла и применяет к нему переданную функцию
def event_command(func):
    try:
        while True:
            file_path = get_file_path()
            check_result = check_file_path(file_path)
        
            # Проверка существования файла
            if check_result:
                func(file_path)
                return
            else:
                # Выход в главное меню
                command = input(phr.ASK_TO_MENU)
                if command.lower() == phr.YES: return
    except Exception:
        print(phr.OOPS)


# Обрабатывает событие удаления метаданных
def delete_command():
    print(phr.COMMAND_DELETE)
    event_command(delete_metadata)


# Обрабатывает событие изменения даты создания файла
def edit_creation_command():
    print(phr.COMMAND_EDIT_CREATE)
    event_command(edit_creation_date)


# Обрабатывает событие изменения даты последнего доступа к файлу
def edit_change_command():
    print(phr.COMMAND_EDIT_CHANGE)
    event_command(edit_change_date)


# Выбор действий
def menu():
    command = 0
    while command != phr.COMMAND_4:
        command = input(phr.MENU_QUESTIONS)
        
        match command:
            case phr.COMMAND_1:
                delete_command()
            case phr.COMMAND_2:
                edit_creation_command()
            case phr.COMMAND_3:
                edit_change_command()
    
    print(phr.EXIT)


if __name__ == '__main__':
    menu()


# by Valendovsky
