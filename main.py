import os
import subprocess
import sys
from os import getcwd, getlogin, chdir, system
from colorama import Fore, Style, init
from time import sleep
import readline
try:
    # Получаем имя текущего пользователя
    user_home = os.path.expanduser("~")  # Получаем домашнюю директорию пользователя
    history_file = os.path.join(user_home, '.history')  # Формируем полный путь к файлу истории

    # Загружаем историю команд, если файл существует
    if not os.path.isfile(history_file):  # Проверяем, является ли это файлом
        history = []  # Если файл не найден, инициализируем пустой список
    else:
        with open(history_file, 'r') as f:
            history = f.read().splitlines()

    # Добавляем историю команд для автозаполнения
    for cmd in history:
        readline.add_history(cmd)

    init(autoreset=True)
    sys.stdout.write('PyTerm 2024\n')
    sys.stdout.flush()

    while True:
        path = getcwd()
        name = getlogin()
        command = input(f'{Fore.CYAN}{name}{Style.RESET_ALL} ► {Fore.GREEN}{path}{Style.RESET_ALL} > ')

        if command.startswith('cd '):
            try:
                chdir(command[3:])
            except FileNotFoundError:
                sys.stdout.write(f"cd: no such file or directory: {command[3:]}\n")
            except PermissionError:
                sys.stdout.write(f"cd: permission denied: {command[3:]}\n")
            continue

        elif command.lower() in ['exit', 'quit']:
            sys.stdout.write("Выход из PyTerm.\n")
            sleep(0.5)
            break

        try:
            system(command)
        except Exception as e:
            error_message = str(e)
            cleaned_error = error_message.replace('/bin/sh: строка 1: ', '')
            sys.stdout.write(f"{cleaned_error}\n")

        # Сохраняем команду в файл истории

        with open(history_file, 'a') as f:
            f.write(command + '\n')
except:
    print('Error!')
