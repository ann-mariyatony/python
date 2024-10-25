'''
Author:Ann mariya tony
Date:25-10-2024
Description:A Program program to convert temperature values back and forth between Celsius and Fahrenheit. 
'''
Temp=int(input("Enter the temperature:"))
scale=input("Is this in (C)elsius or (F)ahrenheit ? : ")
if scale=="C":
    temp1  =(9/5*Temp)+32
    print(Temp,"celsius is",temp1,"Fahrenheit")
else:
    temp2 = (5/9)*(Temp-32)
    print(Temp,"Fahrenheit is ",temp2,"Celsius")
