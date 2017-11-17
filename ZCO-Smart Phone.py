n = int(input())
budgets = []
for x in range(n):
    budgets.append(int(input()))

maxi = 0
budgets.sort(reverse=True)

for x in range(len(budgets)):
    ma = (budgets[x])*(x+1)
    if ma > maxi:
        maxi = ma

print(maxi)
