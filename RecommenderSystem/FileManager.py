personsFilename = "persons.txt"
normalizedDataFilename = "NormalizedData.txt"
booksFilename = "Books.txt"
booksRatingsFilename = "BooksRatings.txt"

def WriteData(Line, mode):
    if mode == 1:
        file = open(personsFilename, "a")
        file.write('\n'+Line)
        file.close()
    elif mode == 2:
        file = open(normalizedDataFilename, "a")
        file.write('\n' + Line)
        file.close()


def ReadData(mode):
    if mode == 1:
        file = open(personsFilename, "r")
        Persons_List = []
        for line in file:
            Persons_List.append(line.split())
        print("Persons: ", Persons_List)
        file.close()
        return Persons_List
    elif mode == 2:
        file = open(normalizedDataFilename, "r")
        Normalized_Persons_List = []
        for line in file:
            Normalized_Persons_List.append(line.split())
        print("Persons: ", Normalized_Persons_List)
        file.close()
        return Normalized_Persons_List
    elif mode == 3:
        file = open(booksRatingsFilename, "r")
        BooksRatings = []
        for line in file:
            BooksRatings.append(line.split())
        # print("Books Ratings: ", BooksRatings)
        file.close()
        return BooksRatings


def NormalizeData():
    DataToNormalize = ReadData(1)
    AgeArray = []
    SalaryArray = []
    j = 0

    for i in range(len(DataToNormalize)):
        AgeArray.append(int(DataToNormalize[j][3]))
        SalaryArray.append(int(DataToNormalize[j][4]))
        j = j + 1
    MaxAge = FindMax(AgeArray)
    MaxSalary = FindMax(SalaryArray)

    for x in range(len(DataToNormalize)):
        for y in range(len(DataToNormalize[0])):

            if y == 7:
                NormalizedLine = ""

            if y == 0:
                NormalizedLine = DataToNormalize[x][y]
            if y == 1:
                NormalizedLine += " "+ DataToNormalize[x][y]
            if y == 2:
                NormalizedLine += " " + DataToNormalize[x][y]
            if y == 3:
                NormalizedLine += " "+ str(float(DataToNormalize[x][y])/MaxAge)
            if y == 4:
                NormalizedLine += " "+ str(float(DataToNormalize[x][y])/MaxSalary)
            if y == 5:
                if DataToNormalize[x][y] == 'M':
                    NormalizedLine += " " + '1' + " "+ '0'
                elif DataToNormalize[x][y] == 'F':
                    NormalizedLine += " " + '0' + " " + '1'
            if y == 6:
                if DataToNormalize[x][y] == 'Y':
                    NormalizedLine += " " + '1' + " "+ '0'
                elif DataToNormalize[x][y] == 'N':
                    NormalizedLine += " " + '0' + " " + '1'
            y = y + 1

        WriteData(NormalizedLine, 2)

def FindMax(Numbers):

    MaxNumber= max(Numbers)
    return MaxNumber

def AddBook(Line):
    file = open(booksFilename, "a")
    file.write(Line + '\n' )
    file.close()

def AddRating(Line):
    RatingsFile = open(booksRatingsFilename, "r")

    found = False
    ToWrite = Line.split()

    with open(booksRatingsFilename, 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    for lineNumber,line in enumerate(RatingsFile):
        Temp = line.split()

        if(Temp[0] == ToWrite[0]):
            line = line.replace('\n'," "+ ToWrite[1] +" "+ ToWrite[2]+'\n')
            data[lineNumber] = line
            with open(booksRatingsFilename, 'w') as file:
                file.writelines(data)
            found = True
            break
    if(found == False):
        file = open(booksRatingsFilename, "a")
        file.write(Line + '\n')
        file.close()


def UpdateRating(Rate):

    RatingsFile = open(booksRatingsFilename, "r")

    with open(booksRatingsFilename, 'r') as file:
        # read a list of lines into data
        data = file.readlines()

    for lineNumber, line in enumerate(RatingsFile):
        Temp = line.split()
        lastLine = data[len(data)-1].split()
        if (Temp[0] == lastLine[0]):
            line = line.replace('0',str(Rate) + '\n')
            data[lineNumber] = line
            with open(booksRatingsFilename, 'w') as file:
                file.writelines(data)

def ReadBooks():
    file = open(booksFilename, "r")
    Books_List = []
    Books_List = file.readlines()
    newl = []
    for x in Books_List:
        newl.append(x.strip('\n'))

    print("Books: ",newl)
    file.close()
    return newl

def CheckLogin(username,password):
    persons=ReadData(1)

    for i in range(len(persons)):
        if username==persons[i][2] and password==persons[i][1]:
            return True
    return False

def write(data,filename):
    file = open(filename, "a")
    file.write(data+'\n')
    file.close()

def delete(filename):
    f = open(filename, 'r+')
    f.truncate()

def read(filename):
    file = open(filename, "r")
    List=file.readlines()
    newl=[]
    for x in List:
        newl.append(x.strip('\n'))

    print("name: ", newl)
    file.close()
    return newl





