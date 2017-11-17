# useless = input()
# time = list(map(int, input().split()))

time = [3, 2, 1, 1, 2, 3, 1, 3, 2, 1]
n = len(time)

count = 0
min = min(time[0], time[1], time[2])
int_x = time.index(min)

count += min
x == int_x
while(x < n-1):
    x == int_x

    min = min(time[x:n])
    x = time.index(min, x+1, x+3)
    count+=min

print(min(count1, count2, count3))
