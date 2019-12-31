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
t = [3, 3, 1, 1, 3, 1, 1, 1, 1]
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
	
		Player: x or y
		row_value: Calculated value of the row. (All entered values multiplied)
				
		## Interesting Note
		p**(1./3.) is finding the cubed root of a value. 	
			(https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python/28014245)
	"""
	p = player_to_num(player)

	if (row_value != 1) and (p == math.sqrt(row_value)): 
		print (row_value, ": Winning row")
		return True
	else:
		print ("Not winning")
		return False

def add_check(player, location):
	p = player_to_num(player)
	t[location] = p

def win_row(player, row):
	p = player_to_num(player)
	for c in range(3):
		coord = solutions[row][c]
		print (coord)
		t[coord] = p
			
		
def player_to_num(player):
	""" Convert the player to number
	"""
	if player == "x": 
		p = 3 
	elif player == "y":
		p = 2
	else:
		p = 1 					## Just to capture bad programming. 				
	
	return p
	
def calc_values(t, solutions):
	"""
	"""
	row_value = 1
	c = 0
	for i in solutions:
		for j in range (3):
			z = i[j]
			row_value = row_value * t[z]
		
		if check_win("x", row_value):
			win_row("x", c)
		print (c, row_value)
		c += 1
		row_value = 1


	


print_grid()
calc_values(t, solutions)

print_grid()

## Prints the rows.
# for i in range (9):
	# m = i % 3
	# print(i, ":", m)
