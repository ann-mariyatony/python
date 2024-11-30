'''
Author:Ann mariya tony
date:30-11-2024
'''
def sum_of_list(list):
    sum=0
    for i in list:
        sum=sum+i
    print("Sum of all the numbers in list:",sum)
list=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
    n=int(input("Enter the numbers:"))
    list.append(n)
sum_of_list(list)
