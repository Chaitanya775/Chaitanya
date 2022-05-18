n=int(input('enter the number to be checked : '))
x=0
for i in range(1,n+1):
    if n%i == 0 :
        x=x+i
if x==n+1:
    print('prime')
elif x>(n+1):
    print('non prime')
