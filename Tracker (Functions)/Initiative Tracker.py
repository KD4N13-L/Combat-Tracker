from initiative_functions import *


def main():
    npcs = npc_import()
    pcs = pc_import()
    initiative = {}
    initiative.update(npcs)
    initiative.update(pcs)
    initiative_display(initiative)

main()