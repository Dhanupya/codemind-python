n=int(input())
t=n
r=0
while n!=0:
    c=n//10
    p=n%10
    r=r*10+p
    n=c
if r==t:
    print("True")
else:
    print("False")