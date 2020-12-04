from tracker_objects_datastructures_meaningless import *


def main():
    init = Initiative()
    players = Player_list()
    npc_number = int(input("How many NPCs are participating (0 to 15)? ---- "))
    init.import_npcs(npc_number)
    print("Would you like to create a group of players? (Otherwise you'll import an already existing one)")
    check = int(input("Answer: 1 for YES, 2 for NO ---- "))
    if check == 1:
        players.create_players(init)
    else:
        players.import_players(init)
    init.sort_creatures()
    init.display_current_list()


main()
