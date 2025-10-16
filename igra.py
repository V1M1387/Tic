from doska import *
from check_win import *
from esli_full import *
from koordinates import *

def igra():
    while True:
        pole = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        game_over = False

        while not game_over:
            doska(pole)
            try:
                user_input = input(f"{current_player}, введи число клетки от 1 до 9: ")
                pos = int(user_input)
                mesto = koordinates(pos)
                if mesto is None:
                    print("Ты либо нулями ошибся либо граммовкой. (Не подходит число или это не число).")
                    continue
                row, col = mesto
            except ValueError:
                print("Введи число от 1 до 9.")
                continue

            if pole[row][col] == " ":
                pole[row][col] = current_player
                if check_win(pole, current_player):
                    doska(pole)
                    print(f" {current_player} с победой.")
                    game_over = True
                elif esli_full(pole):
                    doska(pole)
                    print("Ничья.")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Занято на... давай другую.")

        restart = input("Еще? (y/n): ").lower()
        if restart != "y":
            break