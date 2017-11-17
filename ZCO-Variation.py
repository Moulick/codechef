
import random
import time

#for timming
t0 = time.clock()
#list of 200,000 random numbers
strength = [0,1,3,5,10]

k = 3

n = len(strength)

count = 0
strength.sort()
x = 0
y = n-1

while (x < n - 1):
    if abs(strength[x] - strength[y]) >= k:
        count += n - y
        x += 1
        y = x

    else:
        y += 1

    if y == n:
        x += 1
        y = x
t1 = time.clock()
print(count)
print(t1-t0)