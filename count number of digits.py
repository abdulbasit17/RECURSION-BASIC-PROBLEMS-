
count=0
def count_digits(n):
    global count
    if n!=0:
        count+=1
        return count_digits(n//10)
    return count
    
    
n=int(input("enter digits: "))
print(count_digits(n))