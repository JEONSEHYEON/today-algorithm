import sys


sys.stdin = open('input.txt')

num1,num2 = map(int, input().split())

print(num1*num2)