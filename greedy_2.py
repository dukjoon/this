# 1이 될 때 까지

n, k = map(int,input().split())
count = 0

while 1:
    if n == 1:
        break
    else:
        if n % k == 0:
            n = n / k
            count += 1
        else:
            n = n - 1
            count += 1

print(count)
