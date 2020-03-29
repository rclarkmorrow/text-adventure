import game_includes
# File defines variables with text that will be displayed to
# users' consoles.

# Input request text
input_req = "What would you like to do?\n\n"
input_rep = "\n\nWould you like to play again? (y/n)\n\n"

game_over = "\n\nGAME OVER"

# Intro description text
intro_line1 = "\n\nIt's a nice, sunny morning. And not too cold!"
intro_line2 = "You are walking to your car to go to work, when"
intro_line3 = "all of a sudden a nasty little vortex appears"
intro_line4 = "in the sky. It descends and gobbles you up."
intro_line5 = "You spin and spin and spin, and then pass out."
intro_line6 = "..."
intro_line7 = "..."
intro_line8 = "..."
intro_line9 = "You awaken to find yourself lying in dried grass."
intro_lines = [intro_line1, intro_line2, intro_line3, intro_line4,
               intro_line5, intro_line6, intro_line7, intro_line8,
               intro_line9]

# Clifftop description text
cliff_line1 = "\n\nTo your left is a cliff edge overlooking a three-thousand"
cliff_line2 = "foot drop and to your right is a hill with a giant acorn tree"
cliff_line3 = "at the top. There is also a door and windows built into the"
cliff_line4 = "hillside."
cliff_lines = [cliff_line1, cliff_line2, cliff_line3, cliff_line4]

# Clifftop input request text
cliff_input1 = "\n\nYou can (1) jump off the cliff, (2) knock on the door,"
cliff_input2 = "or (3) run up the hill.\n\n"
cliff_inputs = [cliff_input1, cliff_input2]

# Clifftop win/lose condition text
cliff_jump = "\n\nYou run toward the cliff's edge and leap like a fawn,"

cliff_die1 = "but your elation soon turns to terror as the sound of rushing"
cliff_die2 = "fills your ears. The rocky ground rises quickly to greet"
cliff_die3 = "you. Ooopsies!!! You died!\n\n"
cliff_dies = [cliff_jump, cliff_die1, cliff_die2, cliff_die3, game_over]

cliff_win1 = "and you begin to float, propelled by a nice breeze. Looking"
cliff_win2 = "up, you see the nasty little vortex descending toward you."
cliff_win3 = "It gobbles you up and when you awake you are in your car."
cliff_win4 = "\n\nCongragulations! You Escaped!"
cliff_wins = [cliff_jump, cliff_win1, cliff_win2, cliff_win3, cliff_win4,
              game_over]

# Description text when returning to clifftop
cliff_return = "You return to the cliff top."

# House in the hill description text
house_line1 = "\n\nYou walk up to the door in the hill and knock three"
house_line2 = "times. After a few seconds, the door creaks open and"
house_line3 = "a hermit with a long white beard greets you:\n\n"
house_lines = [house_line1, house_line2, house_line3]
# Description when player does not have game_includes.inv_item1
house_no_item1_1 = "\"Hello! You look lost. Judging by your strange clothes"
house_no_item1_2 = "I am guessing you aren't from here. That nasty vortex"
house_no_item1_3 = "can be a pain. Don't worry. I can help, but you'll have"
house_no_item1_4 = "to bring me a " + game_includes.inv_item2 + \
                   " from the tree on the hill.\""
house_no_item1_5 = "\n\n\"Here. Take this. My last visitor didn't fare so"
house_no_item1_6 = "well. But she left this.\" He hands you a knotty"
house_no_item1_7 = "blackthorn stick with a large knob at one end."
house_no_item1_8 = "\n\nYou have recieved the " + game_includes.inv_item1 + \
                   " (it could come"
house_no_item1_9 = "in really handy if you need to declare shillelagh" + \
                   " law.)\n\n"
house_no_item1 = [house_no_item1_1, house_no_item1_2, house_no_item1_3,
                  house_no_item1_4, house_no_item1_5, house_no_item1_6,
                  house_no_item1_7, house_no_item1_8, house_no_item1_9,
                  cliff_return]

# Description when player does not have game_includes.invitem2 and
# player already has game_includes.invitem1
house_no_item2_1 = "\"I see you don't have my " + game_includes.inv_item2 + \
                   " yet!"
house_no_item2_2 = "Don't come back until you have it. Now SCRAM!\"\n\n"
house_no_item2 = [house_no_item2_1, house_no_item2_2, cliff_return]

house_has_item2_1 = "The hermit's eyes widen. He squeals in excitement"
house_has_item2_2 = "and exclaims, \"My prescious!\" He slames the door"
house_has_item2_3 = "and you hear the sounds of rummaging. After a few"
house_has_item2_4 = "moments he returns and hands you the " + \
                    game_includes.inv_item3
house_has_item2_5 = "He disappears inside, slamming the door again.\n\n"
house_has_item2 = [house_has_item2_1, house_has_item2_2, house_has_item2_3,
                   house_has_item2_4, house_has_item2_5, cliff_return]

# Description when player has game_includes.inv_item3
house_has_item3_1 = "I've already given you all the help I can! Now go"
house_has_item3_2 = "jump off a cliff!!!!\n\n"
house_has_item3 = [house_has_item3_1, house_has_item3_2, cliff_return]

# On top of the hill description game_text
hill_line1 = "\n\nYou ascend the one tree hill. The acorn tree is massive,"
hill_line2 = "reaching a thousand feet into the sky. Hundreds of acorns litter"
hill_line3 = "the gound at its base."
hill_lines = [hill_line1, hill_line2, hill_line3]

hill_has_item2_1 = "\n\nThe Bono monster has been silenced. It is quiet except"
hill_has_item2_2 = "the sounds of birds chirping. Your work here is done.\n\n"
hill_has_item2 = [hill_has_item2_1, hill_has_item2_2, cliff_return]

hill_fight1 = "\n\nA figure steps out from behind the acorn three. Oh no!!!!"
hill_fight2 = "It's a Bono monster. He says, \"You must want my " +\
              game_includes.inv_item2 + "."
hill_fight3 = "I will give it to you if you listen to my ballad.\""
hill_fight = [hill_fight1, hill_fight2, hill_fight3]

hill_run1 = "\n\nYou shrink back in horror at the thought of hearing the Bono"
hill_run2 = "monster's ballad and run down the hill to the clifftop."
hill_runs = [hill_run1, hill_run2]

hill_input1 = "\n\nYou can (1) listen to the ballad, (2) run away or"
hill_input2 = "(3) attempt to fight the Bono monster.\n\n"
hill_inputs = [hill_input1, hill_input2]

# Descriptive text for the Bono monster fight
ballad1_1 = "\n\nYou figure, \"What's the harm in a song?\" Anyway you need" +
ballad1_2 = "that" + game_includes.inv_item2 + ".
ballad1_3 = "The Bono monster begins to sing.""
ballad1 = [ballad1_1, ballad1_2, ballad1_3]

ballad2_1 = "\n\nOuch! That hurt! The Bono monster clearly means business."
ballad2_2 = "You prepare to defend yourself."
ballad2 = [ballad2_1, ballad2_2]

shillelagh1 = "\n\nYou raise up your " + game_includes.inv_item1 + " and" + \
              " let out a fierce cry."
shillelagh2 = "It's time for the Bono monster to learn about shillelagh law!"
shillelagh = [shillelagh1, shillelagh2]

no_shillelagh1 = "\n\nThe thought of a ballad is more than you can bear. You"
no_shillelagh2 = "step forward and attempt to cover the Bono monster's"
no_shillelagh3 = "mouth as it begins to sing."
no_shillelagh = [no_shillelagh1, no_shillelagh2, no_shillelagh3]

attack1 = "\n\nYou definitely got the drop on the Bono monster, but it is"
attack2 = "not enough. The Bono monster backs up and bursts into song."
attack = [attack1, attack2]

fight_win1 = "\n\nYou are victorious! The Bono monster, bruised and beaten,"
fight_win2 = "slinks away and retreats to where the streets have no name."
fight_win3 = "You find the " + game_includes.inv_item2 + " laying on the " + \
             "ground where it was standing."
fight_win = [fight_win1, fight_win2, fight_win3]

fight_lose1 = "\n\nOh no! How long must he sing this song?! You are overcome."
fight_lose2 = "With bleeding ears, you slump to the ground and succumb to"
fight_lose3 = "the waves of sonic defilement. Ooopsies!!! You died!"
fight_lose = [fight_lose1, fight_lose2, fight_lose3, game_over]
