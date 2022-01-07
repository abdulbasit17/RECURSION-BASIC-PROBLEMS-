




## reverse of a given number 

def rev_number(a,b):
    if a==0:
        return b
    else:
        return rev_number(a//10,(b*10+a%10))
    
a=int(input("enter number: "))
b=rev_number(a,0)
print(a,b)
    


