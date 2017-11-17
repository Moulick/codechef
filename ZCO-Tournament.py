import random
import time

#for timming
t0 = time.clock()
#list of 200,000 random numbers
teams = [random.randrange(0,1000) for x in range(200000)]

total_rev= 0

#reverse sort
teams.sort(reverse=True)

tot = sum(teams)
leng = 200000

for x in range(len(teams)):
    leng -= 1
    first = teams[x]*leng
    tot -= teams[x]
    ads = (first) - (tot)
    total_rev += ads
print(total_rev)
t1 = time.clock()

print(t1-t0)