#print Floyd's Triangle
n=int(input('Enter the number of rows'))
num=1
for row in range(1,n+1):
    while row >=1 :
        print(num,'',end='')
        num+=1
        row-=1
    print('\r')