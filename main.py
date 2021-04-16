
name1 = input("player1: please enter your name ")
name2 = input("player2: please enter your name ")
count = 10
player1 = 0
player2 = 0
while (count > 0):
    game1, game2 = input("Both players please enter your value: stone/paper/scissor  ").split()

    if (game1 == "stone"):
        if (game1 == game2):

            pass
        elif (game1 == "stone" and game2 == "paper"):

            player2 = player2 + 1
        else:

            player1 = player1 + 1
    elif (game1 == "paper"):
        if (game1 == game2):

            pass
        elif (game1 == "paper" and game2 == "scissor"):

            player2 = player2 + 1
        else:

            player1 = player1 + 1
    else:
        if (game1 == game2):

            pass
        elif (game1 == "scissor" and game2 == "stone"):

            player2 = player2 + 1
        else:

            player1 = player1 + 1
    count = count - 1
if (player1 > player2):
    print(name1, "wins")
elif (player1 < player2):
    print(name2, "wins")
else:
    print("It is a tie")

