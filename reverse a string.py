


# reversing a string , by taking input from user


def rev_str(n):
    if len(n)==1:
        return n
    else:
        return rev_str(n[1:])+n[0]
    
    
n=str(input("enter string to be reversed: "))

print(rev_str(n))

    