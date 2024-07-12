from time import sleep
from random import randint

ignore_words = ["at","my", "to", "the", "can", "i", "a", "do", "up"]
valid_verbs = ["get", "pick", "inventory", "what", "use", "go", "move", "fight", "attack", "parry", "evade", "distract", "look", "examine", "bribe"]

#The pacifist variable exists to check if you have either killed or found peaceful means to settle conflict throughout the game. At the end, it will be used to tell you how you played.
pacifist = True
gameovers = 0
user_command = []
player_inventory = {}
inventory_items = {
    "wine" : "A bottle of rough, but strong, wine",
    "sword" : "A heavy sword stol- er, borrowed from a distracted soldier",
    "paper" : "A piece of paper with a puzzle clue written on it",
    "hairpin" : "A bent hairpin you could use to unchain yourself",
    "knife" : "A small pocket knife",
    "chains" : "Chains that fasten around your wrists and secure you to the wall"
    
}

hashline = "---------------------------------------------------------------------------------------------------"

def process_input() :
    while True :
        global user_command

        user_command.clear()
        
        print("")

        user_input = input("What would you like to do? ")
        command_list = user_input.lower().split()

        command_verb = command_list[0]

        command_list_copy = command_list [:] # Use slicing otherwise the copy is just a reference

        for command_word in range (0,len(command_list)) :
            for delete_word in range (0,len(ignore_words)) :
                if command_list[command_word] == ignore_words[delete_word]:
                    command_list_copy.remove(command_list[command_word])

        if command_list[command_word] == ignore_words[delete_word]:
            command_list_copy.remove(command_list[command_word])
                    
        if command_verb == "what" :            
            print("You can LOOK around, MOVE in a direction, or USE an object you have found.")
            print ("Type 'inventory' to check what items you have already found")
            print ("")

            # return

        if command_verb == "quit" or command_verb == "bye" or command_verb == "exit" :
            print("OK, see you later maybe?")

            quit()

        if command_verb == "inventory" :
            inv_check()
        else :
            command_list = command_list_copy[:]

            valid_verb = False

            for verb_check in range(0,len(valid_verbs)) :
                if command_verb == valid_verbs[verb_check] :
                    user_command.append(command_verb)

                    valid_verb = True
            
            if valid_verb :
                for command_words in range(1,len(command_list)) :
                    user_command.append(command_list[command_words])
                    # print(f"Command passed back: {user_command}")
                    print("")
                return
            else :
                print("I'm sorry, I don't know how to do that")
            
#Inventory Check function should be always available via input
def inv_check():
    global player_inventory
    if len(player_inventory) == 0:
        print("You are currently holding nothing in your inventory.")
    else:
        print("You are currently holding:")
        print(hashline)
        for item in player_inventory:
            print(player_inventory.get(item))

def in_inventory(passed_object) :
    if player_inventory.get(passed_object) is None :
        return False
    else :
        return True

def add_inventory(passed_object) :
    inv_desc = inventory_items.get(passed_object)
    player_inventory.setdefault(passed_object,inv_desc)

def drop_inventory(passed_object) :
    player_inventory.pop(passed_object)

def clear_inventory() :
    player_inventory.clear()

def starter_cell() :
    global dict_room1
    print(dict_starter_cell.get("intro"))

    while True:
        process_input()

        user_verb = user_command[0]

        if user_verb != "what" :
            user_object = user_command[1]

            if user_verb == "go" or user_verb == 'move' :
                if user_object == 'north' :
                    if not in_inventory("chains") :
                        dungeon_hallway()
                    else :
                        print("You can't.  You're chained to the wall, remember?")
                else :
                    print (f"You can't go {user_object}")

            if user_verb == "use" or user_verb == 'pick' or user_verb == 'get' :
                if user_object == "knife" :
                    if not in_inventory("chains") :
                        print ("You put the knife in your pocket.  Who knows, it may come in useful.")

                        add_inventory("knife")
                    else :
                        print("You can't reach it.  You're chained to the wall, remember?")

                elif user_object == "paper" :
                    if not in_inventory("chains") :
                        print ("You put the paper in your pocket.  Who knows, it may come in useful.")

                        add_inventory("paper")
                    else :
                        print("You can't reach it.  You're chained to the wall, remember?")

                elif user_object == "hairpin" :
                    print ("You pick up the hairpin and use it to pick the lock securing the chains around your wrist.")
                    print("The hairpin is broken in the process of doing this, but you are now free to move.")

                    drop_inventory("chains")
                    add_inventory("hairpin")

                else :
                    print(f"I don't know what a {user_object} is, sorry.")

            if user_verb == "examine" or user_verb == 'look' :
                if user_object == "cell" or user_object == "room" or user_object == "around" :
                    print("You are in a small, damp, dimly lit cell.")
                    print("A door leads north out into the hallway")
                    print("There is a small mirror attached to the wall.")

                    if in_inventory("chains") :
                        print("You are firmly chained to the wall by your wrists")
                
                    if not in_inventory("hairpin") :
                        print("A bent hairpin is just within your grasp")

                    if not in_inventory("knife") :
                        print("A small pocket knife must have been dropped by one of the guards.")

                elif user_object == "mirror" :
                    print ("The mirror shows you a reflection of your face.  What, were you expecting to see someone else?")
                    print ("")
                    if not in_inventory("paper") :
                        print ("There is a small piece of paper tucked behind one edge")

                else :
                    print(f"I don't know what a {user_object} is, sorry.")

            if user_verb == "fight" or user_verb == 'attack' :
                print("There is no-one here to fight with")

                if in_inventory("chains") :
                    print("Plus you are chained to a wall, remember?")

def dungeon_hallway() : 
    print(dict_dungeon_hallway.get("intro"))
    print(dict_dungeon_hallway.get("doors"))

    while True:
        process_input()

        user_verb = user_command[0]

        if user_verb != 'what' :
            user_object = user_command[1]

            if user_verb == 'go' or user_verb ==  'move' :
                if user_object == 'west' :
                    print("You attempt to push past the guard and open the door he is protecting and go through it")
                    guard_death()
                    
                    return
                
                elif user_object == 'east' :
                    dungeon_cellar()
                elif user_object == 'south' :
                    starter_cell()
                else :
                    print (f"You can't go {user_object}")

            if user_verb == 'bribe' or user_verb == "distract":
                if not in_inventory("wine") :
                    print("You attempt to distract the guard with nothing more than a winning smile and a bawdy joke.")
                    print("")

                    guard_death()
                else :
                    print("The guard takes a mighty swig from the bottle of wine you gave him.")
                    print("With an approving nod he moves aside and lets you open the large door and go through.")
                    print("")

                    drop_inventory("wine")

                    great_hall()

            if user_verb == 'fight' or user_verb == 'attack' :
                if not in_inventory("knife") :
                    print("You muster up all your strength and lay a mighty punch on the guard's chin.  He barely flinches.")
                    print("")

                    guard_death()
                else :
                    print("You threaten the guard with the small knife you found.  The guard points, giggles, and mutters someething about not having any fruit to peel.")

                    guard_death()

            if user_verb == 'look' or user_verb == 'examine'  :
                if user_object == 'hall' or user_object == 'hallway' or user_object == 'room' or user_object == "around" :
                   print(dict_dungeon_hallway.get("intro"))
                   print(dict_dungeon_hallway.get("doors"))
                
                if in_inventory("wine") :
                    print("You have a bottle the evil local wine in your hand")
            
                else:
                    print(f"I don't know what a {user_object} is, sorry.")

def dungeon_cellar() : 
    
    print(dict_dungeon_cellar.get("intro"))
    print(dict_dungeon_cellar.get("doors"))

    while True:
        process_input()

        user_verb = user_command[0]

        if user_verb != 'what' :
            user_object = user_command[1]
    
            if user_verb == 'go' or user_verb == 'move' :
                if user_object == 'west' :
                    if in_inventory("wine") :
                        print(dict_dungeon_cellar.get("wine"))
                    else :
                        print(dict_dungeon_cellar.get("no_wine"))
                        
                    dungeon_hallway()
                else :
                    print (f"You can't go {user_object}")

            if user_verb ==  "use" or user_verb == "pick" or user_verb == 'get' :
                if in_inventory("wine") :
                    print("You already have a bottle of the wine in your hand.")
                    print("Why would anyone want more than one bottle of that foul concoction?")
                else:
                    print ("You have picked up a bottle of wine.")

                    add_inventory("wine")

            if user_verb == "examine" or user_verb == "look" :
                if user_object == "wine" :
                    print("Reading the label, you learn that the wine is a rough but robust brew from the rural heartland")
                    print("It tastes like it was strained through yesterday's laundry, but is strong enough to tranquilise an ox")
                elif user_object == 'room' or user_object == 'cellar' or user_object == "around" :
                    print(dict_dungeon_cellar.get("intro"))
                    print(dict_dungeon_cellar.get("doors"))
                else :
                    print(f"I don't know what a {user_object} is, sorry.")
                
def staircase() : 
    while True:
        print(dict_stairway_knight.get("intro"))

        process_input()

        user_verb = user_command[0]

        if user_verb != 'what' :
           user_object = user_command[1]
        else:
            if user_verb == 'go' or user_verb == 'move' :
                if user_object == 'north' :
                    dungeon_hallway()
                else :
                    print (f"You can't go {user_object}")

            if user_verb == 'use' :
                print("Use code")

            if user_verb == 'examine' or user_verb == 'look' :
                print("Examine code")

def great_hall() : 
   print(dict_great_hall.get("intro"))

   while True:

        process_input()

        user_verb = user_command[0]

        if user_verb != 'what' :
           user_object = user_command[1]

           if user_verb == 'go' or user_verb == 'move' :
                if user_object == 'hidden room' :
                    print()#vault()
                elif user_object == 'north' or user_object == 'archway':
                    staircase()
                elif user_object == 'west' or 'left' or 'door':
                    print()#storage_room()
                else:
                    print (f"You can't go {user_object}")

           if user_verb ==  'use' or user_verb == 'get' or user_verb == "pick" :
                if user_object == 'sword' :
                    print("You pick up one of the discarded battle swords.   ")
                    print("It is nearly as big and heavy as you are, but you just manage to carry it")

                    add_inventory("sword")
                else :
                    print(f"I don't know what a {user_object} is, sorry.")


           if user_verb == 'examine' or user_verb == 'look' :
                # print(dict_great_hall.get("observe_room"))
                print(dict_great_hall.get("ghevent1"))
               # print(dict_great_hall.get("ghevent2")) Removed from demo
                print(dict_great_hall.get("ghevent3"))

def staircase() : 
    print(dict_stairway_knight.get("intro"))
    print(dict_stairway_knight.get("pre_knight"))

    while True:
        process_input()

        user_verb = user_command[0]

        if user_verb != 'what' :
           user_object = user_command[1]

           if user_verb == 'go' or user_verb == 'move' :
                if user_object == 'north' :
                    knight_battle_violent()
                elif user_object == 'south' or 'back':
                    print("There's no turning back.")
                else :
                    print (f"You can't go {user_object}")

           elif user_verb == 'examine' or user_verb == 'look' :
                print(dict_stairway_knight.get("pre_knight"))

def knight_battle_violent() :
    global pacifist
    global user_command

    pacifist = False

    knight_health = 3
    player_health = 2
    
    print(dict_stairway_knight.get("knight_fight"))
    
    sleep(2)
    
    if not in_inventory("sword"):
        print(dict_stairway_knight.get("knight_battle_no_weapons"))
        game_over()
    else :
       print(dict_stairway_knight.get("knight_battle_sword"))
    
    while True:
        knight_action = randint(1,3)

        if knight_health == 1:
            print (dict_stairway_knight.get("knight_battle_one_more_hit"))
            print()

        if knight_action == 1:
            print(dict_stairway_knight.get("knight_battle_feinting"))
            print()
        elif knight_action == 2:
            print(dict_stairway_knight.get("knight_battle_approaching"))
            print()
        elif knight_action == 3:
            print (dict_stairway_knight.get("knight_battle_leap"))
            print()

        process_input()

        user_verb = user_command[0]

        # The object can safely be ignored here, it's always the knight, but this allows for multiple opponents
        if len(user_command) == 1 :
            user_object = 'knight'
        else :
            user_object = user_command[1]

        if user_verb == 'attack' :
            if user_object == 'knight' and knight_action == 1:
                print (dict_stairway_knight.get("knight_suc_attack"))
                knight_health = knight_health-1
            else :
                print (dict_stairway_knight.get("knight_battle_hit"))
                player_health = player_health-1

        if user_verb == 'parry' :
            if user_object == 'knight' and knight_action == 2:
                print (dict_stairway_knight.get("knight_suc_parry"))
                knight_health = knight_health-1
            else :
                print (dict_stairway_knight.get("knight_battle_hit"))
                player_health = player_health-1
                    
        if user_verb == 'evade' :
            if user_object == 'knight' and knight_action == 3:
                print (dict_stairway_knight.get("knight_suc_evade"))
                knight_health = knight_health-1
            else :
                print (dict_stairway_knight.get("knight_battle_hit"))
                player_health = player_health-1

        if player_health == 0:
            print (dict_stairway_knight.get("knight_battle_death"))

            game_over()
        elif knight_health == 0:
            print (dict_stairway_knight.get("knight_dead"))

            sleep (2)
        
            print (dict_stairway_knight.get("battlements_proceed"))
            game_win() #END OF DEMO (Unless we get past this point)
            #nextfunction()

def final_puzzle():
    print("You approach a drawbridge with a table text to it, the table has 10 cube like holes with blocks with letters on it")
    print("You notice a sign that states, only the correct answer may pass")
    if in_inventory("paper"):
        print("Look to the east where the 40 thieves hide, Step to the left then jump back five")
    else:
        print("")
    if user_command == "help":
        print("OPEN SESAME was the phrase used to move the rock hiding the entrance to the cave in Ali Baba And The 40 Thieves")
        print("How would you like to arrange the blocks? ")
    if user_command == "STIR  WIWEQI":
        print("You hear a click and the drawbridge begins to lower")
        print("You run for the exit")
        sleep(1)
        game_win()
    elif user_command != "STIR  WIWEQI":
        print("Incorrect, 2/3 attempts remaining")
    elif user_command != "STIR  WIWEQI":
        print("Incorrect, 1/3 attempts remaining")
    elif user_command != "STIR  WIWEQI":
        print("Incorrect, you fall into the moat and drown")
        sleep(1)
        game_over()

def guard_death() :
    print("Without so much as a second thought the guard draws his large double-edged sword and plunges it into your chest.")
    print("")
    print("You died.")
    x=input("Press any key to continue ")
    game_over()
    
def title_screen_and_credits() :
    credits = ["Alan Edwards", "Monika D. Barnes", "Chanel Albadri", "Thomas Stephens", "Dylan Heaton", "Anas Ali", "Mark McCarthy", "Code Nation"]
    print(hashline)
    sleep(1)
    print(".___ __. __ .__..__ .___  .___.__ .__..  .   __ .__. __..___..   .___  .__ .   ,.___..  ..__..  .")
    sleep(0.5)
    print("[__ (__ /  `[__][__)[__   [__ [__)|  ||\/|  /  `[__](__   |  |   [__   [__) \./   |  |__||  ||\ |")
    sleep(0.5)
    print("[___.__)\__.|  ||   [___  |   |  \|__||  |  \__.|  |.__)  |  |___[___  |     |    |  |  ||__|| \|")
    sleep(1)
    print(hashline)
    print("DEMO VERSION")
    print(hashline)
    print()
    print()
    print("Created by:")
    print(credits[0])
    print(credits[1])
    print(credits[2])
    print(credits[3])
    print(credits[4])
    print(credits[5])
    print(f"Special Thanks to {credits[6]} and {credits[7]} for making this game possible!")
    print(hashline)
    game_start()
    
def game_start() :
    clear_inventory()
    add_inventory("chains")
    print(hashline)
    game_s_made = False
    while game_s_made == False:
        game_start_option = str(input("Would you like to start a new game? (Y/N) : "))
        game_start_option == game_start_option.split()
        if game_start_option == "y" or game_start_option == "yes":
            print("Then let us begin...")
            sleep(2)
            print("")
            starter_cell()
            break
        elif game_start_option == "n" or game_start_option == "no":
            print("Thank you for playing!")
            sleep(2)
            quit()
        else:
            print("Invalid Command, please try again.")
            game_s_made == False

def game_win():
    global pacifist
    global gameovers
    print()
    print("  _  _        __  _      ___           ___ ___  _        __       ")
    print(" /  / \ |\ | /__ |_)  /\  | | | |   /\  |   |  / \ |\ | (_  | | | ")
    print(" \_ \_/ | \| \_| | \ /--\ | |_| |_ /--\ |  _|_ \_/ | \| __) o o o ")
    sleep(2)
    print("This is the end of the demo for ESCAPE FROM CASTLE PYTHON.")
    sleep(2)
    if pacifist == True :
        print (f"You have died {gameovers} times this play session.")
        sleep (2)
        print ("You have avoided killing any monsters during your escape. Well done!")
        sleep (2)
        print ("Thank you so much for playing our game!")
        sleep (2)
        print()
        title_screen_and_credits()
    else:
        print (f"You have died {gameovers} times this play session.")
        sleep(2)
        print ("Thank you so much for playing our game!")
        sleep (2)
        print()
        title_screen_and_credits()

def game_over():
    global gameovers
    gameovers = gameovers+1
    print()
    print("  _  _      _    _     _  _ ")
    print(" / `/_//|,//_`  / /| |/_`/_/")
    print("/_;/ //  //_,  /_/ |//_,/ \.")
    sleep(2)
    print(f"You have died {gameovers} times this play session.")
    if gameovers>5:
        sleep(2)
        print("Try harder.")
    sleep(5)
    print()
    title_screen_and_credits()

dict_starter_cell = {
    "intro" : "You find yourself in a cell in a dungeon.  You are chained to a wall.",
    "under_bed" : "You look under the bed and find a small knife and a hair pin",
    "behind_mirror" : "You check benind the mirror and find a piece of paper with numbers written on it",
    "flush_toilet" : "Good job, flushing that toilet! Proud of you!",
    "knife_hairpin" : "You use the knife and hair pin to unlock the door and escape the room",
    "peak_out_the_door" : "You peak out the door and see a creepy hallway with flickering lights"
}

dict_great_hall = {
    "intro" : "You find yourself in a great banqueting hall, with long tables laden with food and wine, and a great many seats along both sides.",
    "ghevent1" : "In the far north corner you can just see an archway that could be your way out.",
    "ghevent2" : "On the west side of the room you can see another door.",
    "ghevent3" : "Along one wall there is a large pile of swords belonging to the knights just ripe for the picking",
    "observe_room" : "You observe the room and can see some bricks protruding the wall, a slight push knocks the bricks over, there was a HIDDEN ROOM",
}

dict_dungeon_hallway = {
    "intro" : "You enter a cold amd damp hallway with a flickering light, you can hear the wind whistling through the cracks in the wall.",
    "doors" : "There is a door with a guard guarding it at the western end of the hall, and a smaller unguarded door at the eastern end.",
    "guards" : "As you walk down the hallway you see 2 doors 1 of which is being guarded",
    "unguarded_door" : "The unguarded door seems to be a cellar of some sort",
    "guarded_door" : "The guarded door has armed guards protecting it, it seems to be the only way forward",
    "wine_to_guard" : "You give the bottle of wine to the guards and they let you pass",
    "attack_guard_knife" : "You use the knife to take down the guards that were blocking the door, your knife breaks in the process",
    "attack_guard_no_knife" : "You attempt to attack the guards with your fists, they draw their swords and cut you down",
    "guards_defeated" : "The defeated guards drop their swords and a key, you take the sword and key then quickly go through the door."
}
dict_dungeon_cellar = {
    "intro" : "You are in a cellar off the main dungeon hallway.  You notice it's being used as a wine cellar, there are bottles of wine and an intoxicated guard asleep.",
    "doors" : "The only door is behind you, to the west.",
    "wine" : "You take a bottle of wine from the cellar",
    "no_wine" : "You leave the cellar slowly as not to wake the sleeping guard",
    "drink_wine" : "You drink the wine, as you drink you start feeling pain, the wine was poisoned, you die"
} 
dict_storage_room = {
    "intro" : "As you enter the storage room there are lots of useless things stored here but a key catches your attention",
    "take_key" : "You pick up the key as it seems useful",
    "take_random_item" : "You pick up one of the useless items scattered around the room which triggers a trap, the whole room caves in and you die",
    "observe_storage_rooom" : "As you look around the room",
    "intro" : "As you enter the vault you see plenty of valuable items including weapons, armour and health items",
    "vault_trap" : "You pick up a random item that looks useful, the item is attached to a string, you hear a click and the room explodes, you die",
    "observe_vault" : "You observe the room and notice a few items are attached to strings, best not to pick things up randomly, you also notice a locked box that seems to have as puzzle to access it",
    "vault_puzzle" : "The chest has a ",
    "correct_vault_puzzle" : "Congrants you completed the puzzle!!, as the chest opens you notice theres only one thing inside, a flute?",
    "incorrect_vault_puzzle" : "Unlucky, you failed the puzzle, the chest implodes, whatever was inside is now lost forever",
    "pickup_flute" : "You pick up the flute that was in the chest, you have no idea how to play the flute but you take it anyway"
}
dict_stairway_knight = {
    "intro" : "You see a staircase leading north to the castle battlements.",
    "pre_knight" : "You peep through the door and see a great armored knight. You have a feeling this will be the final foe you face today.",
    "knight_fight" : "You decide to steel your nerves and confront the giant foe. Entering the battlements, you feel a chilling wind blow through you. No turning back.",
    "knight_return" : "You feel unprepared for this fight. It may be wise to look for something that will help you through this before making any rash decisions.",
    "knight_battle_no_weapons" : "As you run into the battlements, you realise that you are woefully unprepared for this fight. You don't even have a weapon, and you sorely doubt that your grimy hands or a battered knife will be enough to fight this monster.",
    "knight_battle_no_weapons_death" : "Your folly was proven correct shortly after as the giant knight beheaded you with ease.",
    "knight_battle_hit" : "It was no use, the knight managed to land a hit on you - narrowly missing your neck. You won't survive another, be careful.",
    "knight_battle_death" : "Unfortunately, despite your best efforts, you succumbed to the knight's strength. Your body lays strewn on the battlements.",
    "knight_battle_storeroom_dagger" : "Drawing your stubby blade, you close in to attack the knight.",
    "knight_battle_sword" : "Drawing your sword, you fiercely rush towards your opponent.",
    "knight_battle_flute" : "Thinking sharply, you take out the flute you found earlier. It emits an eerie glow. As you begin to play it, the sorrowful tune it plays begins to lull the knight - it appears dazed and yet, interested in your flute.",
    "knight_battle_approaching" : "The knight is approaching for an attack! Its great claymore is rapidly approaching your neck and there is not much time to react.",
    "knight_battle_feinting" : "The knight is feinting! It's a narrow window, but you could land an attack.b",
    "knight_battle_leap" : "The knight is preparing to a devastating leaping attack towards you! There's seemingly no time to attack or defend. The knight is enraged!",
    "knight_suc_parry" : "You parried the incoming attack and cut through the knight's defenses!",
    "knight_suc_attack" : "You cut through the knight's feint and land a hit!",
    "knight_suc_evade" : "You barely dodge the titan's attack, fabric tearing mere millimetres from your sskin. It was not all for naught, though, as you managed to land a hit on the knight's head whilst it was recovering.",
    "knight_battle_one_more_hit" : "You just need one more clean hit to down the great foe. You can do this.",
    "knight_dead" : "With a clatter of heavy armour and a desperate roar, the knight falls motionless to the ground. You have narrowly defeated the knight with the equipment you found.",
    "knight_pacified" : "With the sound of the flute at your side and some soothing words of encouragement, you persuade the knight to allow you through the battlements.",
    "knight_enraged" : "Your attack towards the knight at its weakest moment only served to enrage it further. By the time the morning came, there was not much of you left to sift through on the battlements.",
   "battlements_proceed" : "You continue onward through the battlements and down the stairs to a new room."
}
title_screen_and_credits()