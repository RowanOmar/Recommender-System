import math
from random import randint

import FileManager


#Manhatten Dist = |x1 - x2| + |y1 - y2|
def Calculate_ManhattanDistance(k, mode):

    if mode == 1:
        PersonsList = FileManager.ReadData(2)
        Mrx = PersonsList[len(PersonsList)-1]
        PersonsDistances = [[0 for i in range(2)] for j in range(len(PersonsList)-1)]

        for x in range(len(PersonsDistances)):
            for y in range(len(PersonsList[0])):

                AgeDist = abs((float(Mrx[3]) - float(PersonsList[x][3])))
                SalaryDist = abs((float(Mrx[4]) - float(PersonsList[x][4])))
                GenderMDist = abs((int(Mrx[5]) - int(PersonsList[x][5])))
                GenderFDist = abs((int(Mrx[6]) - int(PersonsList[x][6])))
                HasCreditY = abs((int(Mrx[7]) - int(PersonsList[x][7])))
                HasCreditN = abs((int(Mrx[8]) - int(PersonsList[x][8])))
                Distance = AgeDist + SalaryDist + GenderMDist + GenderFDist + HasCreditY + HasCreditN

            PersonsDistances[x][0] = PersonsList[x][2]
            PersonsDistances[x][1] = str(Distance)

        NearestDistances = FindMinDistance(PersonsDistances,k)
        return NearestDistances
    elif mode == 2:

        BooksRating = FileManager.ReadData(3)
        BooksRatingList = [[0 for i in range(6)] for j in range(len(BooksRating))]
        PredictedRatings = [[0 for i in range(2)] for j in range(len(BooksRating) - 1)]
        PredictedResult = 0
        Count1 = 0
        Count2 = 0
        Count3 = 0
        Count4 = 0
        Count5 = 0
        Rate = 0

        for b in range(0,len(BooksRating)):
            for c in range(0,len(BooksRating[0]),2):
                BooksRatingList[b][c/2] = BooksRating[b][c]

        Mrx = BooksRatingList[len(BooksRatingList)-1]

        for x in range(len(BooksRatingList)-1):
            for y in range(1,len(BooksRatingList[0])-1):
                PredictedResult += abs((int(Mrx[y]) - int(BooksRatingList[x][y])))

            PredictedRatings[x][0] = BooksRating[x][0]
            PredictedRatings[x][1] = PredictedResult
            PredictedResult = 0

        Nearest = FindMin(PredictedRatings, k)
        BooksActualRates = []

        for i in range(len(Nearest)):
            for j in range(len(BooksRating) - 1):
                if (Nearest[i][0] == BooksRating[j][0]):
                    BooksActualRates.append(BooksRating[j][10])

        if (k == 1):
            Rate = BooksActualRates[0]
        elif (k == 2):
            randomIndex = randint(0, 1)
            Rate = BooksActualRates[randomIndex]
        elif (k > 2):
            Count1 = BooksActualRates.count("1")
            Count2 = BooksActualRates.count("2")
            Count3 = BooksActualRates.count("3")
            Count4 = BooksActualRates.count("4")
            Count5 = BooksActualRates.count("5")
            if (Count1 > Count2 and Count1 > Count3 and Count1 > Count4 and Count1 > Count5):
                Rate = 1
            elif (Count2 > Count1 and Count2 > Count3 and Count2 > Count4 and Count2 > Count5):
                Rate = 2
            elif (Count3 > Count2 and Count3 > Count1 and Count3 > Count4 and Count3 > Count5):
                Rate = 3
            elif (Count4 > Count2 and Count4 > Count3 and Count4 > Count1 and Count4 > Count5):
                Rate = 4
            elif (Count5 > Count2 and Count5 > Count3 and Count5 > Count4 and Count5 > Count1):
                Rate = 5
            else:
                Rate = BooksActualRates[randint(0, len(BooksActualRates) - 1)]

        FileManager.UpdateRating(Rate)
        return Rate,Nearest


#Ecludien Dist = sqrt((x1 - x2)^2 + (y1 - y2)^2)
def Calculate_EcludienDistance(k, mode):

    if mode == 1:
        PersonsList = FileManager.ReadData(2)
        Mrx = PersonsList[len(PersonsList) - 1]
        PersonsDistances = [[0 for i in range(2)] for j in range(len(PersonsList) - 1)]

        for x in range(len(PersonsDistances)):
            for y in range(len(PersonsList[0])):

                AgeDist = pow((float(Mrx[3]) - float(PersonsList[x][3])),2)
                SalaryDist = pow((float(Mrx[4]) - float(PersonsList[x][4])),2)
                GenderMDist = pow((int(Mrx[5]) - int(PersonsList[x][5])),2)
                GenderFDist = pow((int(Mrx[6]) - int(PersonsList[x][6])),2)
                HasCreditY = pow((int(Mrx[7]) - int(PersonsList[x][7])),2)
                HasCreditN = pow((int(Mrx[8]) - int(PersonsList[x][8])),2)
                Distance = AgeDist + SalaryDist + GenderMDist + GenderFDist + HasCreditY + HasCreditN
                SqrDistance = math.sqrt(Distance)

            PersonsDistances[x][0] = PersonsList[x][2]
            PersonsDistances[x][1] = str(SqrDistance)

        NearestDistances = FindMinDistance(PersonsDistances,k)

        return NearestDistances
    elif mode == 2:

        BooksRating = FileManager.ReadData(3)
        BooksRatingList = [[0 for i in range(6)] for j in range(len(BooksRating))]
        PredictedRatings = [[0 for i in range(2)] for j in range(len(BooksRating) - 1)]
        PredictedResult = 0
        Count1 = 0
        Count2 = 0
        Count3 = 0
        Count4 = 0
        Count5 = 0
        Rate = 0

        for b in range(0,len(BooksRating)):
            for c in range(0,len(BooksRating[0]),2):
                BooksRatingList[b][c/2] = BooksRating[b][c]

        Mrx = BooksRatingList[len(BooksRatingList)-1]

        for x in range(len(BooksRatingList) - 1):
            for y in range(1, len(BooksRatingList[0]) - 1):
                PredictedResult += pow((int(Mrx[y]) - int(BooksRatingList[x][y])), 2)
                SqrDistance = math.sqrt(PredictedResult)

            PredictedRatings[x][0] = BooksRating[x][0]
            PredictedRatings[x][1] = SqrDistance
            PredictedResult = 0

        Nearest = FindMin(PredictedRatings, k)
        BooksActualRates = []

        for i in range(len(Nearest)):
            for j in range(len(BooksRating) - 1):
                if (Nearest[i][0] == BooksRating[j][0]):
                    BooksActualRates.append(BooksRating[j][10])

        if (k == 1):
            Rate = BooksActualRates[0]
        elif (k == 2):
            randomIndex = randint(0, 1)
            Rate = BooksActualRates[randomIndex]
        elif (k > 2):
            Count1 = BooksActualRates.count("1")
            Count2 = BooksActualRates.count("2")
            Count3 = BooksActualRates.count("3")
            Count4 = BooksActualRates.count("4")
            Count5 = BooksActualRates.count("5")
            if (Count1 > Count2 and Count1 > Count3 and Count1 > Count4 and Count1 > Count5):
                Rate = 1
            elif (Count2 > Count1 and Count2 > Count3 and Count2 > Count4 and Count2 > Count5):
                Rate = 2
            elif (Count3 > Count2 and Count3 > Count1 and Count3 > Count4 and Count3 > Count5):
                Rate = 3
            elif (Count4 > Count2 and Count4 > Count3 and Count4 > Count1 and Count4 > Count5):
                Rate = 4
            elif (Count5 > Count2 and Count5 > Count3 and Count5 > Count4 and Count5 > Count1):
                Rate = 5
            else:
                Rate = BooksActualRates[randint(0, len(BooksActualRates) - 1)]

        FileManager.UpdateRating(Rate)
        return Rate,Nearest


#Cousine Distance
def Calculate_CousineDistance(k, mode):

    if mode == 1:
        PersonsList = FileManager.ReadData(2)
        Mrx = PersonsList[len(PersonsList) - 1]
        PersonsDistances = [[0 for i in range(2)] for j in range(len(PersonsList) - 1)]

        for x in range(len(PersonsDistances)):
            for y in range(len(PersonsList[0])):

                AgeDist = (float(Mrx[3]) * float(PersonsList[x][3]))
                SalaryDist = (float(Mrx[4]) * float(PersonsList[x][4]))
                GenderMDist = (int(Mrx[5]) * int(PersonsList[x][5]))
                GenderFDist = (int(Mrx[6]) * int(PersonsList[x][6]))
                HasCreditY = (int(Mrx[7]) * int(PersonsList[x][7]))
                HasCreditN = (int(Mrx[8]) * int(PersonsList[x][8]))
                Distance1 = AgeDist + SalaryDist + GenderMDist + GenderFDist + HasCreditY + HasCreditN

                MrxDist = (pow(float(Mrx[3]),2) + pow(float(Mrx[4]),2) + pow(int(Mrx[5]),2) + pow(int(Mrx[6]),2) + pow(int(Mrx[7]),2) + pow(int(Mrx[8]),2))
                PersonDist = (pow(float(PersonsList[x][3]),2) + pow(float(PersonsList[x][4]),2) + pow(int(PersonsList[x][5]),2) + pow(int(PersonsList[x][6]),2) + pow(int(PersonsList[x][7]),2) + pow(int(PersonsList[x][8]),2))

                Distance2 = math.sqrt(MrxDist) * math.sqrt(PersonDist)
                FinalDistance = Distance1 / Distance2
            PersonsDistances[x][0] = PersonsList[x][2]
            PersonsDistances[x][1] = str(FinalDistance)

        NearestDistances = FindMaxDistance(PersonsDistances,k)

        return NearestDistances
    elif mode == 2:
        BooksRating = FileManager.ReadData(3)
        BooksRatingList = [[0 for i in range(6)] for j in range(len(BooksRating))]
        PredictedRatings = [[0 for i in range(2)] for j in range(len(BooksRating)-1)]
        PredictedResult = 0
        Count1 = 0
        Count2 = 0
        Count3 = 0
        Count4 = 0
        Count5 = 0
        Rate = 0

        for b in range(0, len(BooksRating)):
            for c in range(0, len(BooksRating[0]), 2):
                BooksRatingList[b][c / 2] = BooksRating[b][c]

        Mrx = BooksRatingList[len(BooksRatingList) - 1]

        for x in range(len(BooksRatingList) - 1):
            for y in range(1, len(BooksRatingList[0]) - 1):
                PredictedResult += (int(Mrx[y]) * int(BooksRatingList[x][y]))

                MrxDist = (pow(int(Mrx[1]), 2) + pow(int(Mrx[2]), 2) + pow(int(Mrx[3]), 2) + pow(int(Mrx[4]), 2))
                PersonDist = (pow(int(BooksRatingList[x][1]), 2) + pow(int(BooksRatingList[x][2]), 2) + pow(int(BooksRatingList[x][3]),2) + pow(int(BooksRatingList[x][4]), 2))

                Distance2 = math.sqrt(MrxDist) * math.sqrt(PersonDist)
                FinalDistance = PredictedResult / Distance2

            PredictedRatings[x][0] = BooksRating[x][0]
            PredictedRatings[x][1] = FinalDistance
            PredictedResult = 0
        Nearest = FindMax(PredictedRatings, k)
        BooksActualRates = []

        for i in range(len(Nearest)):
            for j in range(len(BooksRating)-1):
                if(Nearest[i][0] == BooksRating[j][0]):
                    BooksActualRates.append(BooksRating[j][10])

        if(k == 1):
            Rate = BooksActualRates[0]
        elif(k == 2):
            randomIndex = randint(0,1)
            Rate = BooksActualRates[randomIndex]
        elif(k > 2):
            Count1 = BooksActualRates.count("1")
            Count2 = BooksActualRates.count("2")
            Count3 = BooksActualRates.count("3")
            Count4 = BooksActualRates.count("4")
            Count5 = BooksActualRates.count("5")
            if(Count1 > Count2 and Count1 > Count3 and Count1 > Count4 and Count1 > Count5):
                Rate = 1
            elif(Count2 > Count1 and Count2 > Count3 and Count2 > Count4 and Count2 > Count5):
                Rate = 2
            elif(Count3 > Count2 and Count3 > Count1 and Count3 > Count4 and Count3 > Count5):
                Rate = 3
            elif(Count4 > Count2 and Count4 > Count3 and Count4 > Count1 and Count4 > Count5):
                Rate = 4
            elif(Count5 > Count2 and Count5 > Count3 and Count5 > Count4 and Count5 > Count1):
                Rate = 5
            else:
                Rate = BooksActualRates[randint(0,len(BooksActualRates)-1)]
        FileManager.UpdateRating(Rate)
        return Rate,Nearest


def FindMin(arrayOfDist, k):

    MinNumbersList = []

    # To get minimum numbers according to k
    for i in range(k):
        MinNum = min(arrayOfDist)
        MinNumbersList.append(MinNum)
        arrayOfDist.remove(MinNum)
    return MinNumbersList

def FindMinDistance(arrayOfDist, k):

    MinNumbersList = []
    Dist = []
    NearestPeople = []

    #To get all distances
    for j in range(len(arrayOfDist)):
        Dist.append(arrayOfDist[j][1])

    #To get minimum numbers according to k
    for i in range(k):
        MinNum = min(Dist)
        MinNumbersList.append(MinNum)
        Dist.remove(MinNum)

    for k in range(len(arrayOfDist)):
        for z in range(len(MinNumbersList)):
            if(arrayOfDist[k][1] == MinNumbersList[z]):
                NearestPeople.append(arrayOfDist[k])

    return NearestPeople

def FindMax(arrayOfDist,k):

    MaxNumbersList = []

    # To get minimum numbers according to k
    for i in range(k):
        MaxNum = max(arrayOfDist)
        MaxNumbersList.append(MaxNum)
        arrayOfDist.remove(MaxNum)

    return MaxNumbersList

def FindMaxDistance(arrayOfDist, k):

    MaxNumbersList = []
    Dist = []
    NearestPeople = []

    # To get all distances
    for j in range(len(arrayOfDist)):
        Dist.append(arrayOfDist[j][1])

    # To get minimum numbers according to k
    for i in range(k):
        MaxNum = max(Dist)
        MaxNumbersList.append(MaxNum)
        Dist.remove(MaxNum)

    for k in range(len(arrayOfDist)):
        for z in range(len(MaxNumbersList)):
            if (arrayOfDist[k][1] == MaxNumbersList[z]):
                NearestPeople.append(arrayOfDist[k])

    return NearestPeople


# print ('.......MANHATTAN DISTANCE.......')
# print(Calculate_ManhattanDistance(1,2))
#
# print ('.......ECLUDIEN DISTANCE.......')
# print(Calculate_EcludienDistance(1,2))
#
# print ('.......COUSINE DISTANCE.......')
# print(Calculate_CousineDistance(1,2))