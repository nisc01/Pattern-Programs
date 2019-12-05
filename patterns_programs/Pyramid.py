#Program to print pyramid using *
n=int(input('Enter the number of rows'))
for row in range(1,n+1):
    space=n-row
    print(' '*space,end='')
    print('*'*row,end='')           #Prints Half Pyramid
    print('*'*(row-1))              #Prints the next * after Half Pyramid

#program to print pyramid using numbers

for row in range(1,n+1):
    space=n-row
    print(' '*space,end='')
    for i in range(row,row*2):
        print(i,end='')                   #Prints Half Pyramid
    for i in range(row*2-2,row-1,-1):
        print(i,end='')                   #Prints the next numbers after Half Pyramid
    print('\r')

