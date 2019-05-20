import sys
import pandas as pd

def ToList(FileName):
    df = pd.read_excel(FileName)
    PhoneList = df['SO DT'].values.tolist()
    return PhoneList

def ToFile(PhoneList):
    with open("PhoneNumber.txt","w",encoding="utf-8") as TextFile:
        for PhoneNumber in PhoneList:
            TextFile.write(str(PhoneNumber) + "\n")

def IsInt(char):
    try: 
        int(char)
        return True
    except ValueError:
        return False

def Delete(PhoneList):
    PhoneNumber = []
    for Phone in PhoneList:
        PhoneArray = list(str(Phone))
        x = 0
        while x < len(PhoneArray):
            if IsInt(PhoneArray[x]) == False and PhoneArray[x] != '-':
                PhoneArray.remove(PhoneArray[x])
                x += -1
            x += 1
        PhoneNumber.append(''.join(PhoneArray))
    return PhoneNumber

def Mode(Mode, PhoneList):
    PhoneNumber = []
    # Mode = list(str(Mode))
    for Phone in PhoneList:
        ChangedNumber = []
        PhoneArray = Phone.split('-')
        for Number in PhoneArray:
            if len(Number) >= (len(Mode)-1):
                Number = Number.replace(Number[:(len(Mode)-1)],Mode[-(len(Mode)-1):],1)
            ChangedNumber.append(Number+'-')
        ChangedNumber = ''.join(ChangedNumber)
        ChangedNumber = ChangedNumber[:-1]
        PhoneNumber.append(ChangedNumber)
    return PhoneNumber


def main():
    PhoneList = ToList(sys.argv[1])
    PhoneList = Delete(PhoneList)
    PhoneList = Mode(sys.argv[2],PhoneList)
    ToFile(PhoneList)
    
if __name__ == '__main__':
    main()