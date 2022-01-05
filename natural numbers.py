


## natural number in agiven range


def natural_number(x,y):
    if x>y:
        return  
    print(x, " ",end="")
    
    return natural_number(x+1,y)
    

x=int(input("enter first number: "))
y=int(input("enter last number: "))

print(natural_number(x,y))