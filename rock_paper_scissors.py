import random

def computer_variants():
    choices = ["Rock", "Paper", "Scissors"]

    return random.choice(choices)

player_variants = {
    1: "Paper",
    2: "Scissors",
    3: "Rock"
}

while True:
    ask = input("Do you want to play Paper, Scissors, Rock? (y/n): ")
    if ask.lower() != "y":
        break
    while True:
        computer_choice = computer_variants()
        while True:
            player_choice = input("Choose one of them: 1: Paper, 2: Scissors, 3: Rock: ")
            if player_choice.isdigit():
                player_choice = int(player_choice)
                if 1 <= player_choice <= 3:
                    break
                else:
                    print("\nChoose number from 1 to 3!")
            else:
                print("\nIncorrect! Choose the number from 1 to 3!")
        if computer_choice == player_variants[player_choice]:
            print(f"\nYou're both have {player_variants[player_choice]}")
        else:
            if computer_choice == "Rock":
                match player_choice:
                    case 1:
                        print(f"\nYou win! You have a {player_variants[player_choice]} and Computer has {computer_choice}\n")
                        break
                    case 2:
                        print(f"\nYou lose... You have a {player_variants[player_choice]} and Computer has {computer_choice}\n")
                        break
            elif computer_choice == "Paper":
                match player_choice:
                    case 2:
                        print(f"\nYou win! You have a {player_variants[player_choice]} and Computer has {computer_choice}\n")
                        break
                    case 3:
                        print(f"\nYou lose... You have a {player_variants[player_choice]} and Computer has {computer_choice}\n")
                        break
            elif computer_choice == "Scissors":
                match player_choice:
                    case 1:
                        print(f"\nYou lose... You have a {player_variants[player_choice]} and Computer has {computer_choice}\n")
                        break
                    case 3:
                        print(f"\nYou win! You have a {player_variants[player_choice]} and Computer has {computer_choice}\n")
                        break