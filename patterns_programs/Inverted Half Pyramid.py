#Program to print inverted half pyramid using *
n=int(input('Enter the number of rows'))
for row in range(n,0,-1):
    print('* '*row)


#Program to print inverted half pyramid using numbers
for row in range(n,0,-1):
    j=1
    while row>=1:
        print(j,' ',end='')
        j+=1
        row-=1
    print('\r')
