import logging
import sys

from .testdata.testdata import createTestData
from .testdata.exportdata import exportFile, importFile

from .sort import sortList

logger = logging.getLogger("Sortinghat")

def performSort(numberOfEntries, numberOfCats, inputFile, outputFile, singlePass):
    data = []
    if inputFile == "":
        logger.info("Generating test data file with {} entries and {} categories".format(numberOfEntries, numberOfCats))
        data = createTestData(numberOfEntries, numberOfCats)
    else:
        logger.info("Trying to import data from: {}".format(inputFile))
        try:
            data = importFile(inputFile)
        except Exception:
            logger.error("Error while trying to read data from import. Is the file location correct?")
            sys.exit(0)

    sortedList = sortList(data, singlePass)

    if outputFile == "":
        # print it, if not too long
        if len(sortedList) <= 1000:
            logger.info("Printing list to screen")
            for n in sortedList:
                print("{}\t{}\t{}".format(n[0], n[1], n[2]))
        else:
            logger.warning("List is too long to print. Better provide an outputfile with the -o option. Check -h for more info")
    else:
        logger.info("Trying to write output to {}".format(outputFile))
        try:
            exportFile(sortedList, outputFile)
            logger.info("Exported Data. Till we meet again!")
        except Exception:
            logger.error("Something whent wrong outputting the file. Is the location correct?")   

def showHelp():
    print("""
        Perform a category optimization

        Use the following flags (all optional):
        -h: show help
        -n: followed by int, length of list (default 16)
        -c: followed by int, number categories (default 4)
        -i: followed by filename, file to import and sort (this overrides creating a testfile with above settings)
        -o: followed by filename, export list to this file as csv (default to print)
        -s: flag for single pass (ie. not doing a divide a conquer but a single pass through the input). This is more efficient, but does NOT always work
    """)

if __name__ == "__main__":
    # parse stuff
    numberOfEntries = 16
    numberOfCats = 4
    outputFile = ""
    inputFile = ""
    singlePass = False
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
            elif input == "-i": 
                try:
                    inputFile = sys.argv[n + 1]
                    ignoreNext = True
                except Exception:
                    print("Error parsing -i input. Please check input or use help: -h flag")            
            elif input == "-s": 
                singlePass = True
            else:
                print("Unknown command. Please use -h flag for help")
                sys.exit(0)

    logging.basicConfig(level = logging.INFO)
    logger.info("Started sortinghat")
    performSort(numberOfEntries, numberOfCats, inputFile, outputFile, singlePass)