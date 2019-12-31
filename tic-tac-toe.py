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
t = [3, 1, 1, 1, 3, 1, 1, 1, 3]

x = 3
o = 2
b = 1			# Blank = 1

def print_grid():
	s = ""						## String that will contain the view.
	c = 0						## Used for figuring out the row.
	for item in t:
		s = s + str(item) + " "
		c += 1
		if (c%3 == 0): s = s + ("\n") 		## If the last column num is divisible by 3, put it on a new row.
	print (s)

def check_win(player, t):
	"""	Player: x or y
		t: The stored values of the playing board. 
		p**(1./3.) is finding the cubed root of a value. 	
			(https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python/28014245)
	"""
	p = player_to_num(player)
		
	cv = calc_values(t)			## Get the calculated values
	
	c = 0						## Counter
	for item in cv: 
		if (item != 1) and (p == math.sqrt(item)): 
			print (c, item, ": Winning row")
			win_row(player, c)
		else: 
			print (c, item)
			c += 1				## Increment counter

def add_check(player, location):
	p = player_to_num(player)
	t[location] = p

def win_row(player, row):
	p = player_to_num(player)
	if row == 0: 
		t[0]=t[1]=t[2] = p
	if row == 1: 
		t[3]=t[4]=t[5] = p
	if row == 2: 
		t[6]=t[7]=t[8] = p
	if row == 3: 
		t[0]=t[3]=t[6] = p	
	if row == 4: 
		t[1]=t[4]=t[7] = p
	if row == 5: 
		t[2]=t[5]=t[8] = p
	if row == 6: 
		t[2]=t[4]=t[6] = p
	if row == 7: 
		t[0]=t[14]=t[8] = p					
		
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
	
def calc_values(t):
	""" Ways to measure winning. 
			First 3: by rows
			Next 3:	 by columns
			Final 2: by diagonals
	"""
	calc = []
	calc.append(t[0] * t[1] * t[2])
	calc.append(t[3] * t[4] * t[5])
	calc.append(t[6] * t[7] * t[8])
	calc.append(t[0] * t[3] * t[6])
	calc.append(t[1] * t[4] * t[7])
	calc.append(t[2] * t[5] * t[8])
	calc.append(t[2] * t[4] * t[6])
	calc.append(t[0] * t[4] * t[8])
	
	return calc
	
print_grid()
check_win("x", t)
print_grid()

