import os
import sys
from os import getcwd, getlogin, chdir
from time import sleep
import readline

# Инициализация colorama


try:
    # Получаем имя текущего пользователя
    user_home = os.path.expanduser("~")  # Получаем домашнюю директорию пользователя
    history_file = os.path.join(user_home, '.history')  # Формируем полный путь к файлу истории

    # Загружаем историю команд, если файл существует
    if os.path.isfile(history_file):  # Проверяем, является ли это файлом
        with open(history_file, 'r') as f:
            history = f.read().splitlines()
    else:
        history = []  # Если файл не найден, инициализируем пустой список

    # Добавляем историю команд для автозаполнения
    for cmd in history:
        readline.add_history(cmd)

    print('PyTerm 2024')

    while True:
        path = getcwd()
        name = getlogin()
        
        # Формируем строку запроса без цветовых кодов
        command = input(f'{name} ► {path} > ')

        if command.startswith('cd '):
            try:
                chdir(command[3:])
            except FileNotFoundError:
                print(f"cd: no such file or directory: {command[3:]}")
            except PermissionError:
                print(f"cd: permission denied: {command[3:]}")
            continue

        try:
            os.system(command)
        except Exception as e:
            error_message = str(e)
            cleaned_error = error_message.replace('/bin/sh: строка 1: ', '')
            print(f"{cleaned_error}")

        # Сохраняем команду в файл истории
        with open(history_file, 'a') as f:
            f.write(command + '\n')

except Exception as e:
    print('Error!')