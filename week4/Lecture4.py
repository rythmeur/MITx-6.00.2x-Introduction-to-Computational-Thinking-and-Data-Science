__author__ = 'Intel'
import random

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

def checkPascal(numTrials, roll):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = roll()
            d2 = roll()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print 'Probability of losing =', 1.0 - yes/numTrials

##checkPascal(10000, rollDie)

















def rollLoadedDie():
    if random.random() < 1.0/5.5:
        return 6
    else:
        return random.choice([1,2,3,4,5])

##checkPascal(10000, rollLoadedDie)
















def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)

for i in range(5): #number of trials
    print flip(10)


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    event_occured=0.
    for i in range(numTrials):
        bucket = ["g","g","g","r","r","r"]
        random.shuffle(bucket)
        first=bucket.pop()
        second=bucket.pop()
        third=bucket.pop()
        if first==second==third:
            event_occured+=1.
    return event_occured/numTrials

print noReplacementSimulation(100)