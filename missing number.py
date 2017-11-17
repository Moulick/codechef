f = open("in05.txt", 'r')

n = int(f.readline())
print('this is n: ', n)


arr = map(int, f.readline().split())

dict = {}
for x in arr:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

for ball, num in dict.items():
    if num == 1:
        print(ball)
