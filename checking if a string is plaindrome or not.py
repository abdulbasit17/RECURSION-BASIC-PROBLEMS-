



## checking if a given string is palindrome or not



def palindrome_string(n):
    
    if len(n)==1:
        return n
    else:
        a= palindrome_string(n[1:])+n[0]
        return a
    
n=str(input("enter string: "))
if n==palindrome_string(n):
    print(" the given string is palidrome")
else:
    print("the give string is not palindrome!")
    
print(palindrome_string(n))

    
    