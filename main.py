def palindrome(y):
    a=len(y)-1
    d=0
    while (d<a):
        if y[d]!=y[a]:
            return False
        d=d+1
        a=a-1
    return True
y=(1,2,3,4,5,5,4,3,2,1)
if (palindrome(y)):
    print("Combination is a palindrome")
else:
    print("Combination is Not an Palindrome")        
        