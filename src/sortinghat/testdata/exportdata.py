# Stuff needed to export (and import) a dataset to csv

from xml.dom import ValidationErr


def exportFile (dataList, filename, sep = ";"):
    with open(filename, "w") as csvFile:
        for line in dataList:
            csvFile.write("{}{}{}{}{}\n".format(line[0], sep, line[1], sep, line[2]))

def importFile (filename, sep=";"):
    with open(filename, "r") as csvFile:
        listToReturn = []
        for line in csvFile:
            if line is not None and line != "":
                splitLine = line.strip().split(sep)
                if len(splitLine) != 3:
                    raise ValueError("Input can not be split in 3 parts. Cancelling.")
                else:
                    listToReturn.append((splitLine[0], splitLine[1], splitLine[2]))
        return listToReturn
