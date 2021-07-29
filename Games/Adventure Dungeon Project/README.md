## Adventure Dungeon Project
Development of a text-based game in which one explores a building and battles some enemies. 
Includes the following:
### battlesys.py
This file encodes the mechanics of characters (playable and enemies), moves and other battle details. To be imported by other files.
### battlsim.py
Play unending battles -  a battle simulator, hence the name - both a game and to test the balance of moves and characters in battles. Imports battlesys.
### adventuredungeon.py
The actual game, currently text-based. Includes items (map, weapons, etc) to pick up/obtain, locked doors and keys, map updates based on rooms one has been in, descriptions for rooms, enemies, items, etc.
