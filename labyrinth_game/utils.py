"""Вспомогательные функции для игры."""

from labyrinth_game import constants, player_actions


def describe_current_room(game_state):
    """Описание текущей комнаты."""
    current_room_name = game_state['current_room']
    room = constants.ROOMS[current_room_name]
    
    print(f"\n== {current_room_name.upper().replace('_', ' ')} ==")
    print(room['description'])
    
    # Вывод предметов
    if room['items']:
        print("Заметные предметы:", ", ".join(room['items']))
    
    # Вывод выходов
    if room['exits']:
        exits_str = ", ".join([f"{dir} -> {room}" for dir, room in room['exits'].items()])  # noqa: E501
        print("Выходы:", exits_str)
    
    # Вывод информации о загадке
    if room['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    """Решение загадки в текущей комнате."""
    current_room = game_state['current_room']
    room_data = constants.ROOMS[current_room]
    
    if not room_data['puzzle']:
        print("Загадок здесь нет.")
        return
    
    question, correct_answer = room_data['puzzle']
    print(f"\nЗагадка: {question}")
    
    user_answer = player_actions.get_input("Ваш ответ: ")
    
    if user_answer.lower() == correct_answer.lower():
        print("Верно! Загадка решена.")
        room_data['puzzle'] = None  # Убираем загадку
        
        # Награды за решение загадок в разных комнатах
        if current_room == 'hall':
            if 'treasure_key' not in game_state['player_inventory']:
                game_state['player_inventory'].append('treasure_key')
                print("Вы получаете ключ от сокровищницы!")
        elif current_room == 'garden':
            print("Из фонтана появляется серебряная монета!")
            if 'silver_coin' not in room_data['items'] and 'silver_coin' not in game_state['player_inventory']:  # noqa: E501
                room_data['items'].append('silver_coin')
        elif current_room == 'observatory':
            print("Телескоп чудесным образом починился! Вы видите новые звезды.")
        elif current_room == 'throne_room':
            print("Скелет на троне кивает вам в знак уважения.")
    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    """Попытка открыть сундук с сокровищами."""
    current_room = game_state['current_room']
    
    if current_room != 'treasure_room':
        print("Здесь нет сундука с сокровищами.")
        return
    
    room_data = constants.ROOMS[current_room]
    
    # Проверка наличия ключа
    if 'treasure_key' in game_state['player_inventory']:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        if 'treasure_chest' in room_data['items']:
            room_data['items'].remove('treasure_chest')
        game_state['game_over'] = True
        print("🎉 В сундуке сокровище! Вы победили!")
        print(f"🏆 Ваш результат: {game_state['steps_taken']} шагов")
        return
    
    # Попытка ввести код
    print("Сундук заперт. У вас нет ключа.")
    answer = player_actions.get_input("Попробовать ввести код? (да/нет): ")
    
    if answer == 'да':
        if room_data['puzzle']:
            _, correct_code = room_data['puzzle']
            user_code = player_actions.get_input("Введите код: ")
            
            if user_code == correct_code:
                print("Код принят! Сундук открывается!")
                if 'treasure_chest' in room_data['items']:
                    room_data['items'].remove('treasure_chest')
                game_state['game_over'] = True
                print("🎉 В сундуке сокровище! Вы победили!")
                print(f"🏆 Ваш результат: {game_state['steps_taken']} шагов")
            else:
                print("Неверный код. Сундук остается запертым.")
        else:
            print("Здесь нет загадки для кода.")
    else:
        print("Вы отступаете от сундука.")


def show_help():
    """Показать справку по командам."""
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west/up/down)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
    print("\nНаправления: north, south, east, west, up, down")