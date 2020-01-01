## Python 3.6
## Tic-Tac-Toe by math
## License: MIT
## 

## Order of precedence for deciding where to go next. 
## 1. See if you can win. 
## 2. See if you need to block someone else to win. 
## 3. See if you can add to a row that only has one of your own placed on. 
## 4. Place your symbol on a row with no other symbols. 

import math

## The grid of blank spaces.
t = [3, 1, 1, 2, 1, 1, 1, 1, 1]
solutions = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[2, 4, 6], [0, 4, 8]]

x = 3
o = 2
b = 1			# Blank = 1

def print_grid():
	print ("\n")
	s = ""						## String that will contain the view.
	c = 0						## Used for figuring out the row.
	for item in t:
		s = s + str(item) + " "
		c += 1
		if (c%3 == 0): s = s + ("\n") 		## If the last column num is divisible by 3, put it on a new row.
	print (s)

def check_win(player):
	"""	Purpose: to see if there is a row where you can win.
	
		Player: 	string	: x or y
		row_value:  integer	: Calculated value of the row. (All entered values multiplied)

		returns:	True	: If the row can be a winning row.
					False	: If the row cannot become a winning row.
					
	"""
	p = player_to_num(player)

	for row, possible_solution_set in enumerate(solutions):
		row_value = 1
		for num in possible_solution_set:
			row_value = row_value * t[num]

			if (row_value != 1) and (p == math.sqrt(row_value)): 
				for num in possible_solution_set:
					if t[num] == 1:
						t[num] = p
						return True	

	return False
		
def check_block(player, row):
	
	""" Purpose: If the opposing team can win by adding to this row, block it.
	
		row: 	integer : that fits within the solutions list
		player: string 	: x or y (the person making the move)
		
		returns:	True	: If the row can be a winning row.
					False	: If the row cannot become a winning row.
	"""
	op = opposite_player(player)
	p  = player_to_num(player)
	
	for row, possible_solution_set in enumerate(solutions):
		row_value = 1
		for num in possible_solution_set:
			row_value = row_value * t[num]
			
			if (row_value != 1) and (op == math.sqrt(row_value)): 
				for num in possible_solution_set:
					if t[num] == 1:
						t[num] = op	
						return True		
	
	return False

def win_row(player, row):
	## NOT IN USE
	""" Purpose: If the row can be won, add your item there and win the game.
				 The whole row is re-filled with your number.
	
		row: 	integer : that fits within the solutions list
		player: string 	: x or y (the person making the move)
	"""
	p = player_to_num(player)
	
	for num in solutions[row]:
		update_coordinates 		= num
		t[update_coordinates] 	= p			
		
		print (update_coordinates)

def check_best(player):
	""" Determine if there is a row that already has one of your markers on it.
		The first row that has a marker on it already is updated with a second one.
	
		returns:	True	: If any row is updated with a second marker.
					False	: If there is nothing that can be updated.		
	"""
	
	p  = player_to_num(player)
	
	for row, possible_solution_set in enumerate(solutions):
		row_value = 1
		for num in possible_solution_set:
			row_value = row_value * t[num]	
			
			if row_value == p:
				for num in possible_solution_set:
					if t[num] == 1:
						t[num] = p
						return True

	return False

def find_blank_row(player):
	""" If there no other move works, find a blank row and start putting your marker on it.
	
		returns:	True	: If any row is updated with a marker.
					False	: If there is nothing that can be updated.	
	"""
	p  = player_to_num(player)
	
	for row, possible_solution_set in enumerate(solutions):
		row_value = 1
		for num in possible_solution_set:
			row_value = row_value * t[num]
			
			if row_value == 1: 
				possible_solution_set[0] = p
				return True
	
	return False		

def find_any_space(player):
	""" If there are no other options, just find a space to place marker.
	
		returns:	True	: If any square is updated with a marker.
					False	: If there is nothing that can be updated.			
	"""			
	
	p  = player_to_num(player)
	
	try:
		num = t.index(1)
		t[num] = p
		return True
	except:
		print("No move can be made.")
		return False
	
def opposite_player(player):
	""" Find the opposite player and return the opposite player number.
		
		Player: 	string 	: x or y
		returns: 	string	: x or y
	"""	
	
	if player == "x":
		opp_player = "y"
	elif player == "y":
		opp_player = "y"
	else: 
		opp_player = "z"

	print (opp_player)		
	return opp_player
	
def player_to_num(player):
	""" Player: 	string : x or y
		Returns: 	int	   : 1 = None, 2 = y, 3 = x
	"""
	if player == "x": 
		p = 3 
	elif player == "y":
		p = 2
	else:
		p = 1 					## Just to capture bad programming. 				
	
	return p

def test_board(t):
	""" Check to see if any of the rows on the board have won.
	"""
	pass
	
def calc_values(t, solutions):
	"""
	"""
	if check_win("x"):
		print ("win!")
	else: 
		print ("not a win.")
	
	print_grid()
		
	## Test for Winning
	# print ("### Winning Test ###") 				## Remove after testing

	# for row, possible_solution_set in enumerate(solutions):
		# row_value = 1
		# for num in possible_solution_set:
			# row_value = row_value * t[num]
		
		# if check_win("x", row_value):
			# win_row("x", row)
			# break
		
		# print (row, row_value)

	
	# print ("### Winning Test End ###\n")			## Remove after testing

	

	
	# ## Test for blocking
	# print ("### Blocking Test ###") 				## Remove after testing
	# row_value = 1
	# c = 0
	# for possible_solution_set in solutions:
		# for num in possible_solution_set:
			# row_value = row_value * t[num]
				
		# if check_block("x", row_value):
			# print(num)
			# for num in possible_solution_set:
				# if t[num] == 1:
					# t[num] = 3						## TODO - Make this dynamic to x or y.
			# print('yup')
			# #add_item("x", location)

		# print (c, row_value)
		# c += 1
		# row_value = 1

	# print ("### Blocking Test End ###")			## Remove after testing

	# ## Test for Next Move
	# print ("### Next Move Test ###") 				## Remove after testing
	# row_value = 1
	# c = 0
	# for possible_solution_set in solutions:	
		# for num in possible_solution_set:
			# row_value = row_value * t[num]
	
		# check_best("x", row_value, c)	
		
		# print (c, row_value)
		# c += 1
		# row_value = 1	
			
	# print ("### Next Move Test End ###")			## Remove after testing

	# ## Test for Blank Move
	# print ("### Blank Move Test ###") 				## Remove after testing
	# row_value = 1
	# c = 0
	# for possible_solution_set in solutions:	
		# for num in possible_solution_set:
			# row_value = row_value * t[num]
	
			# if row_value == 1: 
				# t[0] = 3;							## Reset for x
				
		# print (c, row_value)
		# c += 1
		# row_value = 1	
		
	# print ("### Blank Move Test End ###")			## Remove after testing
	
print_grid()
calc_values(t, solutions)

print_grid()

### Reference Materials
## 	Enumerations and counting in loops
## 		https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
##
##	Cubed Values
##		p**(1./3.) is finding the cubed root of a value. 	
##		(https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python/28014245)
