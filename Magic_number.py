#Project for High School ladies in Ashanti Region Kumasi, to help them develope
#interest in Techonology and it related sciences , engineering & mathematics).
#This code would be furhter developed to a more complex model.

# A GAME PROJECT - MAGIC NUMBER (GUESS RIGHT)
import random
robot_guess = random.randint(1, 15)
game_message =''' Hello I am a Robot, and I want you to challenge me in GAME.
Let start, YOU WIN if you GUESS the RIGHT number I am holding, Good Luck!'''

print("Your guess should be between 1 and 15")

print(game_message)
print("********************************************")
print()
player1 = input("Enter Number : ")
number_of_chances = int(3)
player_guess = int(player1)


def chance(number_of_chances):
        if number_of_chances == 1:
            print("I WON !!, GAME OVER press 1 to play again")
            print("My GUESS was %s" % robot_guess)

def guess(number_of_chances, robot_guess, player_guess):
    while(number_of_chances > 1):
        if (robot_guess==player_guess):
            print("You WON!!!me, Weldone")
            break
        elif( player_guess < robot_guess):
            print("Your guess is LOWER than my GUESS")
            number_of_chances = number_of_chances - 1
            print()
            player1 = input("Try Again: ")
            player_guess = int(player1)
            chance(number_of_chances)

            
        elif(player_guess > robot_guess):
            print("Your guess is  HIGHER, than my GUESS")
            number_of_chances = number_of_chances - 1
            print()
            player1 = input("Try Again: ")
            player_guess = int(player1)
            chance(number_of_chances)
            
        else:
            print('''I WON !!, GAME OVER press 1 to play again''')
            print("My GUESS was %s" % robot_guess)


guess(number_of_chances, robot_guess, player_guess)


        
