




# sum of digits

def sum_of_digits(n):
    if n<10:
        return n
    return (n%10)+sum_of_digits(n//10)

n=int(input("enter digits"))
print(sum_of_digits(n))