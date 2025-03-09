import random

def game():
    print("You are playing a game")
    score = random.randint(1, 62)
    # fetch the hiscore
    with open("Hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your Score is: {score}")
    if (str(score)>str(hiscore)):
        # write it in hiscore file
         with open("Hiscore.txt", "w") as f:
               f.write(str(score))

    return score

game()