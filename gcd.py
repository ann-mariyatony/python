def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
print(f"The GCD:{gcd(n1,n2)}")