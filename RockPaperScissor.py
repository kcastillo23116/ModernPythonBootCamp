import random

computer_score = 0
player_score = 0
winning_score = 2
options = ["rock", "paper", "scissors"]

print(f"Best of {winning_score}!\n")

while player_score < winning_score and computer_score < winning_score:
	print(f"Player: {player_score}, Computer: {computer_score}")
	print("rock, paper, scissors...")
	player = input("enter player 1's choice: ").lower()
	computer = random.choice(options)
	print(f"Computer chose: {computer}")
	print("SHOOT!")


	if player == computer:
		print("Draw!\n")
	elif player == "rock" and computer == "scissors":
		print("Player Wins!\n")
		player_score += 1
	elif player == "paper" and computer == "rock":
		print("Player Wins!\n")
		player_score += 1
	elif player == "scissors" and computer == "paper":
		print("Player Wins!\n")
		player_score += 1
	else: 
		print("Computer Wins!\n")
		computer_score += 1

print(f"Player: {player_score}, Computer: {computer_score}")
