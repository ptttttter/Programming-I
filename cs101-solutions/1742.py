import math
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    dp = 1 << m
    *lst, = map(int, input().split())
    for i in range(0,n):
        a, c = lst[i], lst[i+n]
        p = math.floor(math.log2(c))
        for j in range(0,p):
            dp = dp | (dp>> (a << j)) 
        rest = c - (1 << p) + 1
        dp = dp | (dp >> (a * rest))
        s = bin(dp)
    print(bin(dp).count('1')-1)