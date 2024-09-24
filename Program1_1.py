def Devide(iNo1, iNo2):
    iAns = 0
    if(iNo2> iNo1):
        return -1
    iAns = iNo1/iNo2

    return iAns



if __name__ == "__main__":
    iValue1, iValue2 = 15, 5
    iRet = 0

    iRet = Devide(iValue1, iValue2)

    print("Division is ", iRet)
