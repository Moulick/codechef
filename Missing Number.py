"""
Missing Number
You are given an array
A
A. You can decrement any element of the array by
1
1. This operation can be repeated any number of times. A number is said to be missing if it is the smallest positive number which is a multiple of
2
2 that is not present in the array
A
A. You have to find the maximum missing number after all possible decrements of the elements.

Input Format:
The first line of input contains
T
T denoting number if test cases.
The first line of each test case contains
N
N, the size of the array.
The second line of each test case contains
N
N space seperated intergers.

Output Format:
Print the answer for each test case in a new line.

Constraints:

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
10
5
1≤N≤105
0
≤
A
i
≤
10
9
0≤Ai≤109
Sample Input
2
6
1 3 3 3 6 7
3
3 0 2
Sample Output
8
4
Explanation
In the first sample test case, for
0
0 based indexing, if we decrement the
A
1
A1 to
2
2,
A
4
A4 to
4
4 and
A
5
A5 to
6
6. the array becomes
[
1
,
2
,
3
,
3
,
4
,
6
]
[1,2,3,3,4,6]. The smallest positive multiple of
2
2 which is not in the modified array is
8
8, thus the missing number is
8
8.
In the second sample test case, with or without decrements we can get
2
2 as the only multiple of
2
2 in the array, thus the missing number is
4
4.

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
"""


def Solve (arr):

    new_arr =  [(1<<((x).bit_length()-1)) if x !=0 else 0 for x in arr]
    new = [(x-1) if x%2!=0 else x for x in arr]

    return (max(new)+2)


T = int(input())
for _ in range(T):
    n = int(input())
    arr = map(int, input().split())

    out_ = Solve(arr)
    print (out_)
