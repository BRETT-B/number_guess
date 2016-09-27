import random
import subprocess

low = 1
high = 50
limit = 5

print("Guess a number between {} and {}".format(low, high))
print("You have {} guesses to get the correct number".format(limit))

number = random.randint(low, high)
current = 0

while current < limit:
	current += 1
	guess_number = int(input('What is your guess?'))
		
	if guess_number < number:
		print("Too Low")
	if guess_number > number:
		print("Too high")
	if guess_number == number:
		print("Awesome, you guessed the number {}\n It took you {} attempts".format(number, current))
		break

if current == limit and number != guess_number:
	print "Sorry, you\'re out of guesses. The number was {}".format(number)

play_again = str(raw_input("Would you like to try again? [Y/N]").upper())

if play_again == "Y":
	subprocess.call(['python', 'guessing_game.py'])
else:
	print "Thank you for playing"
