def Display(iNo):
    iCnt = 0;
    if(iNo < 10):
        print("Less")
    else:
        print("High")


if __name__ == "__main__":
    iValue = int(input("Enter a number"))
    Display(iValue)
