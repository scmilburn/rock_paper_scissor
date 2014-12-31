import math
import time
import random

def set_num_games():

	""" 
	Predetermining number of games we want to play. 
	There should be an odd number of games to easily 
	determine a winner.
	"""
	
	done = False

	while not done:
		num_games = raw_input("How many games? (Odd number over 2) ")
		
		try:
			# str to int
			num_games = int(num_games)
		except:
			try:
				float(num_games)
				print "Please give an integer."
				continue
			except:
				print "Must be a number. Try again."
				continue
				
		if num_games >= 3 and num_games % 2 == 1:
			done = True
		else:
			print "Try again with a valid odd number."	
			
	num_to_win = int(math.ceil(num_games / 2.0))
	print "~ Best %s out of %s ~" % (num_to_win, num_games)
	return num_to_win, num_games
			
def countdown():
	print "\nRock"
	time.sleep(1)
	print "Paper"
	time.sleep(1)
	print "Scissors"
	time.sleep(1)
	print "SHOOT!\n"
	time.sleep(.3)

def game(num_to_win, num_games):
	comp_score = 0
	user_score = 0
	games_played = 0
		
	while games_played != num_games:
		choices = ['rock', 'paper', 'scissors']
		comp_ans = random.choice(choices);
		
		user_ans = raw_input("Rock, Paper, or Scissors? ")
		user_ans = user_ans.lower()
		
		countdown()
	
		if user_ans == comp_ans:
			print "It was a tie. Try again!"
			continue
		# ROCK
		elif user_ans == 'rock':
			if comp_ans == 'paper':
				print "Computer answered paper. You lose this round :("
				comp_score += 1
			elif comp_ans == 'scissors':
				print "Computer answered scissors. You win this round :D"
				user_score += 1
			games_played += 1
			
		# PAPER
		elif user_ans == 'paper':
			if comp_ans == 'scissors':
				print "Computer answered scissors. You lose this round :("
				comp_score += 1
			elif comp_ans == 'rock':
				print "Computer answered rock. You win this round :D"
				user_score += 1
			games_played += 1
			
		# SCISSORS
		elif user_ans == 'scissors':
			if comp_ans == 'rock':
				print "Computer answered rock. You lose this round :("
				comp_score += 1
			elif comp_ans == 'paper':
				print "Computer answered paper. You win this round :D"
				user_score += 1
			games_played += 1
		# INVALID
		else:
			print "Invalid option. Try again."
			continue
		
		# Check if already won
		if user_score == num_to_win:
			print "You WON! %s - %s" % (user_score, comp_score)
			break
			
		elif comp_score == num_to_win:
			print "You lost... %s - %s" % (user_score, comp_score)
			break
		else:
			print "Next round!"
			
answer = raw_input("Do you want to play Rock, Paper, Scissors? (yes/no) ");
if answer == "yes" or answer == 'y' or answer == "Yes":
	num_to_win, num_games = set_num_games()
	game(num_to_win, num_games)
elif answer == "no" or answer == 'n' or answer == "No":
	print "Bye..."