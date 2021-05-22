from AdvDung.battlesys import *
from random import randint, choice, choices
'''
Possible see-all mode.
Add choice of player.
'''

#MOVES
slash = move("Slash", 30, 75, 2)
bite = move("Bite", 50, 65, 3, [-4,-4,-8])
pounce = move("Pounce", 60, 80, 4, [-6,-10,-15])
roar = move("Roar", 20, 90, 3, [-10,-5,0],[10,-5,0])
atomic = move("Atomic Split Slash", 75, 65, 4, [-5,5,0], [12,0,0])
kagizume = move("Karyu no Kagizume", 40, 90, 2, [-2,-2,-2], [3,3,3])
hoko = move("Rairyu no Hoko", 60, 80, 4, [0,0,-13], [0,0,12])
rasengan = move("Rasengan", 60, 90, 3, [-5,0,0], [0,7,-3])
shadow = move("Shadow Strike", 80, 98, 6, [-2,-2,5], [5,3,3])
spook = move("Spook", 10, 90, 3, [-13,-8,-5])
paralyze = move("Paralyze", 15, 70, 4, [-11,-13,-13],[5,3,3])
foul = move("Foul Feeder", 80, 90, 7, [-6,-6,-6], [5,11,5])
OP = move("Overpowered", 100, 100, 1, [-15,-15,-15],[17,15,15])

#CHARACTERS
player1 = entity("You", [randint(50,75), randint(50,75), randint(50,75), randint(380,420), randint(35,45)],
                [atomic, kagizume, hoko, rasengan, foul],
                ["Your HP has reached 0! The pain is overbearing, and your vision \
goes blurry. Unable to move, you give up and all to the ground, defeated, as your consciousness fades.",
                 "Drained of magic, you are unable to use any move, and mustering your strength, \
you throw a feeble punch."])

beast = entity("Beast", [40,50,20,240,20],
               [slash,bite,pounce,roar],
               ["The Beast howled, and its eyes glowed red as it fell to the ground, then exploded.",
                "Looking tired, the beast made a feeble attempt to attack.", "menacing growl"])

goblin = entity("Goblin", [40,30,70,180,30],
                [slash,bite,pounce,roar],
                ["The Goblin screeched, the glow in its eyes fading, and then it burst into stinging yellow powder.",
                 "Looking tired, the goblin made a feeble attempt to attack.", "menacing screech"])

demon = entity("Shadowy Demon", [60,45,60,360,30],
               [slash, shadow, spook, paralyze],
               ["A loud groan seemed to travel through the walls and the ground, and the demon cloaked \
in shadow began to fold in on itself, cursing you as it did.",
                "Its tendrils becoming sluggish, the demon lunged at you in desperation.", "menacing cackle"])


print("BATTLE SIMULATOR")

def rand_move():
	move_ = move(choice(["Slash", "Bite", "Pounce", "Burp", "Roar", "Growl", "Destruction", "Scratch",
	                     "3-Tiered Chocolate Cake", "Strike", "Counter", "Swipe","Smash","Destroy",
	                     "Punch","Giggle","Stomp","Kick","Jeer","Rick Roll","Unforgivable Curse",
	                     "Forbidden Jutsu","Lysanderoth's Gun","Lamb Sauce","Cruelty","Whirlwind",
	                     "Curiosity","Universe-shifting Clap","Samehada","Jump Float Serve","Guess Block",
	                     "Enigmatic Demolition","Moonlight Sword - 6th form","Unending Cheescakes","Poisonous Fart",
	                     "Panicky Pancake","Awful Rendition of Pop Songs","Toenail Filing","Minus Tempo Spike"]),
	             randint(10, 100), randint(10,100), randint(1,10),
	             [randint(-12,4) for i in range(3)], [-randint(-12,4) for i in range(3)])
	return move_

def rand_enemy():
	enemy = entity(choice(["Beast", "Goblin", "Demon", "Orc", "Monster", "Dragon", "Drakon", "Hydra", "Titan",
	                       "Reindeer","Masquerade","Rogue","Thief","Bandit","Direwolf","Wild Pokemon",
	                       "DRAFT","Debt","Orochimaru","Madara","Generic Bad Guy","Team Rocket Grunt",
	                       "Zeref","You Know Who","Nose-less Idiot","King Dragon","Evil King","Lysanderoth",
	                       "Dormammu","Purple Prune","Guess Monster","Shiggy","Touya Todoroki",
	                       "Sebastian Morgenstern","Student Council","Youkai","That One Bad Guy","Evil Elephant",
	                       "Dark Reflection of Yourself","Pimple","Door-to-door Salesman","Vacuum Cleaner",
	                       "Crushing Debt","Nivea Skin Cream","Reheated Nimbu Soda Jamun Flavour","Motu Cheeks",
	                       "Bad Guy Marvel copyrighted","Bad Guy Disney copyrighted",
	                       "That One Friend Who Keeps Spoiling Endings","An Unsolved Rubik's Cube",
	                       "Conspiracy Theorist"]),
	               [randint(25,100) for i in range(3)] + [randint(125,600), randint(15,60)],
	               [rand_move() for i in range(4)],
	               ["The enemy was defeated! You sustained damage due to the enemy's destruction.",
	                "The enemy, out of magic, launches at you in desperation.",
	                choices(["","desperate","soundless","unending","noisy","sky-piercing","disturbing","malicious",
	                         "soul-rending"],
	                        [6,1,1,1,1,1,1,1,1])[0] + " "
	                +choice(["growl", "shriek", "laugh", "sauce", "cry", "howl", "bark", "meow", "yell",
	                        "scream", "screech", "cackle","'Where's the lamb sauce?!'","stutter",
	                        "mutter","peanut butter","bellow","shout","holler","yodel","'May the Force be with you!'",
	                        "tirade","echo","fart","burp","yelp","squawk","gurgle","blub-blub","silence"])])
	return enemy

def rand_battle(player):
	opponent = choices([rand_enemy(), beast, goblin, demon], [7,1,1,1])[0]
	po_battle(player, opponent)
	opponent.full_heal()
	return player.HP > 0

wins = 0
player = player1 #Choice later.
while True:
	if rand_battle(player):
		print("Victory!")
		wins += 1
		print(f"You have a streak of {wins} wins!")
		print("Now onto the next.\n")
		player.HP += player.HP_max / 2
		player.MP += player.MP_max / 2
	else:
		print("You were defeated.")
		again = input(f"You won {wins} times! Would you like to try again? (y/n)")
		if again == "y":
			wins = 0
			player.HP = player.HP_max
			player.MP = player.MP_max
			continue
		else:
			break

input("Press enter to exit.")


