"""
Platform   : Codeforces
Problem    : A. Game with Integers
Problem Code : 1899A
Language   : Python

Problem Statement:
    Vanya and Vova are playing a game. Players are given an integer n. 
    On their turn, the player can add 1 to the current integer or subtract 1. 
    The players take turns; Vanya starts. If after Vanya's move the integer is divisible by 3, then he wins.
     If 10 moves have passed and Vanya has not won, then Vova wins. 
    Write a program that, based on the integer n, determines who will win if both players play optimally.

Approach:
The important observation is to consider the remainder of n when divided by 3.

There are three possible cases:

1. n % 3 == 0
   Vanya can either add 1 or subtract 1, so the resulting number
   will not be divisible by 3. Therefore, Vanya cannot win immediately.
   Vova can then make a move that leaves a number divisible by 3,
   so Vova wins.

2. n % 3 == 1
   Vanya can subtract 1, making the number divisible by 3.
   Therefore, Vanya wins.

3. n % 3 == 2
   Vanya can add 1, making the number divisible by 3.
   Therefore, Vanya wins.

Therefore:
- If n is divisible by 3 → Second
- Otherwise → First


Time Complexity: O(t)
Space Complexity:  O(1)
"""
"""Code Solution"""

list_n = []
for _ in range(int(input())):
    n = int(input())
    list_n.append(n)
for i in list_n:
    if i % 3 == 0:
        print("Second")
    else:
        print("First")