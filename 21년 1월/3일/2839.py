import sys


sys.stdin = open('input.txt')

N = int(input())

sum = N/5
if((N%5)%3==0):
    sum += (N%5)/3
    # print sum

else:
    print(-1) 
    

