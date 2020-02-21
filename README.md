# ENGS-110 Individual Project
Combat Tracker

OVERVIEW:

Every Dungeon Master (hereby DM) knows how pointlessly long it takes to switch from roleplaying to combat. Having to set up the map, bookmarking each participant’s page for later reference during combat, and most importantly, tracking the initiative order and the hit points of each participant. 

Combat Tracker automizes and quickens the start and flow of combat, doing a lot of the mechanical work and math for the DM, giving the latter, and consequently, the players, more time to focus on the important aspects of the game.

It will consist of two main parts: the Initiative Tracker and Hit Point (hereby HP) Tracker. The Initiative Tracker allows the DM to search and pick the  DM-controlled participants of the combat engagement, possibly including some home-made characters, add the initiative rolls of the Player Characters (hereby PCs), and with a simple click of a button, roll and display the Initiative Order and the elapsed rounds of combat on the screen.

The HP Tracker displays the HP of each DM-controlled participant and shows the change of HP throughout the combat encounter. 


TARGET USERS:

Who: Dungeon Masters 

What: The app allows the user to easily organize the start of combat by rolling initiative for all DM-controlled characters and track each of their HP throughout the encounter.

When: End of the Spring 2020 semester 

How: Python


USER PROBLEMS SOLVED:

User Need: Roll Initiative for all DM-controlled encounter participants. 

Resolution: Combat Tracker chooses a random number from 1 to 20 (representing the 20-sided die a.k.a. d20) and adds each participant's initiative modifier to the number.


User Need: Order all encounter participants in the initiative order frm highest to lowest.

Resolution: Combat Tracker orders all participants, both DM-controlled and PCs, first by their roll, and, in case of equal totals, by their initiative modifiers. It then display's the order, including information about the roll, the initiative modifier, the initiative count 20, and whether the participant is a PC or a DM-controlled creature.


User Need: Track and display DM-controlled creatures' HP

Resolution: Combat Tracker displays each DM-controlled creatures' HP and allows to easily type in any changes to it, be it damage (negative) or healing(positive). It then displays the change, including information about change


USER STORIES:

1. As a user, I can quickly create adn track the initiative order of the encounter.

  a. As a user, I can pick DM-controlled participants from the list;
  
  b. As a user, I can roll initiative for each DM-controlled participant;
  
  c. As a user, I can, including the PCs' rolls, order the initiative list from highest to lowest;

2. As a user, I can display each DM-controlled participant's HP individually and apply changes to it, which will be displayed as well.

