def Display(iNo):
    iCnt = 0;
    if(iNo < 0):
        iNo = -iNo;
    while(iCnt < iNo):
        print(" * ",end='')
        iCnt +=1


if __name__ == "__main__":
    iValue = int(input("Enter a number"))
    Display(iValue)
