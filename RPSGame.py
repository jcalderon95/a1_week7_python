from random import randint

# available weapons => store in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
print("Computer chooses: ", computer)

while player is False:
	print("Choose your weapon!\n")
	player = input("Rock, Paper or Scissors? \n")
	print("Player chooses", player)

	# check to see if you picked the same thing
	if (player == computer):
		print("Tie! Live to shoot another day")

	elif player == "Rock":
		if computer == "Paper":
			#computer won
			print("You loose", computer, "cuts", player)
		else:
			print("You win!", player, "smashes", computer)

	elif player == "Paper":
		if computer == "Scissors":
			print("You lose!", computer, "cuts", player)
		else:
			print("You Win", player, "covers", computer)

	elif player == "Scissors":
		if computer == "Rock":
			print("You Lose!", computer, "smashes", player)
		else:
			print("You win!", player, "cuts", computer)

	elif player == "Quit":
		exit()

	else:
		print("Not a valid option. Check again, and check your spelling!\n")

	player = False
	computer = choices[randint(0,2)]