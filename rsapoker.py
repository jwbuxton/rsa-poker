pairCategories = {"six-of-a-kind":10,
                  "five-of-a-kind":9,
                  "double threes-of-a-kind":8,
                  "four-two full house":7,
                  "four-of-a-kind":6,
                  "three pairs":5,
                  "three-two full house":4,
                  "three-of-a-kind":3,
                  "two pairs":2,
                  "one pair":1,
                  "high card":0}

def getVals(intRoll):
    """
    Converts an integer roll to its six components
    """
    roll = []
    for scale in range(6,0,-1):
        roll.append(intRoll % 10**scale // 10**(scale - 1) )
    return(roll)

def getSortedVals(rollVal):
    """
    Converts the six components of a roll to an ordered list of
    frequencies.  
    """
    bins = [0]*10
    for val in rollVal:
        bins[val] += 1
    return sorted(bins, reverse=True)

def getPairCategory(rollSorted):
    """
    Converts a roll's ordered list of frequencies to the pairwise hand
    category.  
    """
    if rollSorted[0] == 6:
        return "six-of-a-kind"
    elif rollSorted[0] == 5:
        return "five-of-a-kind"
    elif rollSorted[0] == 4 and rollSorted[1] == 2:
        return "four-two full house"
    elif rollSorted[0] == 4:
        return "four-of-a-kind"
    elif rollSorted[0] == 3 and rollSorted[1] == 3:
        return "double threes-of-a-kind"
    elif rollSorted[0] == 3 and rollSorted[1] == 2:
        return "three-two full house"
    elif rollSorted[0] == 3:
        return "three-of-a-kind"
    elif rollSorted[0] == 2 and rollSorted[1] == 2 \
         and rollSorted[2] == 2:
        return "three pairs"
    elif rollSorted[0] == 2 and rollSorted[1] == 2:
        return "two pairs"
    elif rollSorted[0] == 2:
        return "one pair"
    else:
        return "high card"

def processRolls():
    """
    Categorizes and prints all possible hands.  
    """
    processRollsUpTo(10**6)

def processRollsUpTo(n):
    """
    Categorizes and prints the first n hands.  
    """
    results = [0]*11
    for intRoll in range(n):
        valRoll = getVals(intRoll)
        sortRoll = getSortedVals(valRoll)
        roll = getPairCategory(sortRoll)
        results[pairCategories[roll]] += 1
    
    print('--Across {num:9,} hands--'.format(num=n))
    for hand in pairCategories:
        count = results[pairCategories[hand]]
        print('{h:24}:{c:8,}'.format(h=hand, c=count))


processRolls()
