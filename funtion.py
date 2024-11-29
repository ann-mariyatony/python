def mobile_no(num):
    if len(num)==10 and num[0] in ["9","8","7"]:
        print("Its a  mobile number")
    else:
        print(" Its a invalid mobile number")
num=str(input("Enter a number:"))
mobile_no(num)


