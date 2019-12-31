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
t = [2, 1, 1, 2, 1, 1, 1, 1, 1]
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

def check_win(player, row_value):
	"""	Purpose: to see if there is a row where you can win.
	
		Player: 	string	: x or y
		row_value:  integer	: Calculated value of the row. (All entered values multiplied)

		returns:	True	: If the row can be a winning row.
					False	: If the row cannot become a winning row.
					
		## Interesting Note	
		p**(1./3.) is finding the cubed root of a value. 	
			(https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python/28014245)
	"""
	p = player_to_num(player)

	if (row_value != 1) and (p == math.sqrt(row_value)): 
		print (row_value, ": Winning row")
		return True
	else:
		print (row_value, ": Not winning")
		return False
		
def check_block(player, row):
	""" Purpose: If the opposing team can win by adding to this row, block it.
	
		row: 	integer : that fits within the solutions list
		player: string 	: x or y (the person making the move)
		
		returns:	True	: If the row can be a winning row.
					False	: If the row cannot become a winning row.
	"""
	opposite = opposite_player(player)
	
	p  = player_to_num(player)
	
	print (opposite)
	
	result = check_win(opposite, row)
	
	return result
	
def win_row(player, row):
	""" Purpose: If the row can be won, add your item there and win the game.
				 The whole row is re-filled with your number.
	
		row: 	integer : that fits within the solutions list
		player: string 	: x or y (the person making the move)
	"""
	p = player_to_num(player)
	
	for num in possible_solution_set:
		update_coordinates 		= solutions[row][num]
		t[update_coordinates] 	= p			
		
		print (update_coordinates)

def check_best(player, row_value, row):
	p  = player_to_num(player)
	x = solutions[row]
	
	if row_value == p:
		for i in x:
			if t[i] == 1:
				print (t[i])
				t[i] = p
				break
				return True
	else:
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
	
	## Test for Winning
	print ("### Winning Test ###") 				## Remove after testing
	row_value = 1
	c = 0
	for possible_solution_set in solutions:
		for num in possible_solution_set:
			row_value = row_value * t[num]
		
		if check_win("x", row_value):
			win_row("x", c)
			break
		
		print (c, row_value)
		c += 1
		row_value = 1
	
	print ("### Winning Test End ###\n")			## Remove after testing


	## Test for blocking
	print ("### Blocking Test ###") 				## Remove after testing
	row_value = 1
	c = 0
	for possible_solution_set in solutions:
		for num in possible_solution_set:
			row_value = row_value * t[num]
				
		if check_block("x", row_value):
			print(num)
			for num in possible_solution_set:
				if t[num] == 1:
					t[num] = 3						## TODO - Make this dynamic to x or y.
			print('yup')
			#add_item("x", location)

		print (c, row_value)
		c += 1
		row_value = 1

	print ("### Blocking Test End ###")			## Remove after testing

	## Test for Next Move
	print ("### Next Move Test ###") 				## Remove after testing
	row_value = 1
	c = 0
	for possible_solution_set in solutions:	
		for num in possible_solution_set:
			row_value = row_value * t[num]
	
		check_best("x", row_value, c)	
		
		print (c, row_value)
		c += 1
		row_value = 1	
			
	print ("### Next Move Test End ###")			## Remove after testing

	## Test for Blank Move
	print ("### Blank Move Test ###") 				## Remove after testing
	row_value = 1
	c = 0
	for possible_solution_set in solutions:	
		for num in possible_solution_set:
			row_value = row_value * t[num]
	
			if row_value == 1: 
				t[0] = 3;							## Reset for x
				
		print (c, row_value)
		c += 1
		row_value = 1	
		
	print ("### Blank Move Test End ###")			## Remove after testing
	
print_grid()
calc_values(t, solutions)

print_grid()

## Prints the rows.
# for i in range (9):
	# m = i % 3
	# print(i, ":", m)
