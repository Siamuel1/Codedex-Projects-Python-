#Bonus: Rock Paper Scissors Lizard Spock
# A simple game of rock-paper-scissors against a computer.
'''
1) Rock > 3) Scissors
2) Paper > 1) Rock
3) Scissors > 2) Paper
1) Rock > 4) Lizard
2) Paper > 5) Spock 
3) Scissors > 4) Lizard
4) Lizard > 5) Spock
4) Lizard > 2) Paper
5) Spock > 1) Rock 
5) Spock > 3) Scissors
 '''
import random

choices = ['rock ✊', 'paper ✋', 'scissors ✌️', 'lizards 🦎', 'spock 🖖']
print("===================\nRock Paper Scissors\n===================")

computer = random.randint(1, 5)
player = int(input("\n1) Rock ✊\n2) Paper ✋\n3) Scissors ✌️\n4) Lizards 🦎\n5) Spock 🖖\n\nPick a number: "))

# 1. Print choices once at start so we don't repeat it in every if/elif statement 
# Using player-1 because list 'choices' start at index 0
print(f"\nYou chose: {choices[player-1]}")
print(f"CPU chose: {choices[computer-1]}")

# Tie
if player == computer:
    print("It's a tie!")

# 2. Check all options for each {player} [choices]
# 1) Rock > 3) Scissors & 1) Rock > 4) Lizard
elif (player == 1 and (computer == 3 or computer == 4)):
    print("The player won!")
    
# 2) Paper > 1) Rock & 2) Paper > 5) Spock 
elif (player == 2 and (computer == 1 or computer == 5)):
    print("The player won!")

# 3) Scissors > 2) Paper & 3) Scissors > 4) Lizard
elif (player == 3 and (computer == 2 or computer == 4)):
    print("The player won!")

# 4) Lizard > 5) Spock & 4) Lizard > 2) Paper
elif (player == 4 and (computer == 5 or computer == 2)):
    print("The player won!")

# 5) Spock > 1) Rock & 5) Spock > 3) Scissors
elif (player == 5 and (computer == 3 or computer == 1)):
    print("The player won!")

else: 
    print("The CPU won!")