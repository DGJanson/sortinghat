import logging
import sys

from .testdata import createTestData
from .exportdata import exportFile, importFile

logger = logging.getLogger("SortingHat - Testdata")

def showHelp ():
    print("""
        Generates a list of testdata

        Use the following flags (all optional):
        -h: show help
        -n: followed by int, length of list (default 16)
        -c: followed by int, number categories (default 4)
        -o: followed by filename, export list to this file as csv (default to print)
    """)

if __name__ == "__main__":
    # default options
    numberOfEntries = 16
    numberOfCats = 4
    outputFile = ""
    # parse input options
    ignoreNext = False
    for n in range(1, len(sys.argv)):
        input = sys.argv[n]
        if ignoreNext:
            ignoreNext = False
        else:
            if input == "-h":
                showHelp()
                sys.exit(0)
            elif input == "-n":
                try:
                    numberOfEntries = int(sys.argv[n + 1])
                    ignoreNext = True
                except Exception:
                    print("Error parsing -n input. Please check input or use help: -h flag")
            elif input == "-c":
                try:
                    numberOfCats = int(sys.argv[n + 1])
                    ignoreNext = True
                except Exception:
                    print("Error parsing -c input. Please check input or use help: -h flag")
            elif input == "-o":
                try:
                    outputFile = sys.argv[n + 1]
                    ignoreNext = True
                except Exception:
                    print("Error parsing -c input. Please check input or use help: -h flag")            
            elif input == "-i": # secret flag :) Use it to quickly test the input method
                try:
                    inputFile = sys.argv[n + 1]
                    print(importFile(inputFile))
                    sys.exit(0)                    
                except Exception:
                    print("Error parsing -i input. Please check input or use help: -h flag")            
            else:
                print("Unknown command. Please use -h flag for help")
                sys.exit(0)

            

    logging.basicConfig(level = logging.INFO)
    logger.info("Generating testdata with {} entries, {} categories.".format(numberOfEntries, numberOfCats))

    testData = createTestData(numberOfEntries, numberOfCats)
    if outputFile == "": # no output specified. Print to screen
        print(testData)
    else:
        logger.info("Writing output to {}".format(outputFile))
        exportFile(testData, outputFile)

