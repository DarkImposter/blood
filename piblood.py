import time
import random


# __init__

health = 10
attack = 3
running = True
death = False
prog = 0

Loc = 'Nowhere, really.'


#funk
def c():
    input('"Enter to continue"')
def dead(prog):
    running = False
    res = input('Well you died. Try again I guess?')
    if res == y or res == Yes or res == Y or res == yes:
        running = True
def stat():
    print('your stats are:\ Health = '+str(health)+'\nLocation = '+Loc+'\nAttack = '+str(attack)+'\nLevel = '+str(prog))
def fight(prog):
    

while running:
    if prog == 0:
        prog += 1
        name = input('What is your Name?')
        quest = input('What is your quest?')
        color = input('What is your favorate color?')
        print('you are ready, warrior')
        c()
        print('wow! welcome! you are a bloodthirsty monster itching to kill anything you find. To look for something to satisfy your need, use "hunt" or "h". \n or, to check your stats, try "s" or "stats"')
        c()
        t1 = input('so! lets give it a try. \n what will it be? stats, or a fight?')
        if t1 == 'h' or 'hunt':
            print('you have gone on a wild hunt...')
        if t1 == 's' or 'stats':
            stat()
        print('you are ready, '+name+'time for your first adventure!')
    if prog == 1:
        msg = 'what would you like to do?'
    dat = input(msg)
    if dat == 'h' or 'hunt':
        fight(prog)
        
    
