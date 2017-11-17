import time

n, k = 7, 4

strength = [0,1,1,3,4,5,5,10]
start = time.clock()
count = 0
strength.sort()
x = 0
y = n-1

while(x<y):
    if strength[x] + strength[y] < k:
        count += y-x
        x +=1
        y-= 1

    else:
        y -=1



end = time.clock()
print(count)
print(end - start)