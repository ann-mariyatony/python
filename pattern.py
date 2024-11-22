'''
Author:Ann mariya tony
Date:22-11-2024
'''
row1=int(input("Enter the no.of rows:"))
print("Increasing Triangle")
for i in range(row1):
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
row2=int(input("enter the no.of rows"))
print("Decreasing Triangle")
for i in range(row2):
    for j in range(row1-i):
       print("*",end=" ")
    print(" ")
row3=int(input("Enter the no.of rows:"))
print("Hill Pattern")
for i in range(1, row3+ 1):
    for j in range(row3- i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
row4=int(input("Enter the no.of rows:"))
print("Reverse hill pattern")
for i in range(row4,0,-1):
    for j in range(row4 - i):
        print(" ", end="")
    for k in range(i*2-1):
        print("*", end=" ")
    print()
