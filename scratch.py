def mul(elem):
    if elem > 0:
        return elem * 3
    return elem * -5


def fun(arr, k):
    arrlist = list()

    for elem in arr:
        l1 = [elem - i for i in arr]

        print("l1: ", l1)

        al = sorted(map(mul, l1))[:k]

        print("al: ", al)
        arrlist.append(al)
        print('arrlist: ', arrlist)

    return arrlist


for x in range(int(input())):

    i, k = input().split()

    arr = sorted(map(int, input().split()))

    arrlist = fun(arr, int(k))

    res = min(list(map(sum, arrlist)))

    print(res)