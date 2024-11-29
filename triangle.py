'''
Author:Ann mariya tony
date:29-11-2028
'''
def triangle_side(triangle):
    if side1==side2:
        print("The given triangle is a right triangle ")
    else:
        print("The given triangle is not a right triangle ")
num1=int(input("Enter the length of the first side:"))
num2=int(input("Enter the length of the second side:"))
num3=int(input("Enter the length of third side:"))
triangle=[num1,num2,num3]
triangle.sort()
side1=num3*num3
side2=num1*num1+num2*num2
triangle_side(triangle)