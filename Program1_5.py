# print * on screen number of times give by user

def Accept(iNo):
    iCnt = 0;
    for iCnt in range(iNo):
        print("*\t",end='');


if __name__ == "__main__":
    iValue = input("Enter the value:");

    Accept(int(iValue));

    