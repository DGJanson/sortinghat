# this file contains the methods we need for sorting. hurray
# it is not sorting really. But it is the thought that counts

# the main input is a list, which gets passed around with an index range to use

import logging

logger = logging.getLogger("Sortinghat")

def sortList(listToSort):
    """
    Change the list so that the number are categories are divided 
        as equally as possible between column 2 and column 3
    
    The first column contains the id and is completely ignored.
    The list is changed in place by a divide and conquer approach
    """
    logger.info("Score before algorithm: {}".format(calcScore(listToSort, 0, len(listToSort))))

    nrPerIt = 2 # the number of entries to optimize by iteration. Start low and "merge" upwards to bigger and bigger chunks

    while nrPerIt < len(listToSort):
        index = 0
        while (index + nrPerIt) < len(listToSort):
            optimizeLocally(listToSort, index, index + nrPerIt)
            index = index + nrPerIt
        optimizeLocally(listToSort, index, len(listToSort))
        nrPerIt = nrPerIt * 2
    
    optimizeLocally(listToSort, 0, len(listToSort))
    
    logger.info("Score after algorithm: {}".format(calcScore(listToSort, 0, len(listToSort))))

    return(listToSort)

def optimizeLocally(slice, start, stop):
    """
    This is where the work happens
    Calculate a score and go through each of the entries to check if flipping the cat columns would improve the score
    """
    if len(slice) <= 1:
        return
    
    score = calcScore(slice, start, stop)

    for n in range(start, stop):
        # copy the dict.TODO can we optimize this
        newScore = dict(score)
        newScore[slice[n][1]] = newScore[slice[n][1]] - 2 # a flip removes and adds, so double the score
        newScore[slice[n][2]] = newScore[slice[n][2]] + 2 # a flip removes and adds, so double the score
        if (calcAbsScore(newScore) < calcAbsScore(score)):
            score = newScore
            slice[n] = (slice[n][0], slice[n][2],slice[n][1]) # replace with flipped values

def calcScore(slice, start, stop):
    """
    Score is calced as follows:
    For each category an entry in the first / left column increases the score
    An entry in the second /right column decreases the score
    The scores should be as close to zero as possible
    The ABSOLUTE sum of the score can be used as heuristic for a score for the entire slice
    """
    score = {}
    for n in range(start, stop):
        if slice[n][1] in score:
            score[slice[n][1]] = score[slice[n][1]] + 1
        else:
            score[slice[n][1]] = 1
        
        if slice[n][2] in score:
            score[slice[n][2]] = score[slice[n][2]] - 1
        else:
            score[slice[n][2]] = -1

    return score
    
def calcAbsScore (score):
    """
    Calculate the absolute score
    This is needed to allow for flipping a balanced category with odd number of entries:
    this changes score from 1 to -1 (or vice versa) and hence should be "free"
    """
    sum = 0
    for key in score:
        sum = sum + abs(score[key])
    return sum