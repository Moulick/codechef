"""
Initially, there are
K
K number of almonds in the bowl. Alice eats
A
A  almonds in the morning and
B
B number of almonds is added to her bowl in the evening. You need to determine the number of consecutive days for which Alice will be able to eat almonds.

Input Format:
The first line of the input contains an integer T,the number of test cases.
Each test case is described by
3
3 lines,having the integers A, B and K respectively.

Output Format:

Output the answer for each test case in a new line.
If the activity can go on forever,print -1.

Input Constraints:

1
≤
T
≤
5
1≤T≤5
0
≤
A
≤
10
9
0≤A≤109
0
≤
B
≤
10
9
0≤B≤109
0
≤
K
≤
10
9
0≤K≤109
Sample Input
1
2
1
2
Sample Output
1
Explanation
In the sample case, there are initially 2 almonds in the bowl.On the first day, Alice eats 2 almonds and later in the evening, 1 almond is added into the bowl.The next morning, there will be only 1 almond in the bowl. So, the answer is 1 day.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
"""


def solve(A, B, K):
    if K < A:
        return 0

    if B and K == 0:
        return 0
    if K == 0:
        return 0

    if A - B <= 0:
        return -1

    count = 0
    total = K
    diff = (-A + B)
    while total >= A:
        total = total + diff
        count += 1
    return count


T = int(input())
for _ in range(T):
    A = int(input())
    B = int(input())
    K = int(input())

    out_ = solve(A, B, K)
    print(out_)