# substraction of two numbers

a = int(input('Enter how many numbers you want addition of: '))

ans = 0

for i in range(a):
    b = int(input(f'Enter number {i}: '))
    ans = b + ans

print('Addition of given numbers is: ', ans)