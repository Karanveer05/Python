def Largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=int(input("Enter the First Number :"))
b=int(input("Enter the Second Number :"))
c=int(input("Enter the Second Number :"))
print(f"The Largest Number From the Following Scaned Numbers is : {Largest(a,b,c)}")
