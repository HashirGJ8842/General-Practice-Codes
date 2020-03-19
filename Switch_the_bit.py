import numpy
x=input('Enter the matrix')
x=list(x.split(' '))
x=list(map(int,x))
while True:
    temp=int(input('Enter the index'))
    if x[temp] == 0:
        x[temp] = 1
    else:
        x[temp] = 0
    if all([j==0 for j in x]):
        break
print(x)
