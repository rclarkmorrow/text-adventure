# File includes inventory items that might be used,
# lists used for input validation.

# Lists of valid input options
num_input1 = ["1", "one"]
num_input2 = ["2", "two"]
num_input3 = ["3", "three"]
semantic_cliff1 = ["cliff", "jump"]
semantic_cliff2 = ["knock", "door", "house"]
semantic_cliff3 = ["run", "hill", "acorn", "tree"]
semantic_hill1 = ["listen", "ballad"]
semantic_hill2 = ["run", "cliff", "back"]
semantic_hill3 = ["fight", "bono", "monster", "hit"]
bool_input_yes = ["y", "yes"]
bool_input_no = ["n", "no"]

# Inventory items
inv_item1 = "magic truncheon"
inv_item2 = "golden acorn"
inv_item3 = "enchanted feather"

# Set initial hitpoints for player and monster
player_hp = 50
monster_hp = 50

# Damage descriptions

monster_damage = ["\n\nThe Bono monster blasts your ears with \"Unforgettable"
                  + " Fire\" for ", "\n\nYou are overcome by" +
                  " \"Deeeesiiire\" and take ", "\n\nIt's a \"Sunday Bloody" +
                  " Sunday!\" You take "]
shillelagh_damage = ["\n\nYou wrap the Bono monster across its knuckles with "
                     "your " + inv_item1 + "\nfor ",
                     "\n\nYou bonk the Bono monster on the noggin with your " +
                     inv_item1 + ".\nIt takes ",
                     "\n\nUsing your " + inv_item1 + ", You trip the Bono " +
                     "monster.\nIt falls and takes "]
unarmed_damage = ["\n\nYou cover your ears and the Bono monster feels sha" +
                  "me. It takes ", "\n\nYou weakly slap the Bono monster" +
                  " for ", "\n\nYou place your hand over the Bono monster's " +
                  "mouth. It takes "]
