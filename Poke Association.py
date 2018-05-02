"""
New pokemons have been found near Mount Kukrimaro. They need to be trained so that they can perform better in unknown situations. Mostly they are fighting and grass pokemons. So the first instruction they are given is to preacefully have dinner. To do that, they are made to sit in a round table with at max N chairs around it. There are E(>= N) number of grass pokemons and H(>= N) number of fighting pokemons. There could be many ways to sit but we cannot let two fighting types to sit side by side, or else there will be commotion. Now we are interested to know the number of valid arrangements possible given you can not distinguish between any two members of a type. As answer could be very large, output the answer modulo 10^9+7.



Input

First line of the input file contains number of test cases T. Each line of the next T lines represents a test case. Each test case contains N, E and H respectively.

Output

For each test case output the number of arrangements possible(modulo 109+7) in a new line.

Constraints

1 ≤ T ≤ 103
1 ≤ N ≤ 106
N ≤ E ; H ≤ 2*N


Example

Input:
1
3 4 5

Output:
4


Explanation

If G represents a grass member and F represents a fighting member then there are following valid arrangements:
GGG
GGF
GFG
FGG

GFG and GGF are different arrangements as the chairs are different. Its just that you cannot distinguish between two members of a type.
"""



