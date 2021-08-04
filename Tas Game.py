import random
from time import sleep
import colorama
from colorama import Fore, Back, Style

while True:
    num = random.randint(1, 6)
    print(Fore.MAGENTA + 'Number Tas:', num)
    if num == 6:
        num = random.randint(1, 6)
        print(Fore.GREEN + 'Award user:', num)
        sleep(2)
    
    else:
        choice = input(Fore.YELLOW + 'try again? y/n= ')
        if choice == 'n':
            print('by!')
            break
