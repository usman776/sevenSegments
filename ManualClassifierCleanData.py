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
        key = [listOfLists[randomIndex]]
        value = [randomIndex]
        mainList.append(key)
        mainList.append(value)
    return mainList


def classifier(natureData):
    correct = 0
    wrong = 0
    for index in range(0, len(natureData), 2):
        for i in natureData[index]:
            classOfSegment = index + 1
            flag = False
            indexOfGroundTruth = 0
            while indexOfGroundTruth < 10:
                if (i == listOfLists[indexOfGroundTruth]):
                    if natureData[classOfSegment].pop() == indexOfGroundTruth:
                        correct = correct + 1
                        flag = True
                        break
                indexOfGroundTruth = indexOfGroundTruth + 1
            if flag == False:
                wrong = wrong + 1
    halfLength = len(natureData) // 2
    accuracy = (correct / halfLength) * 100
    errorRate = (wrong / halfLength) * 100
    print("Accuracy of Classifer is ", str(accuracy) + " %")
    print("Error Rate of Classifier is ", str(errorRate) + " %")


if __name__ == '__main__':

    natureData = dataGenerator(1000)
    print("Length of Generated Data : " + str(len(natureData) // 2))
    classifier(natureData)
