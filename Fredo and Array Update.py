N = int(input())

num_array = list(map(int, input().split()))

avg = sum(num_array)/float(len(num_array))

floor = int(avg)

print(int(avg)+1)