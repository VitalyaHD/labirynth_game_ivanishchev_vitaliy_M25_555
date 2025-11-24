"""Функции для действий игрока."""

from labyrinth_game import constants, utils


def show_inventory(game_state):
    """Отображение инвентаря игрока."""
    inventory = game_state['player_inventory']
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")


def get_input(prompt="> "):
    """Получение ввода от пользователя с обработкой ошибок."""
    try:
        return input(prompt).strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    """Перемещение игрока в указанном направлении."""
    current_room = game_state['current_room']
    room_data = constants.ROOMS[current_room]
    
    if direction in room_data['exits']:
        new_room = room_data['exits'][direction]
        game_state['current_room'] = new_room
        game_state['steps_taken'] += 1
        print(f"Вы переместились {direction}.")
        utils.describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """Взятие предмета из комнаты."""
    current_room = game_state['current_room']
    room_data = constants.ROOMS[current_room]
    
    if item_name in room_data['items']:
        # Особые проверки для определенных предметов
        if item_name == 'treasure_chest':
            print("Вы не можете поднять сундук, он слишком тяжелый.")
            return
        
        game_state['player_inventory'].append(item_name)
        room_data['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    """Использование предмета из инвентаря."""
    if item_name not in game_state['player_inventory']:
        print("У вас нет такого предмета.")
        return
    
    # Обработка использования различных предметов
    if item_name == 'torch':
        print("Вы зажигаете факел. Становится светлее.")
    elif item_name == 'sword':
        print("Вы размахиваете мечом. Чувствуете себя увереннее.")
    elif item_name == 'bronze_box':
        if 'rusty_key' not in game_state['player_inventory']:
            game_state['player_inventory'].append('rusty_key')
            print("Вы открываете бронзовую шкатулку. Внутри лежит ржавый ключ!")
        else:
            print("Шкатулка уже пуста.")
    elif item_name == 'silver_coin':
        print("Вы подбрасываете серебряную монету. Она падает орлом вверх.")
    elif item_name == 'star_chart':
        print("Вы изучаете звездную карту. Видите знакомые созвездия.")
    elif item_name == 'lens':
        print("Смотрите через линзу. Мелкие детали становятся четче.")
    elif item_name == 'potion_ingredient':
        print("Этот ингредиент пахнет странно. Возможно, он для зелья.")
    elif item_name == 'golden_crown':
        print("Вы примеряете золотую корону. Чувствуете себя королем!")
    elif item_name == 'old_diary':
        print("В дневнике записи о исследованиях лабиринта. Много непонятных символов.")
    elif item_name == 'magnifying_glass':
        current_room = game_state['current_room']
        room_data = constants.ROOMS[current_room]
        if room_data['puzzle']:
            print("С помощью лупы вы находите скрытые подсказки в комнате!")
        else:
            print("Вы внимательно осматриваете комнату, но ничего нового не находите.")
    elif item_name == 'hidden_scroll':
        print("На свитке древние письмена: 'Ищи ключ в зале с эхом'")
    else:
        print(f"Вы не знаете, как использовать {item_name}.")