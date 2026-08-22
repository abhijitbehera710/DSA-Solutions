"""
Platform   : Codeforces
Problem    : A. Dr. TC
Problem Code : 2106A
Language   : Python

Problem Statement:
    You are given a binary string s of length n.

    For every index i, create a new string by copying s and flipping
    the character at index i.

    All n strings are placed as rows of a grid.

    Find the total number of 1s present in the entire grid.


Example:

    s = 10110011

    Number of 0s = 3
    Number of 1s = 5


Approach:
    We don't need to actually create all n strings.

    Let:
        count_0 = number of 0s
        count_1 = number of 1s

    When one character is flipped, only the number of 1s in that row
    changes.

    | Character Flipped | New Number of 1s | Number of Times | Contribution |
    |-------------------|------------------|-----------------|--------------|
    | 0 → 1             | count_1 + 1      | count_0         | count_0 × (count_1 + 1) |
    | 1 → 0             | count_1 - 1      | count_1         | count_1 × (count_1 - 1) |

    Therefore:

        result = count_0 × (count_1 + 1)
                 + count_1 × (count_1 - 1)


Example Calculation:

    s = 10110011

    count_0 = 3
    count_1 = 5

    result = 3 × (5 + 1) + 5 × (5 - 1)
           = 3 × 6 + 5 × 4
           = 18 + 20
           = 38

    Answer = 38


Why this works:
    Every row is created by changing exactly one character.

    - Every 0 that we flip gives a row with count_1 + 1 ones.
    - Every 1 that we flip gives a row with count_1 - 1 ones.

    So we only need the number of 0s and 1s.

Time Complexity:
    O(n) per test case
    O(t × n) for all test cases

Space Complexity:
    O(n) for storing the input string.
    O(1) additional space.


Final Formula:

    Answer =
        count_0 × (count_1 + 1)
        + count_1 × (count_1 - 1)

"""
"""Code Solution"""

for _ in range(int(input())):
    n = int(input())
    a = input()

    count_0 = a.count("0")
    count_1 = a.count("1")

    result = count_0 * (count_1 + 1) + count_1 * (count_1 - 1)

    print(result)