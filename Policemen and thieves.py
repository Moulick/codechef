"""
You are given a grid of size
N
×
N
N×N that has the following specifications:

Each cell in the grid contains either a policeman or a thief.
A policeman can only catch a thief if both of them are in the same row.
Each policeman can only catch one thief.
A policeman cannot catch a thief who is more than
K
K units away from the policeman.
Write a program to find the maximum number of thieves that can be caught in the grid.

Input format

First line:
T
T (number of test cases)
For each test case
First line: Two space-separated integers
N
N and
K
K
Next
N
N lines:
N
N space-separated characters (denoting each cell in the grid)
Output format

For each test case, print the maximum number of thieves that can be caught in the grid.

Constraints

1
≤
T
≤
10
1≤T≤10
 1
≤
N
≤
1000
1≤N≤1000
 1
≤
K
≤
N
∗
N
1≤K≤N∗N
Sample Input
1
3 1
P T P
T P T
T T P
Sample Output
3
Explanation
Total Thieves = 5
Number of thieves reachable by policemen in Row 1 = 1
Number of thieves reachable by policemen in Row 2 = 2
Number of thieves reachable by policemen in Row 3 = 1
However, one policeman can catch at most 1 thief. Hence, in Row 2, only 1 thief is catchable.
Therefore, the 3 thieves can be caught.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

"""



def solution (A, K):
    print(A)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().split())
    out_ = solution(A, K)
    print (out_)