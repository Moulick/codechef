"""
Count the Birds
Zulu is a nature lover kind of boy. He visits forests, natural parks and other scenic places regularly. While one of his visit to a bird's park, a problem came in his mind. Suppose, there are
N
N birds present in the park. Each of the bird is rotating around a circular pillar present in the middle of the park. We are provided with the time periods
(
T
[
i
]
)
(T[i]) for each bird. Time period is defined as the time needed to complete a full rotation around the pillar.

Consider that each bird starts its rotation from a fixed point i.e. where Zulu is sitting. Now, Zulu wants to know about the number of birds which are going to be present at that spot at any given time. Since Zulu is a naughty child, he won't give you a fixed time instant instead he gives a range of time and wants you to calculate the maximum number of birds at any integral time instant within that range. To further complicate the question, he is going to give you multiple queries also.

Input :

First line of input will contain
T
E
S
T
TEST denoting number of test cases. For each test case, First line will contain
N
N denoting number of birds. In the second line
N
N numbers will be given representing time periods
(
T
[
i
]
)
(T[i]) for each of the bird. In next line
Q
Q will be given which corresponds to number of queries asked. Below this there will be
Q
Q lines given each having two integers
X
X &
Y
Y which refer to the start time and end time of the given query.

Output :

For each of the query, output the maximum number of birds in a separate line.

Constraints :

1
≤
1≤
T
E
S
T
TEST
≤
5
≤5
1
≤
N
,
Q
,
X
,
Y
≤
2
∗
10
5
1≤N,Q,X,Y≤2∗105
1
≤
T
[
i
]
≤
10
9
1≤T[i]≤109
X
≤
Y
X≤Y
Sample Input
1
2
1 10001
2
1 5
10000 10002

Sample Output
1
2

Explanation
In the first query, first bird will be present at the starting spot at time t = 1, 2, 3, 4, 5 whereas second bird will not be able to complete any single rotation in the given time range. So, answer will be 1.

In the second query, both of the birds will be present at time t = 10001. So, answer will be 2.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

"""

"""
T = 1
Number_of_birds = 2
Time periods = 1 10001
Q = 2
query_time_range1 = 1 5
query_time_range1 = 10000 10002
"""

from functools import reduce    # need this line if you're using Python3.x

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)

"""
T = 1
Number_of_birds = 2
Time periods = 1 10001
Q = 2
query_time_range1 = 1 5
query_time_range1 = 10000 10002
"""
T = int(input())
for _ in range(T):

    num_bir= int(input())
    time_period = list(map(int, input().split()))
    time_period_lcm = get_lcm_for(time_period)

    Q = int(input())
    for ff in range(Q):
        counts = []
        max_count = 0
        q_per_start, q_per_stop = list(map(int, input().split()))
        for x in range(q_per_start, q_per_stop+1):
            count = 0
            if x%time_period_lcm == 0:
                max_count = time_period.__len__()
                # print("x :",x, "lcm :", max_count)
                break

            # print("time :", x, "max_count: ", max_count)
        # print("max_count_final: ", max_count)
        print(max_count)