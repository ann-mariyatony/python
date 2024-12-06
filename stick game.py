'''
Author:Ann mariya tony
date:06-12-2024
'''
print("Welcome to stick game!")
print("Rules:")
print(" Their are 2 players in the game")
print(" Each player picks one set of sticks during his turn")
print(" A set contains 1, 2, or 3 sticks")
print(" The player who takes the last stick is the losser")
person1=input("Enter the name of player 1:")
person2=input("Enter the name of player 2:")
stick=16
while stick!=0:
    if stick!=0:
       print("Remaining stick",stick)
       choice=int(input(f"{person1}:The number of sticks player can take 1,2 or 3:"))
       stick=stick-choice
       player=person1
    if stick!=0:
       print( "remaining stick:",stick)
       choice = int(input(f"{person2} : The number of sticks player can take 1,2 or 3:"))
       stick=stick-choice
       player=person2
if stick==0:
            print(f"{player} is the loser.")

