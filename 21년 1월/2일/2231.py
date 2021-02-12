import sys


sys.stdin = open('input.txt')

N = int(input())

# hap = 0
# def calc(a,k):
#     global hap
#     b = 0
#     rest = 0
#     for i in range(1,k+1):
#         b *= 10
#     rest = a % b
#     for i in range(1,k+1):
#         rest %= 10
#     hap += rest
#     b /= 10
#     if a-rest*b == 0:
#         return
#     calc(a-rest*b , k+1)

for i in range(1,N):
    # calc(i,1)
    # if hap + i == N:
    #     print(i)
    #     break
    # hap=0
    hap = i
    ans = i
    while i:
        a = i // 10
        b = i % 10
        hap += b
        i = a
    if hap == N:
        print(ans)
        break

