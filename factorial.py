'''
Author:Ann mariya tony
date:29-11-2024
'''
def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
num = int(input("Enter a number:"))
print("Factorial:",factorial(num))