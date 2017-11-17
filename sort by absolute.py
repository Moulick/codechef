N = int(input())

num_array = list(map(int, input().split()))

arr = sorted(num_array, key=abs)
print(arr)
for x in arr:
    print(x, sep = '', end = ' ')
print()