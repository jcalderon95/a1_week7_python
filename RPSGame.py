from random import randint

# available weapons => store in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choice in the terminal window
print("Computer chooses: ", computer)

# Lives
computer_lives = 3
player_lives = 3


while player is False:
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors? \n")
    print("Player chooses", player)

    # check to see if you picked the same thing
    if (player == computer):
        computer_lives = computer_lives
        player_lives = player_lives
        print("Tie! Live to shoot another day")
        print("Your Lives", player_lives, "Computer Lives", computer_lives)

    elif player == "Rock":
        if computer == "Paper":
            # computer won
            player_lives = player_lives - 1
            print("You loose", computer, "cuts", player)
            print("Your Lives", player_lives, "Computer Lives", computer_lives)
        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "smashes", computer)
            print("Your Lives", player_lives, "Computer Lives", computer_lives)

    elif player == "Paper":
        if computer == "Scissors":
            player_lives = player_lives - 1
            print("You lose!", computer, "cuts", player)
            print("Your Lives", player_lives, "Computer Lives", computer_lives)
        else:
            computer_lives = computer_lives - 1
            print("You Win", player, "covers", computer)
            print("Your Lives", player_lives, "Computer Lives", computer_lives)

    elif player == "Scissors":
        if computer == "Rock":
            player_lives = player_lives - 1
            print("You Lose!", computer, "smashes", player)
            print("Your Lives", player_lives, "Computer Lives", computer_lives)
        else:
            computer_lives = computer_lives - 1
            print("You win!", player, "cuts", computer)
            print("Your Lives", player_lives, "Computer Lives", computer_lives)

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    player = False
    computer = choices[randint(0, 2)]
