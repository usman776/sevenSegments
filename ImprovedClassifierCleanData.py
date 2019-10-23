import random

listOfLists = [[1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1],
                   [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1]]

def dataGenerator(dataRange):
    mainList = []
    key = []
    value = []
    for i in range(dataRange):
        randomIndex = random.randint(0, 9)
        key = listOfLists[randomIndex]
        value = [randomIndex]
        mainList.append(key)
        mainList.append(value)
    return mainList



def classifier(noisyData):
    listOfLists = [[1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 0, 0, 1],
                   [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 1]]
    correct = 0
    wrong = 0
    for index in range(0, len(noisyData), 2):
        noisyInstance = noisyData[index]
        classOfSegment = index + 1
        for i in range(len(listOfLists)):
            if noisyData[classOfSegment] == [i]:
                n = 0
                match = 0
                for j in noisyInstance:
                    if j == listOfLists[i][n]:
                        match = match + 1
                    n = n + 1
                break
        if match == 7:
            correct = correct + 1
        else:
            wrong = wrong + 1

    halfLength = len(noisyData) // 2
    accuracy = (correct / halfLength) * 100
    errorRate = (wrong / halfLength) * 100
    print("Accuracy of Classifer is ", str(accuracy) + " %")
    print("Error Rate of Classifier is ", str(errorRate) + " %")

if __name__ == '__main__':

    natureData = dataGenerator(100000)
    print("Length of Generated Data : " + str(len(natureData) // 2))
    classifier(natureData)
