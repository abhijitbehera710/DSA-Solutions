"""
Platform   : Codeforces
Problem    : A. Painting With Two Colors
Problem Code : 2134A
Language   : Python

Problem Statement:
    You are given three positive integers n, a, and b.

    Consider a row of n cells, initially all white and indexed from 1 to n.
    You will perform the following two steps in order:

    1. Choose an integer x such that 1 ≤ x ≤ n-a+1, and paint the
       a consecutive cells x, x+1, ..., x+a-1 red.

    2. Choose an integer y such that 1 ≤ y ≤ n-b+1, and paint the
       b consecutive cells y, y+1, ..., y+b-1 blue.

    If a cell is painted both red and blue, its final color is blue.

    A coloring is considered symmetric if the color of every cell i
    is the same as the color of cell n+1-i.

    Determine whether there exist suitable values of x and y such that
    the final coloring is symmetric.

Approach:
The important observation is to consider the parity (odd/even) of n and b.

For the final coloring to be symmetric, the blue segment must either:
1. Be centered around the middle of the row, or
2. Be positioned in such a way that the red segment can make the
   remaining coloring symmetric.

There are two important conditions:

1. n % 2 == b % 2
   The blue segment must have the same parity as n so that it can
   be placed symmetrically around the center.

2. If the above condition is satisfied, we can make the coloring
   symmetric if either:
      - b > a
      - a % 2 == b % 2

Therefore, the answer is YES if:

    n % 2 == b % 2
    and
    (b > a or a % 2 == b % 2)

Otherwise, the answer is NO.

Therefore:
- If n % 2 != b % 2 → NO
- If n % 2 == b % 2 and (b > a or a % 2 == b % 2) → YES
- Otherwise → NO


Time Complexity: O(t)
Space Complexity: O(1)

"""
"""Code Solution"""

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    
    if n % 2 == b % 2:
        if (b > a) or (a % 2 == b % 2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")