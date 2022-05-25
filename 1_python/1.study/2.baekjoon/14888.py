from collections import deque

n = int(input())
nums = deque(map(int, input().split()))
operators = deque(map(int, input().split()))

# 초기화
max_value = -1000000000
min_value = 1000000000

def dfs(depth, total, plus, minus, multiply, divide):