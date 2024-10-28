while True:
    print("1.\tconvert celsius to Fahrenheit")
    print("2.\t convert Fahrenheit to celsius")
    print("3.\tExit the program")
    choice=int(input("Enter the choice:"))
    if choice==1:
       Temp= int(input("Enter a temperature in Celsius:"))
       f = (9 / 5 * Temp) + 32
       print(f"The equivalent temperature in fahrenheit is {f}")
    elif choice==2:
       Temp1 = int(input("Enter a temperature in fahrenheit:"))
       c=(Temp1- 32) * 5/9
       print(f"The equivalent temperature in celsius is {c}")
    elif choice==3:
        break
    else:
        print("Invalid entry")



