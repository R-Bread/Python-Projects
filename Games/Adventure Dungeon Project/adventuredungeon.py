from battlesys import *
'''
To Do:
Second-last room onwards.
Secret Room from entrance, boss battle.
Exit if walk back (Using event block).
Fix all lore parts.

Better Tutorial
Character Choice
Difficulty
Other maps
'''

print("Actions:\nl/r/b/f to move, i for info on room, s or m to see your stats or moves, and e for exiting the dungeon.")
cord=[0,0]
chamber_list, corridor_list=[], []


# Define room class and descriptions.
class room:
	def __init__(self,info,dimensions,name,type):
		self.info=info
		self.dimensions=dimensions # Dimensions will be a list of lists, first is x-range, second is y-range.
		self.name = name
		self.type = type
		if type=="Chamber":
			chamber_list.append(self)
		if type=="Corridor":
			corridor_list.append(self)

	def __repr__(self):
		return self.name

#ALL ROOMS/CORRIDORS
entrance = room("The first room of the dungeon, a place to prepare yourself for the trials which await you. Beneath the \
rubble a paved floor is visible in places. The ceiling is held up by steel frames. Two passages lead from the space, old \
and man-made.",
				[[-2,2],[0,4]], "Entrance", "Chamber")
lcorridor = room("A short corridor to the left of the entrance. A smaller version of the inscription in the entrance is \
painted on a wall, though the paint has almost faded.",
				 [[-3,-3],[2,2]], "Left Corridor", "Corridor")
leftroom = room("A dark and empty room, the wind whistles through the corridor behind you, and an archway looms ahead, \
shrouded in darkness. A low growl seems to come from behind it.",
				[[-6,-4],[1,5]], "Side Chamber", "Chamber")
archway = room("An archway leading to a room shrouded in darkness. What seems like a heavy breathing sound can be heard. \
Be cautious.",
			   [[-6,-5],[6,6]], "Archway", "Corridor")
store = room("A small room with a couple of empty barrels, a chest at one corner, and two monsters asleep, blocking your \
way. You may fight for possible treasure, or step back, carefully, so as to not wake the beasts.", # Put as lore block.
			 [[-6,-4],[7,8]], "Store Room", "Chamber")
rcorridor = room("A corridor to the right of the entrance. The room ahead is visible, but barely. It seems more refined \
than the left corridor, painted and polished.",
				 [[3,4],[2,2]], "Right Corridor", "Corridor")
rightroom = room("A small chamber, lit by the dying embers of a torch. The faded paint on the walls might have seemed \
welcoming once. The remains of a door lie beside a doorway set in the opposite wall, and a bottle lies in the middle of \
the room, corked and half-empty.",
				 [[5,7],[2,5]], "Antechamber", "Chamber")
doorway = room("A short, tiled path towards the next room continues from the doorway. The darkness ahead seems impenetrable,\
 despite the torch you hold. The roof, illuminated, has the same symbol on it, in a rust-like colour, and looks merely days old.",
			   [[8,8],[4,4]], "Doorway", "Corridor")
diningroom = room("A carpeted room with many small tables, plates and silverware laid, but no food in sight. Dust coated \
the ground but the tablecloths shone bright. A bag lay on the last table.",
				  [[9,11],[4,10]], "Dining Room", "Chamber")
longcorridor = room("A long corridor, with a floor of marble and mosaic art hung on the walls. A set of double doors lies\
 at the end, looking pristine as can be in the light of the torch.",
					[[5,8],[9,9]], "Beautiful Corridor", "Corridor")
ballroom = room("A solid wood floor lay under your feet, a chandelure hung from the centre of the roof, and the walls were wood-panelled.\
Two carved wood pedestals welcomed you into the ballroom. On each of them sat a grotesque creature, both of them snarling at you,\
 waiting for you to approach.",
				[[-2,4],[6,10]], "Ballroom", "Chamber")


# Define being inside a room.
def findroom(cord_): # in_room_ and croom_ are local variables whose values will be assigned to the global variables in_room and croom.
	in_room_ = False
	croom_ = None
	for roomname in corridor_list:
		if roomname.dimensions[0][0] <= cord_[0] <= roomname.dimensions[0][1] and\
				roomname.dimensions[1][0] <= cord_[1] <= roomname.dimensions[1][1]:
			croom_ = roomname
			in_room_ = True
			break
	for roomname in chamber_list:
		if roomname.dimensions[0][0] <= cord_[0] <= roomname.dimensions[0][1] and\
				roomname.dimensions[1][0] <= cord_[1] <= roomname.dimensions[1][1]:
			croom_ = roomname
			in_room_ = True
			break
	return in_room_ , croom_

#WALLS
wallcords=[]
for x in range(-7,13):
	for y in range(-1,13):
		if not findroom([x,y])[0]:
			wallcords.append([x,y])
wallcords.remove([0,-1])

def walls_surrounding():
	r = []
	for wall in wallcords:
		x = wall[0]
		y = wall[1]
		for useless in rooms_been_to:
			x1 = useless.dimensions[0][0]-1
			x2=useless.dimensions[0][1]+1
			y1=useless.dimensions[1][0]-1
			y2=useless.dimensions[1][1]+1
			if x in range(x1,x2+1):
				if y == y1 or y==y2:
					r.append(wall)
			if y in range(y1,y2+1):
				if x == x1 or x==x2:
					r.append(wall)
	return r


#MOVES
slash = move("Slash", 30, 75, 2)
bite = move("Bite", 50, 65, 3, [-4,-4,-8])
pounce = move("Pounce", 60, 80, 4, [-6,-10,-15])
roar = move("Roar", 20, 90, 3, [-10,-5,0],[10,-5,0])
atomic = move("Atomic Split Slash", 75, 65, 4, [-5,5,0], [12,0,0])
kagizume = move("Karyu no Kagizume", 40, 90, 2, [-2,-2,-2], [3,3,3])
hoko = move("Rairyu no Hoko", 60, 80, 5, [0,0,-13], [0,0,12])
rasengan = move("Rasengan", 60, 80, 3, [-5,0,0], [0,7,-5])
shadow = move("Shadow Strike", 80, 98, 6, [-4,-7,5], [5,3,3])
spook = move("Spook", 10, 90, 3, [-15,-10,-5])
paralyze = move("Paralyze", 15, 70, 4, [-15,-15,-15],[5,3,3])
foul = move("Foul Feeder", 80, 90, 7, [-6,-6,-6], [5,11,5])
rage = move("Rage", 0, 75, 5, [-5,-5,-5], [20,20,20])
lionhit = move("Lion King's Majestic Blow", 100, 80, 5)
wolfhit = move("Wolf Queen's Deadly Strike", 100, 80, 5)
chimera = move("Chimeraen Cry", 40, 95, 4, selfstat = [4,4,4], action = lambda user: setattr(user,'HP',user.HP+40))

#DEFINE PLAYER
player = entity("You", [53, 46, 67, 400, 40],
				[atomic, kagizume, hoko, rasengan],
				["Your HP has reached 0! The pain is overbearing, and your vision goes blurry. Unable to move, you give \
up and fall to the ground, defeated, as your consciousness fades.",
				 "Drained of magic, you are unable to use any move, and mustering your strength, you throw a feeble punch."])

# EVENT BLOCKS: Battle, Treasure, Potion, Lore

#Dict of block and enemy. Tuples of blocks are keys.
battle_blocks = {(-4,7):entity("Beast", [40,50,20,240,20],
							   [slash,bite,pounce,roar],
							   ["The Beast howled, and its eyes glowed red as it fell to the ground, then exploded.",
								"Looking tired, the beast made a feeble attempt to attack.", "growl"]),
				 (-5,8):entity("Goblin", [40,30,70,180,30],
							   [slash,bite,pounce,roar],
							   ["The Goblin screeched, the glow in its eyes fading, and then it burst into stinging yellow powder.",
								"Looking tired, the goblin made a feeble attempt to attack.", "screech"]),
				 (10,4):entity("Shadowy Demon", [60,45,60,360,30],
							   [slash, shadow, spook, paralyze],
							   ["A loud groan seemed to travel through the walls and the ground, and the demon cloaked in shadow began to fold in on itself, cursing you as it did.",
								"Its tendrils becoming sluggish, the demon lunged at you in desperation.", "cackle"]),
				 (3,8):entity("Fiendish Feline", [60,60,60,340,35], [bite,lionhit,rage,chimera],
				              ["With a hiss, goop dribbled off the creature, leaving behind a ghostly cat which leapt towards the roof, soaring free.",
				               "Fatigue overcoming the feline, it faltered in its strike, claws scratching you.", "yeowl"]),
				 (3,10):entity("Corrupted Canine",[60,60,60,340,35],[bite,lionhit,rage,chimera],
				               ["With a blast, dust flew off the creature, leaving behind a spirit-like dog, which glided into the ground, diving unchained.",
				                "Exhaustion overcoming the canine, it wavered in its blow, claws scraping you.", "howl"])
				 }
#Again, tuple(block):[T/F, "Text", "Code"]. First whether already happened, then to-be-printed, then input of event() function.
# For treasure and potions.
have_amulet = False
def event(x):
	global player
	if x=="Shield":
		player.atk += 18
		player.dfc += 27
		player.spd -= 4
		player.moveset.append(foul)
	elif x=="Map":
		global map_obtained
		map_obtained = True
	elif x=="Heal1":
		if player.HP <= player.HP_max - 100:
			player.HP += 100
		else:
			player.HP = player.HP_max
	elif x=="Heal2":
		player.HP = player.HP_max
		player.MP = player.MP_max
		global have_amulet
		have_amulet=True

def strike(text):
	result = ''
	for c in text:
		result = result + c + '\u0336'
	return result

event_blocks = {
				(-4,8):[True, "You open the chest, and find a red and black shield, and a short black blade. There may \
be more monsters, so these could come in handy.", "Shield"],
				(-6,2):[True, "You see a board lying on the ground. On it is painted what seems like a map of the \
building. Type map to display it.", "Map"],
				(6,3):[True, "You uncork the bottle to sniff it. Immediately, it evaporates and enters your nose. You \
feel invigorated.",
					   "Heal1"],
				(10,8):[True, "You open the bag, and find a few personal belongings, along with a water bottle, a \
corroded amulet, and two full bottles, similar to the half-empty one in the antechamber. Injured by the Demon, and \
fearing what may lie in the final room, you use them both.\n\nYou feel completely healed, and feel like you could throw \
an elephant a " + strike("mile") + " kilometre. (\#GoMetric!)",
						"Heal2"]
				}

# Doorblocks will not be the blocks which are walled in, but the blocks adjacent.
# Syntax - (cord of adj block):[T/F, "Text", condition for unlock, [locked block cord] ]
# Text must illustrate direction of door for unambiguity.
doorcords = []
door_blocks = {(2,2):[True, "A crude door blocks your way to the right. It is held closed by two locks.",
					  battle_blocks[(-4,7)].HP <= 0 and battle_blocks[(-5,8)].HP <= 0,
					  [3,2]],
			   (6,9):[True, "The double doors to the left are locked. The keyhole is elegant and unique, made of metal.",
					  battle_blocks[(10,4)].HP <= 0,
					  [5,9]]}
#Append to doorblocks when seen.
# Lore blocks, always print.
lore_blocks = {(0,4):"There's an inscription on the wall in front of you - it looks like a crudely drawn helmet.",
			   (-4,2):"Enter numbers for attacks. Attacks use up magic.\nSome health and magic recovered with every step."}

rooms_been_to = []
# Printing map of dungeon.
def map_print():
	map = "MAP\nE is exit, I is a wall, D is a door.\n? is unknown, X is a monster, you are Y.\n! is an event, # is lore,\
 _ is just an empty space.\n"
	for y in range(12,-2,-1):
		for x in range(-7,13):
			if (x,y) == (0,-1):
				map += "E "
			elif [x,y] in walls_surrounding():
				map += "I "
			elif [x,y] in doorcords:
				map += "D "
			elif findroom([x,y])[1] not in rooms_been_to: # Rooms_been_to added to with every findroom.
				map += "? "
			elif (x,y) in battle_blocks and battle_blocks[(x,y)].HP>0:
				map += "X "
			elif (x,y) in event_blocks and event_blocks[(x,y)][0]:
				map += "! "
			elif [x,y] == cord:
				map += "Y "
			elif (x,y) in lore_blocks:
				map += "# "
			else:
				map += "_ "
		map += "\n"
	print(map)
map_obtained = False

#ACTION
def action(act):
	global cord
	if act=="l":
		cord[0]-=1
	elif act=="r":
		cord[0]+=1
	elif act=="b":
		cord[1]-=1
	elif act=="f":
		cord[1]+=1
	elif act=="i":
		print(croom.info)
	elif act=="map" and map_obtained: # map_obtained false until event block for map.
		map_print()
	elif act=="s":
		player.stats_print()
	elif act=="m":
		print(player.movenames())
	elif act=="e":
		return 0
	else:
		print("Inavalid action!")
	return 1

#START
if input("You stand before the dungeon's entrance.\nPress f to enter.")=="f":
	continu = 1
	croom = entrance
	#cord = [-3,5] # For testing.
else:
	continu = 0

#While loop for main stuff.
ask = True
while continu==1:
	cord_store = cord.copy() #Save previous position.

	if ask:
		if not action(input("Perform an action.")): #Action
			break
	ask = True

	if cord in wallcords: #Check for walls.
		print("There's a wall in the way.")
		cord = cord_store.copy()
		continue

	if cord in doorcords: #Check for locked doors.
		print("There's a door in the way.")
		cord = cord_store.copy()
		continue


	in_room, croom = findroom(cord)
	if not in_room:
		raise ValueError("Something went wrong, you were not found to be in any room. Please restart.")
	if croom not in rooms_been_to:
		rooms_been_to.append(croom)

	if cord != cord_store: #So healing only on moving.
		if player.MP < player.MP_max:
			player.MP+=1
		if player.HP <= player.HP_max - 5:
			player.HP+=5
		else:
			player.HP = player.HP_max

	print(f"You're in {croom}.")

	tcord = tuple(cord)

	if tcord in battle_blocks:
		if po_battle(player, battle_blocks[tcord]):
			print("The monster was apparently also guarding a key. It might help with the locks.")
		if player.HP <= 0:
			if have_amulet:
				print("As you are taking your last breaths, a light shines in your bagpack, and the once corroded \
amulet floats out, good as new and bright as the sun. A warm feeling fills you as the amulet dissolves into\
 the air, and you stand, ready to battle again.")
				player.HP = player.HP_max
				player.MP = player.MP_max
				have_amulet = False
				ask = False
				continue
			else:
				print("You lost.")
				break

	elif tcord in event_blocks and event_blocks[tcord][0]:
		print(event_blocks[tcord][1])
		event(event_blocks[tcord][2])
		event_blocks[tcord][0] = False

	elif tcord in door_blocks and door_blocks[tcord][0]:
		door = door_blocks[tcord][3]
		if door not in doorcords:
			doorcords.append(door)
		print(door_blocks[tcord][1])
		print("Try to open the door.")
		if door_blocks[tcord][2]:
			doorcords.pop(door)
			print("The door opened! The keys worked!")
			door_blocks[tcord][0] = False
		else:
			print("It seems you don't have the right keys.")

	elif tcord in lore_blocks:
		print(lore_blocks[tcord])

else:
	print("All right, let's leave then.")

input("Press enter to exit.")
