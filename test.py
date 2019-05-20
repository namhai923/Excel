def Mode(Mode, PhoneList):
    PhoneNumber = []
    # Mode = list(str(Mode))
    for Phone in PhoneList:
        ChangedNumber = []
        PhoneArray = Phone.split('-')
        for Number in PhoneArray:
            if len(Number) >= (len(Mode)-1):
                Number = Number.replace(Number[:(len(Mode)-1)],Mode[-(len(Mode)-1):],1)
            ChangedNumber.append(''.join(Number)+'-')
        ChangedNumber = ''.join(ChangedNumber)
        ChangedNumber = ChangedNumber[:-1]
        PhoneNumber.append(ChangedNumber)
    return PhoneNumber


PhoneList = ['0846559866','64946163165-61511944','3618462161561-36611616161611','622926994-616113161-6161361619']
print(Mode('+84',PhoneList))
x = "hahahuhuhihi"
print(x[:-3])