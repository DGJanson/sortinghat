from multiprocessing.sharedctypes import Value
import random

def createTestData (numberEntries = 16, numberCategories = 4):
    """
    Create a list of entries. 
    Each entry is a tuple consisting of:
    - id
    - first choice (one of the categories)    
    - second choice (one of the categories, but not the first!)
    """
    # Check if numberCategories is not too low, since it will crash :)
    if numberCategories <= 1:
        raise ValueError("Number of Categories can not be 1 or less!")

    listDistribution = createListOfOptions(numberCategories)

    listToReturn = []
    for n in range(0, numberEntries):
        firstChoice = returnCategory(listDistribution)
        secondChoice = returnCategory(listDistribution, firstChoice) # exclude first choice
        listToReturn.append((n, firstChoice, secondChoice))
    
    return(listToReturn)
        

def returnCategory (listToChoose, otherOption = -1):
    """
    Return a random number from optionList till the max number categories (exclusive!)

    Args:
        listToChoose: A list of options to pick a category from
        otherOption: An option to exclude (the function can not return this value)
    """
    toReturn = random.choice(listToChoose)
    # we cannot do the same category twice, hence we check if they are not similar
    while toReturn == otherOption:
        toReturn = random.choice(listToChoose)

    return toReturn

def createListOfOptions (numberCategories):
    """
    Simply make a list with a random number of entries per category
    To make a different category distribution
    Like (0,0,0,0,1,1,2,3,3,3)
    """
    listToReturn = []
    for n in range(0, numberCategories):
        for i in range (0, random.randrange(1,5)):
            listToReturn.append(n)
    
    return listToReturn