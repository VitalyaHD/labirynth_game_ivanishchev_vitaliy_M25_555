#!/usr/bin/env python3
"""Главный модуль для игры 'Лабиринт сокровищ'."""

from labyrinth_game import player_actions, utils

# Состояние игры
game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Флаг окончания игры
    'steps_taken': 0  # Количество шагов
}


def process_command(game_state, command):
    """Обработка команд пользователя."""
    parts = command.split()
    if not parts:
        return
    
    main_command = parts[0]
    
    if main_command == "look":
        utils.describe_current_room(game_state)
    elif main_command == "inventory":
        player_actions.show_inventory(game_state)
    elif main_command == "go" and len(parts) > 1:
        player_actions.move_player(game_state, parts[1])
    elif main_command == "take" and len(parts) > 1:
        player_actions.take_item(game_state, parts[1])
    elif main_command == "use" and len(parts) > 1:
        player_actions.use_item(game_state, parts[1])
    elif main_command == "solve":
        if game_state['current_room'] == 'treasure_room':
            utils.attempt_open_treasure(game_state)
        else:
            utils.solve_puzzle(game_state)
    elif main_command == "help":
        utils.show_help()
    elif main_command in ["quit", "exit"]:
        game_state['game_over'] = True
        print("Спасибо за игру!")
    else:
        print("Неизвестная команда. Введите 'help' для списка команд.")


def main():
    """Главная функция, запускающая игру."""
    print("🎮 Добро пожаловать в Лабиринт сокровищ!")
    print("🔍 Исследуйте комнаты, собирайте предметы, решайте загадки!")
    print("💡 Введите 'help' для списка команд\n")
    
    utils.describe_current_room(game_state)
    
    # Основной игровой цикл
    while not game_state['game_over']:
        command = player_actions.get_input("\nВведите команду: ")
        process_command(game_state, command)


if __name__ == "__main__":
    main()