# Divisible by 5

def Check(iNo):
    bAns = False;

    if(iNo%5 == 0):
        return True;
    else:
        return False;


if __name__ == "__main__":
    iValue = input("Enter Number");
    bRet = False;

    bRet = Check(int(iValue));
    if(bRet == True):
        print("Number is divisible by 5");
    else:
        print("Number is not divisible by 5");
    
    
    