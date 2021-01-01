import sys


sys.stdin = open('input.txt')

n, m = map(int, input().split())
list_stack = list(map(int, input().split()))

from itertools import combinations

comb = list(combinations(list_stack, 3))
# print(comb)
ans = 0
for i in comb:
    res = sum(i)
    if res <= m and res > ans:
        ans = res
print(ans)