
def upper():
    count=0
    low=0
    t={}
    name=input('Enter the string')
    
    for i in range(len(name)):

        if name[i].isupper():
            count=count+1
        elif name[i].islower():
            low=low+1

    # print('Upper count',count)
    # print('Lower count',low)
    t={'Upper':count,'Lower':low}
    return t


