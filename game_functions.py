import time
import random
import game_includes
import game_text


# Global invenory list
inventory = []


def play_adventure():
    inventory = []
    intro(inventory)


# Validates input from the user
def validate_input(prompt, options):
    # print(options)
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                # print (option)
                return option

        slow_print("\n\nI'm sorry. I don't understand. Please try again.\n\n")


# Randomly selects combat description line.
def rand_combat(inventory, actor):
    if actor == "monster":
        index = random.randint(0, len(game_includes.monster_damage) - 1)
        combat_line = game_includes.monster_damage[index]
        return combat_line
    if actor == "player":
        if game_includes.inv_item1 in inventory:
            index = random.randint(0, len(game_includes.shillelagh_damage) - 1)
            combat_line = game_includes.shillelagh_damage[index]
            return combat_line
        else:
            index = random.randint(0, len(game_includes.unarmed_damage) - 1)
            combat_line = game_includes.unarmed_damage[index]
            return combat_line


# Prints messages to the console with a delay.
def slow_print(message):
    print(message)
    time.sleep(1)


# Prints lines with delay
def delay_lines(linelist):
    for line in range(len(linelist)):
        slow_print(linelist[line])


# Prints lines without delay
def fast_lines(linelist):
    for line in range(len(linelist)):
        print(linelist[line])
    time.sleep(1)


# Prints damage information during fight
def print_fight(inventory, damage, actor):
    combat_line = rand_combat(inventory, actor)
    time.sleep(2)
    print(combat_line + str(damage) + " damage!")


# Prints introductory text to the console.
def intro(inventory):
    delay_lines(game_text.intro_lines)
    cliff(inventory)


# Does attack calculations for player and monster
def hit_roll(inventory, actor):
    if actor == "monster":
        damage = random.randint(5, 10)
        print_fight(inventory, damage, actor)
        return(damage)
    if actor == "player":
        damage = random.randint(1, 2)
        if game_includes.inv_item1 in inventory:
            damage *= 10
        print_fight(inventory, damage, actor)
        return(damage)


# Controls the fight with the monster
def fight(inventory, order):
    player_hp = game_includes.player_hp
    monster_hp = game_includes.monster_hp

    if order == "ballad":
        damage = hit_roll(inventory, "monster")
        player_hp = player_hp - damage
        delay_lines(game_text.ballad2)

    elif order == "fight":
        damage = hit_roll(inventory, "player")
        monster_hp = monster_hp - damage
        delay_lines(game_text.attack)

    while (player_hp > 0 and monster_hp > 0):
        print("player HP: " + str(player_hp))
        print("monster HP: " + str(monster_hp))
        damage = hit_roll(inventory, "player")
        monster_hp = monster_hp - damage
        if monster_hp < 1:
            break
        damage = hit_roll(inventory, "monster")
        player_hp = player_hp - damage

    if player_hp < 1:
        delay_lines(game_text.fight_lose)
        play_again()

    elif monster_hp < 1:
        delay_lines(game_text.fight_win)
        inventory.append(game_includes.inv_item2)
        cliff(inventory)


# Description and actions at the cliff.
def cliff(inventory):
    delay_lines(game_text.cliff_lines)
    fast_lines(game_text.cliff_inputs)

    cliff_choice = validate_input(game_text.input_req,
                                  game_includes.num_input1 +
                                  game_includes.num_input2 +
                                  game_includes.num_input3 +
                                  game_includes.semantic_cliff1 +
                                  game_includes.semantic_cliff2 +
                                  game_includes.semantic_cliff3)
# double paranthesis to pass pycodestyle error 129
    if ((cliff_choice in game_includes.num_input1 or cliff_choice in
         game_includes.semantic_cliff1)):

        if game_includes.inv_item3 in inventory:
            delay_lines(game_text.cliff_wins)
            play_again()
        else:
            delay_lines(game_text.cliff_dies)
            play_again()

    elif (cliff_choice in game_includes.num_input2 or cliff_choice in
          game_includes.semantic_cliff2):
        house(inventory)
    elif (cliff_choice in game_includes.num_input3 or cliff_choice in
          game_includes.semantic_cliff3):
        hill(inventory)


# Description and action at the house.
def house(inventory):
    delay_lines(game_text.house_lines)
    if (game_includes.inv_item2 in inventory and game_includes.inv_item3
       not in inventory):
        delay_lines(game_text.house_has_item2)
        inventory.append(game_includes.inv_item3)
        cliff(inventory)
    elif (game_includes.inv_item1 in inventory and game_includes.inv_item2
          not in inventory):
        delay_lines(game_text.house_no_item2)
        cliff(inventory)
    elif game_includes.inv_item3 in inventory:
        delay_lines(game_text.house_has_item3)
        cliff(inventory)
    else:
        delay_lines(game_text.house_no_item1)
        inventory.append(game_includes.inv_item1)
        cliff(inventory)


# Description and action on the hill.
def hill(inventory):
    delay_lines(game_text.hill_lines)

    if game_includes.inv_item2 not in inventory:
        delay_lines(game_text.hill_fight)
        fast_lines(game_text.hill_inputs)

        hill_choice = validate_input(game_text.input_req,
                                     game_includes.num_input1 +
                                     game_includes.num_input2 +
                                     game_includes.num_input3 +
                                     game_includes.semantic_hill1 +
                                     game_includes.semantic_hill2 +
                                     game_includes.semantic_hill3)

        if ((hill_choice in game_includes.num_input1 or hill_choice
             in game_includes.semantic_hill1)):
            delay_lines(game_text.ballad1)
            fight(inventory, "ballad")
        elif (hill_choice in game_includes.num_input2 or hill_choice
              in game_includes.semantic_hill2):
            delay_lines(game_text.hill_runs)
            cliff(inventory)
        elif (hill_choice in game_includes.num_input3 or hill_choice
              in game_includes.semantic_hill3):
            if game_includes.inv_item1 in inventory:
                delay_lines(game_text.shillelagh)
            else:
                delay_lines(game_text.no_shillelagh)
            fight(inventory, "fight")
    else:
        delay_lines(game_text.hill_has_item2)
        cliff(inventory)


# Runs runs game again.
def play_again():
    play_choice = validate_input(game_text.input_rep,
                                 game_includes.bool_input_yes +
                                 game_includes.bool_input_no)

    if play_choice in game_includes.bool_input_yes:
        play_adventure()
