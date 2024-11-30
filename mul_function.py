'''
Author:Ann mariya tony
date:30-11-2024
'''
def product_of_list(list):
    mul=1
    for i in list:
        mul=(mul*i)
    print("product of all the numbers in list:",mul)
list=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
    n=int(input("Enter the numbers:"))
    list.append(n)
product_of_list(list)