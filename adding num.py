'''
Author:Ann mariya tony
date:29-11-2024
'''
def recursion_add(n1,n2):
    if n2==0:
        return n1
    else:
        return(recursion_add(n1+1,n2-1))
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
print("Sum of 2 digits:",recursion_add(n1,n2))