
#Program to print half pyramid using *
n=int(input('enter the number of rows'))
for i in range(1,n+1):
    print('* '*i)

#Program to print half pyramid using number
for i  in range(1,n+1):
    j=0
    while i>=1:
        j+=1
        print(j,' ',end='')
        i-=1
    print('\r')
