import random
import colorama
from colorama import Fore, Style
import pygame
colorama.init(autoreset=True)
import math

range = 100

Randnum = random.randint(1,(range))

print(f"\nRandomNumber is {Randnum} and the range is {range}.")

while True:
    answer = input("\ndo u wish to roll a randomnumber and guess? Y/N : ")
    if answer.upper() == "Y":
        Randnum = random.randint(1,(range))
        while True:
         guess = int(input(f"Guess what number it is between 1 and {range}: "))
         if guess > Randnum:
            print("Too high")
         elif guess < Randnum:
            print("Too low")
         else:
            print(f"{Fore.GREEN}CORRECT{Style.RESET_ALL}")
            print("\n Do u want to change the Range Y/N")
            change = input("").upper()
            if change == "Y":
                range = int(input("Change the range: "))
                break
            else:
                break
            
    else:
        break