'''
Author:Ann mariya tony
date:06-12-2024
'''
def fibonacci_number(num):
    list=[]
    num1=0
    num2=1
    for i in range(num):
        list.append(num1)
        num1,num2=num2,num1+num2
    return(list)



