# https://www.acmicpc.net/problem/3003

chess = [1, 1, 2, 2, 2, 8]
lst = map(int, input().split(' '))
rst = [str(x - y) for x, y in zip(chess, lst)]
print(' '.join(rst))