# # sales = [
# # {"product": "Widget", "quantity": 5},
# # {"product": "Gadget", "quantity": 3},
# # {"product": "Widget", "quantity": 2},
# # {"product": "Gizmo", "quantity": 1},
# # ]

# # Write a Python loop to print the total quantity sold per product.

# # Expected Output :
# # Widget: 7
# # Gadget: 3
# # Gizmo: 1

# sales = [
#     {"product": "Widget", "quantity": 5},
#     {"product": "Gadget", "quantity": 3},
#     {"product": "Widget", "quantity": 2},
#     {"product": "Gizmo", "quantity": 1},
# ]

# for item in sales:
#     keys = item.keys()
#     print(keys[0])


# def prime(no):
#     if no > 1:
#         for i in range(2, no+1):
#             if no % i == 0:
#                 print("It's a prime")
#             else:
#                 print("It's not a prime")
#     else:
#         print("Invalid number")


# prime(47)


# expression = "231*+9-"

# ls = []


# def evaluate_postfix(expression):
#     for i in expression:
#         print(i)
#         try:
#             j = int(i)
#         except:
#             sym = i
#         try:
#             if int(j) >= 0 and (j) <= 9:
#                 ls.append(int(i))
#         except:
#             ls.append(sym)
#     print(ls)

# #     print("Postfix Evaluation:", evaluate_postfix(expression))

# evaluate_postfix(expression)


# Write a program to find the longest substring without repeating characters. Input: abccbadcb Expected Output: cbad

# input_str = 'abccbadcb'

# lng_str = []
# temp = ''
# for i in input_str:
#     if i not in temp:
#         temp = temp+i
#         lng_str.append(temp)

#     else:
#         temp = temp[-1]
# print(lng_str)


# 11. Find the top 3 highest-paid employees from each department.
# Sample Data:
# import pandas as pd
# data = [
#     (1, "Amit", "IT", 90000),
#     (2, "Neha", "HR", 50000),
#     (3, "Raj", "IT", 85000),
#     (4, "Priya", "HR", 60000),
#     (5, "Suresh", "Finance", 75000),
#     (6, "Anjali", "Finance", 80000),
#     (7, "Vikas", "IT", 92000),
#     (8, "Rohan", "HR", 58000),
#     (9, "Meera", "Finance", 82000)
# ]

# id = []
# name = []
# dept = []
# salary = []

# for i in data:
#     id.append(i[0])
#     name.append(i[1])
#     dept.append(i[2])
#     salary.append(i[3])
# print(id, name, dept, salary)

# df = pd.DataFrame(id)

# df["Name"] = name
# df["Department"] = dept
# df["Salary"] = salary

# print(df)

# # highest_emp = df.groupby(["Department", "Name"])["Salary"].max()

# # print(highest_emp.sort_values(by='Salary', ascending=False))

# sales = [
#     {"product": "Widget", "quantity": 5},
#     {"product": "Gadget", "quantity": 3},
#     {"product": "Widget", "quantity": 2},
#     {"product": "Gizmo", "quantity": 1},
# ]

# df_sale = pd.DataFrame(sales)

# print(df_sale)

# total = df_sale.groupby("product")["quantity"].sum().head()
# hi = total.sort_values(ascending=False)
# print(hi)

# Q: You are given a list of sales records. Each record contains a product, store, and quantity.
# Write code to find the total quantity sold per product and return the top 2 products with highest sales.

import pandas as pd

sales = [
    {"product": "Widget", "store": "A", "quantity": 10},
    {"product": "Gadget", "store": "B", "quantity": 4},
    {"product": "Widget", "store": "C", "quantity": 6},
    {"product": "Gizmo", "store": "A", "quantity": 8},
    {"product": "Gadget", "store": "C", "quantity": 7},
]

df = pd.DataFrame(sales)

total = df.groupby(['store', 'product'])['quantity'].sum()

top_two = total.sort_values(ascending=False)
print(top_two)
