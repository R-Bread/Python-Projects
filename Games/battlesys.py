from random import randint

''' To do:
pp_turn, pp_battle
'''
def donone(*x):
	pass

class move:
	def __init__(self, name, rawdmg, acc, cost, otherstat=None, selfstat=None,
	             action: "Use Lambda for input, user always an argument." = donone):
		if selfstat is None:
			selfstat=[0, 0, 0]
		if otherstat is None:
			otherstat=[0, 0, 0]
		self.action = action
		self.name = name
		self.raw_damage = rawdmg
		self.self_stat_changes = selfstat #Buffs/nerfs, are added.
		self.other_stat_changes = otherstat
		self.accuracy = acc #Percentage
		self.cost = cost

class entity:
	def __init__(self, name, stats, moveset, dialogues): # Stats is a list of ints, moveset a list of moves.
		self.name = name # Expected values of atk, dfc, spd are between 0 and 100. 100 is really strong, \
		# player has maybe 50-80.
		self.stats = stats
		self.max_stats = stats[3:] #Only stores max HP and MP.
		self.moveset = moveset
		self.dialogues = dialogues # Dialogues include on fainting, and others if wanted. List.
		self.faint_dialogue = dialogues[0]
		self.out_of_magic = dialogues[1]
		self.death_damage = round(self.atk * self.spd * self.MP / 4000,1)
		self.basic_move = move("Last Resort", round(self.atk * 0.6 + self.dfc * 0.4,1),
		                       round(self.spd * 0.9  + self.HP / 15, 1),0)
		# Not to be seen, used when out of magic.

	def attack(self, other, _move):
		user = self
		move_acc = _move.accuracy
		hit_chance = move_acc + self.spd * 0.9 - other.spd * 1.1 #Percentage
		self.MP -= round(_move.cost*0.4, 1) # Part lost if missed, rest lost if hit. Might remove if messes up.

		if randint(1,100) <= hit_chance:

			modifier = self.atk / other.dfc
			if modifier < 1/5:
				modifier = 1/5
			elif modifier > 5:
				modifier = 5
			damage = round(_move.raw_damage*modifier*randint(95, 115)/100, 1)
			other.HP -= damage
			self.MP -= round(_move.cost*0.6, 1)

			for i in range(3):
				self.stats[i] += _move.self_stat_changes[i]
				other.stats[i] += _move.other_stat_changes[i]

				if self.stats[i] <= 0:
					self.stats[i] = 1
				if other.stats[i] <= 0:
					other.stats[i] = 1

			_move.action(user)

			print(f"{self.name} attacked {other.name} using {_move.name}! It did {damage} damage.")
		elif self.name == "You":
			print(f"Your {_move.name} missed!")
		else:
			print(f"{self.name}'s {_move.name} missed!")

	def full_heal(self):
		self.HP = self.HP_max
		self.MP = self.MP_max

	def stats_print(self):
		print(f"Attack: {self.atk}\nDefence: {self.dfc}\nSpeed: {self.spd}\nHealth: {self.HP}\nMagic: {self.MP}")
	def movenames(self):
		return [_move.name for _move in self.moveset]
	def moves_print(self):
		print("Power, Accuracy, Cost:")
		for _move in self.moveset:
			print(f"{_move.name}: {_move.raw_damage}, {_move.accuracy}%, {_move.cost} MP")

	# The following code makes self.atk and the rest properties, so they act like attributes but they are essentially a
	# simpler way to write self.stats[0], and easier to understand.
	@property
	def atk(self):
		return self.stats[0]
	@atk.setter
	def atk(self, value):
		self.stats[0] = value

	@property
	def dfc(self):
		return self.stats[1]
	@dfc.setter
	def dfc(self, value):
		self.stats[1]=value

	@property
	def spd(self):
		return self.stats[2]
	@spd.setter
	def spd(self, value):
		self.stats[2]=value

	@property
	def HP(self):
		return self.stats[3]
	@HP.setter
	def HP(self, value):
		self.stats[3]=value

	@property
	def MP(self):
		return self.stats[4]
	@MP.setter
	def MP(self, value):
		self.stats[4]=value

	@property
	def HP_max(self):
		return self.max_stats[0]
	@HP_max.setter
	def HP_max(self, value):
		self.max_stats[0]=value

	@property
	def MP_max(self):
		return self.max_stats[1]
	@MP_max.setter
	def MP_max(self, value):
		self.max_stats[1]=value

def inp_exit(condition):
	if condition:
		input("Press enter to exit.")
		exit(2) # To allow exit at any input, if certain input given. See while loop below for use.


# po_turn, po_battle are for player vs opponent.
def po_turn(player, opponent):
	for x in (player, opponent):
		x.stats[3:5] = list(map(round,x.stats[3:5],[1,1])) # Rounds MP, HP every turn.
	print(f"{opponent.name}: {opponent.HP} HP\n{player.name}: {player.HP} HP, {player.MP} MP", end='')
	# Show MP, HP every turn. Option to see all stats, exit.
	command = input()
	if (command) == "s":
		player.stats_print()
	elif command == "m":
		player.moves_print()
	elif command == 'e':
		print("All right, let's leave then.")
		inp_exit(True)

	if any([player.MP>=_move.cost for _move in player.moveset]):
# Checking for enough MP for move above.
		while True: # Making sure accidental presses don't break program, and that there's MP for chosen move.
			try:
				move_no = int(input(f"Choose your move:\n{player.movenames()}"))
				inp_exit(move_no == -1)
				while move_no not in range(1, len(player.moveset)+1):
					move_no = int(input(f"Invalid number!\nChoose your move:\n{player.movenames()}"))
					inp_exit(move_no==-1)

				move_used = player.moveset[move_no-1]
				while move_used.cost > player.MP:
					move_no = int(input(f"Not enough MP! \nChoose your move: \n{player.movenames()}"))
					inp_exit(move_no==-1)
					move_used = player.moveset[move_no-1]
				break
			except ValueError:
				pass

		player.attack(opponent, move_used) #Attack if all's good.
	else: # For when not enough MP.
		player.MP = 0
		print(player.out_of_magic)
		player.attack(opponent, player.basic_move)

# Same but for computer opponent.
	if  any([opponent.MP>=_move.cost for _move in opponent.moveset]):

		move_used = opponent.moveset[randint(0, len(opponent.moveset)-1)]
		while move_used.cost > opponent.MP:
			move_used = opponent.moveset[randint(0, len(opponent.moveset)-1)]

		opponent.attack(player, move_used)
	else:
		print(opponent.out_of_magic)
		opponent.attack(player, opponent.basic_move)


	if opponent.HP <= 0:
		print(opponent.faint_dialogue)
		return False
	elif player.HP <= 0:
		print(player.faint_dialogue)
		return False
	else:
		return True # The returned value is fed into the while loop in the battle function.

def po_battle(player, opponent, heal=0): # heal=0 means standard - heals atk,dfc,spd, not HP or MP. 1 is healall.
	# heal=2 is like 0 but atk,dfc,spd are averaged.
	if opponent.HP <= 0:
		return False # Battle did not happen.
	player_stat_record = player.stats[:3]
	opponent_stat_record = opponent.stats[:3]

	print(f"The {opponent.name} has detected your presence! With a {opponent.dialogues[2]}, it attacks!")
	print("Type s to see stats on a turn, or enter to attack.")

	while po_turn(player, opponent):
		pass
	else:
		player.HP -= round(opponent.death_damage * player.HP / player.dfc / 5, 0)
	if player.HP <= 0:
		return False # Battle lost.

	if heal==0:
		for i in range(3):
			player.stats[i] = player_stat_record[i]
			opponent.stats[i] = opponent_stat_record[i]
	elif heal==1:
		for i in range(5):
			player.stats[i] = player_stat_record[i]
			opponent.stats[i] = opponent_stat_record[i]
	elif heal==2:
		for i in range(3):
			player.stats[i] = (2*player_stat_record[i] + player.stats[i])/3
			opponent.stats[i] = opponent_stat_record[i]
	return True # Battle won.