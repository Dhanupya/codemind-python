n=int(input())
b=n*n
t=n
r=0
y=0
while n!=0:
    c=n//10
    p=n%10
    r=r*10+p
    n=c
f=r*r

while f!=0:
    z=f//10
    p=f%10
    y=y*10+p
    f=z
if b==y:
    print("True")
else:
    print("False")