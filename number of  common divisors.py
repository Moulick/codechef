num1, num2 = map(int, input().split())


# print(num1, num2)


divi = []
def gcd(a,b):
    if (a == 0):
        return b
    return gcd(b % a, a)

# for x in range(1, gcd(num1,num2)+1):
#     if num1%x==0 and num2%x==0:
#         divi.append(x)
# print(divi.__len__())

gcded = gcd(num1,num2)
arr=[]
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            arr.append(i)
            if i*i != n:
                arr.append(n/i)
    # print('arr:', arr)
    return arr

print(list(divisorGenerator(gcded)).__len__())
