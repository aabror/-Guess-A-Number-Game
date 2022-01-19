# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 23:02:54 2022

@author: Abror 
"""

import random

def find_number(x=10):
    r_number = random.randint(1, x)
    print(f"I am thinking a number between 1 and {x}. Can you find the number?")    
    guesses = 0
    while True:
        guesses += 1
        guess = int(input(">>>"))
        if guess < r_number:
            print("Wrong. Enter a bigger number: ")
        elif guess > r_number:
            print("Wrong. Enter a smaller number: ")
        else:
            print(f"Congrats. You found the number with {guesses} guesses !")
            break
    return guesses 
    # print(f"Congrats. You found the number with {guesses} guesses !")


def find_number_pc(x=10):
    input(f"Think a number between 1 and {x}." 
          f" Press 'Enter' when you are ready. I will try to find it!")
    low = 1
    high = x
    guesses = 0
    while True:
        guesses +=1 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        answer = input(f'You are thinking the number {guess}:'
        f" If correct, enter (T), if it is bigger,"
        f"enter (+), if it is smaller, enter (-) ".lower())
        
        if answer == '-':
            high = guess - 1
        elif answer == '+':
            low = guess + 1
        else:
            break
    print(f"I found it with {guesses} guesses !")
    return guesses



         
def play(x=10):
    again = True
    while True:
        guesses_user = find_number(x)
        guesses_pc = find_number_pc(x)
        if guesses_user > guesses_pc:
            print("I have won!")
        elif guesses_user < guesses_pc:
            print("You have won")
        else:
            print("Draw!")
        again = int(input("Do you want to play again? yes(1)/no(0):"))
        if again == 0:
            break
# play()