# 7️⃣ Print the Fibonacci series up to N terms.

n_number = int(input("Enter the number up to you want the fibonacci series: "))

start_num_one, start_num_two = 0, 1

for i in range(n_number):
    print(start_num_one)
    # start_num_one, start_num_two = start_num_two, start_num_two + start_num_one
    next_number = start_num_one + start_num_two
    start_num_one = start_num_two
    start_num_two = next_number
