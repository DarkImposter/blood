
import time
import sys
import random
import pdb
prog = 1
start = input('Have you played before? (Y/N)')
if start.lower() == 'y':
    prog = 1
elif start.lower() == 'n':
    prog = 0
else :
    print('Nope')

health = 10
attackLow = 3
eq = []
attackHi = 5
running = True
move = 'you reach out and punch the '
death = False
Mhealth = 5
Mattack = 5
spec = ''
ondeath = ''
Loc = 'Nowhere, really.'
forest = 'A deep and scary forest'
desert = 'hot and sandy dessert'
water = 'dark underwater depths'
list = []
locations = [forest,desert,water]
class Mob():
    def __init__(self, name, health, attackL,attackHi, spec, ondeath, lvl):
        self.name = name
        self.health = health
        self.attackL = attackL
        self.attackHi = attackHi
        self.spec = spec
        self.ondeath = ondeath
        self.lvl = lvl
class wepon():
    def __init__(self, name, bonus, location, spec):
        self.name = name
        self.bonus = bonus
        self.location = location
        self.spec = spec
class arm():
    def __init__(self, name, bonus, location, type):
        self.name = name
        self.bonus = bonus
        self.location = location
        self.type = type



#forest mobs
bear = Mob( 'Bear', 15, 3,5,  'it claws at your eyes', 'it ties you to a post and scraches its back against you', 4)
wastedBugs = Mob( 'Wasted Bugs', 5, 4,6,'They inject you with an unknown substance', 'the bugs sting, bite, and scratch you until you are unrecongnizably dead', 3)
wolf = Mob('Wolf', 7, 4,6, 'the wolf lunges foreward and bites into you', 'the wolf calls its friends and they rip you up together', 3)
#rabid sloth
#bat
#wasted bugs
fMobs = [bear, wastedBugs, wolf]
shit = []
# forst items
twigSword = wepon('Twig Sword', 3, forest, 'You pull out yor sword and slash the ')
largeStick = wepon('Large Stick', 1,  forest, 'you take your stick and smack the ')

twigShield = arm('Twig Shield', 3,  forest, 'hand')
leafVest = arm('Leaf Vest', 2,  forest, 'chest')

fItems = [twigSword, largeStick, twigShield, leafVest]
#waterMobs
eel = Mob( 'Eel', 5, 4, 6, 'The eel zapps you with its tail', 'The eel strangles you with its body and continuosly zapps you to death', 4)
shark = Mob('Shark', 15, 5,8,  'the shark bites you fircely', 'the shark clamps on and shakes you so hard you fall apart', 5)
fish = Mob('Fish', 3, 3,5, 'the fish swimms up and splashes you', 'the fish trandforms into a monster and devouers you', 1)
wMobs = [eel, shark]
#wateritems self, name, bonus, mob, location, spec
fishboneSword = wepon('Fish Bone Sword', 3,  water, 'you  pull out your floppy sword and swat the')
wItems = [fishboneSword]
#desertMobs
snake = Mob('Snake', 3, 3, 5, 'it slithers up and bites you in the ass', 'the snake unhinges its jaw and swallows you whole.', 3)
cactus = Mob( 'Cactus', 20, 1, 3, 'as you move to attack, a little thorn pricks your arm', 'the cactus lets you body decompose to feed its roots', 3)

dMobs = [snake, cactus]

bagOfSand = wepon('Bag of Sand', 5,  desert, 'you reach in and pull out a handfull of sand and throw it at the' )
dItems = [bagOfSand]
#funk

def tut():
    name = input('What is your Name?')
    quest = input('What is your quest?')
    color = input('What is your favorate color?')
    print('you are ready, warrior')
    c()
    print('wow! welcome! you are a bloodthirsty monster itching to kill anything you find. To look for something to satisfy your need, use "hunt" or "h". \n or, to check your stats, try "s" or "stats"')
    c()
    t1 = input('so! lets give it a try. \n what will it be? stats, or a fight?')
    if t1 == 'h' or t1 == 'hunt':
        print('you have gone on a wild hunt...')
    if t1 == 's' or t1 ==  'stats':
        stat()
    print('you are ready, '+name+'time for your first adventure!')
def pick(L):
    ret = L[random.randint(0, len(L) - 1)]
    return ret
def c():
    input('"Enter to continue"')
def dead(prog):
    running = False
    res = input('Well you died. Try again I guess?')
    if res == 'y' or res == 'Yes' or res == 'Y' or res == 'yes':
        running = True
    if res == None:
        sys.exit(1)
# def stat():
#     print('your stats are:\nHealth = '+str(health)+'\nLocation = '+Loc+'\nAttack = '+str(attackL)', to '+str(attackHi)+'\nLevel = '+str(prog))



def iStat(i):
    val = 'Attack Bonus: '+str(i.bonus)+'.'
    return val



def inventory():
    if shit != None:
        inInv = True
    for i in shit:
        print('you have a '+str(i.name)+' with the stats of '+iStat(i))
    for i in eq:
        print('you have equiped a '+str(i.name)+' with the stats of '+iStat(i))
    while inInv:
        chose = input('what would you like to equip? (one of your items or nothing)')
        if chose == 'nothing':
            inInv = False
        for i in shit:
            if chose.lower() == i.name.lower():
                eq.append(i)
                shit.remove(i)
                print('you have equiped a '+str(i.name)+' with the stats of '+iStat(i))
                if len(shit) == 0:
                    inInv = False











def setLocation():
    Loc = locations[random.randint(0, len(locations) - 1)]
    return Loc

def setMob(Loc):
    print('you have entered the '+Loc)
    if Loc == 'A deep and scary forest':
        list = fMobs
    if Loc == 'hot and sandy dessert':
        list = dMobs
    if Loc == 'dark underwater depths':
        list = wMobs
    return pick(list)


def pickfit(Loc):
    fit = setMob(Loc)
    return fit

def setDrop(Loc):
    if Loc == 'A deep and scary forest':
        drop = fItems
    if Loc == 'hot and sandy dessert':
        drop = dItems
    if Loc == 'dark underwater depths':
        drop = wItems
    return pick(drop)


def checkFight():
    ag = input('do you want to attack or try to run?(A/R)')
    if ag.lower() == 'a':
        return True
    elif ag.lower() == 'r':
        print('your chances of running are 1 out of '+str(fit.lvl))
        chance = random.randint(1,fit.lvl)
        if chance == 1:
            return False
        else:
            return True
    else:
        print('No')
        return checkFight()

def youAttack(fit):
    atm = random.randint(attackLow, attackHi)
    print(move +fit.name+' and deal '+str(atm)+' damage')
    fit.health -= atm

def getDrop(Loc):
    drops = setDrop(Loc)
    print('you found a '+drops.name+' !')
    shit.append(drops)

def theyAttack(fit):
    turnDam = random.randint(fit.attackL, fit.attackHi)
    print(fit.spec + ' and deals '+ str(turnDam)+ ' damage')
    global health
    health -= turnDam

def fight(prog):
    Loc = setLocation()
    fit = pickfit(Loc)
    print('you have encountered: '+fit.name)
    if checkFight():
        combat = True
    lup = 1
    while combat:
        if lup == 1:
            lup += 1
            print('you have enterd combat with '+fit.name)
        health = 10
        if len(eq) != 0:
            for l in eq:
                attackHi += l.bonus
        c()
        youAttack(fit)
        c()
        theyAttack(fit)
        if health <= 0:
            death = True
            combat = False
            dead(prog)
        if fit.health <= 0:
            combat = False
            print('you win!')
            getDrop(Loc)
            prog += 1



while running:
    if prog == 0:
        tut()
        prog += 1

    if prog == 1:
        msg = 'what would you like to do?'

    dat = input(msg)
    if dat == None:
        print('well come on now.')
    if dat == 'h' or dat ==  'hunt':
        fight(prog)
    if dat == 's' or dat == 'stats':
        stat()
    if dat == 'i' or dat == 'inventory':
        inventory()
