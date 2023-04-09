import json
import os
from clients import Client



while True:
    os.system('cls||clear')
    Client.print_commands()
    command = input("Введите команду: ")
    Client.do_command(command)
    is_continue = input("Продлжить - press Enter,  Завершить работу - exit: ")
    if is_continue == "exit":
        break