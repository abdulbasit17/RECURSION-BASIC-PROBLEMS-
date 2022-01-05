



##  checking if a given number is arm strong number or not

## arm strong number is : ex: 153: (1*1*1)+(5*5*5)+(3*3*3)=153

def arm_strong(n):
    if n<10:
        return n*n*n
    return (n%10)*(n%10)*(n%10)+arm_strong(n//10)

n=int(input("enter number: "))

x=arm_strong(n)
if x==n:
    print(n,"number is armstrong")
else:
    print(n," is not an armstrong number")
