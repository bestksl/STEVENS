# Haoxuan Li
# Student ID: 10434197
import random

# all possibilities
rules = {('scissor', 'rock'): "lose", ('scissor', "paper"): "win", ('paper', "rock"): "win",
         ('paper', "paper"): "lose", ('rock', "scissor"): "win",
         ('rock', "paper"): "lose", ('rock', "rock"): "tie", ('paper', "paper"): "tie", ('scissor', "scissor"): "tie"}
choice = ('scissor', 'rock', "paper")


# this is main()
def main():
    try:
        start()
    except:
        print('something wrong')
        main()


# logic part
def start():
    your_choice = input("please chose your chioce, Press r for exit")
    if your_choice == "r":
        print("thank you")
        exec
    elif your_choice not in {'scissor', 'paper', 'rock'}:
        print('unexpected parameter')
        start()
    else:
        com_choice = choice[random.randint(0, 2)]
        print("computer choice :" + com_choice)
        temp = True
        for rule in rules:
            if (your_choice, com_choice) == rule:
                print("you  " + rules.get(rule))
        start()


main()
