# 2️⃣ Create a function that takes a list of numbers and returns their average.

def average(ls):
    total = 0
    for i in ls:
        total += i
    avg = total/len(emp_ls)
    return avg


emp_ls = []
num = int(input("Enter how many numbers you want in list: "))
print("Enter the numbers:")
for i in range(num):
    var = int(input())
    emp_ls.append(var)

print(emp_ls)
print("The average of given numbers is: ", average(emp_ls))
