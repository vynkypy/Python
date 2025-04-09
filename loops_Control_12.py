# 3️⃣ Use pass inside a loop that iterates over a list of names but doesn't print anything.

names_list = ['A', 'B', 'C', 'D', 'E', 'F',]

for i in names_list:
    if i in names_list:
        pass
    else:
        print(i)
