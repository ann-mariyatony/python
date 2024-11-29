'''
Author:Ann mariya tony
date:29-11-2024
'''
def recursive_mul(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+recursive_mul(n1,n2-1)
n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
print("Product of two numbers:",recursive_mul(n1,n2))


