





### power of a number

def power(x,y):
    if y==0:
        return 1
    return x*power(x,y-1)

x=int(input("enter number: "))
y=int(input("enter power: "))

print(power(x,y))