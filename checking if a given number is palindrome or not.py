

## checking if a given number is palindrome or not


def palindrome_number(n,r):
    if n==0:
        return r
    else:
        return palindrome_number(n//10,(r*10+n%10))
    
n=int(input("enter number: "))
r=0
a=palindrome_number(n,r)
if n==a:
    print("given number is palindrome")
    
else:
    print("not a palindrome number ")
    

print(n,r)
