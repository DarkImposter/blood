import time
import random


# __init__

health = 10
attack = 3
running = True
death = False
prog = 0


#funk
def c():
    input('"Enter to continue"')
def dead(prog):
    running = False
    res = input('Well you died. Try again I guess?')
    if res == y or res == Yes or res == Y or res == yes:
        running = True

while running:
    if prog == 0:
        name = input('What is your Name?')
        quest = input('What is your quest?')
        color = input('What is your favorate color?')
        print('you are ready, warrior')
        c()
        print('wow! welcome! you are a bloodthirsty monster itching to kill anything you find. To look for something to satisfy your need, use "hunt" or "h". \n or, to check your stats, try "s" or "stats"')
        c()
        t1 = input('so! lets give it a try. \n what will it be? stats, or a fight?')
        prog += 1
