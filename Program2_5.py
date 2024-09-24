def Display(iNo1, iNo2):
    iCnt = 0;
    if(iNo1 < 0) and (iNo2 < 0):
        iNo1 = -iNo1;
        iNo2 = -iNo2;
    while(iCnt < iNo2):
        print(iNo1,end=' ')
        iCnt+=1


if __name__ == "__main__":
    iValue1 = int(input("Enter a number"))
    iValue2 = int(input("Enter the frequency"))
    Display(iValue1, iValue2)
