from random import randint

keepPlaying = "y"

while(keepPlaying != "n"):
	answer = randint(1, 11)
	correct = False

	while(correct != True):
		guess = input("Guess a number between 1 and 10: ")
		guess = int(guess)

		if guess < answer:
			print("Too low, try again!")
		elif guess > answer:
			print("Too high, try again!")
		else:
			print("You guessed it! You won!")
			correct = True
	keepPlaying = input("Do you want to keep playing? (y/n)")
print("Thanks for playing!")