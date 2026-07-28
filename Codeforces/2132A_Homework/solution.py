"""
Platform   : Codeforces
Problem    : A. Homework
Problem Code : 2132A
Language   : Python

Problem Statement:
    Vlad and Dima have been assigned a task in school for their English class. 
    They were given two strings a and b and asked to append all characters from b to string a in any order. 
    The guys decided to divide the work between themselves and, after lengthy negotiations, determined who would add each character from string b to a.

    Due to his peculiarities, Vlad can only add characters to the beginning of the word, while Dima can only add them to the end. 
    They add characters in the order they appear in string b. 
    Your task is to determine what string Vlad and Dima will end up with.

Approach:
- Read the initial string.
- Iterate through each operation.
- If the current instruction is 'D', append the corresponding character to the end.
- Otherwise, prepend the corresponding character to the beginning.
- Print the final modified string.

Time Complexity : O(n)
Space Complexity: O(n)
"""
"""Code Solution"""

for _ in range(int(input())):
    n = int(input())
    a = input()
    
    m = int(input())
    b = input()
    c = input()
    
    for i in range(m):
        if c[i] == "D":
            a = a + b[i]
        else:
            a = b[i] + a
    print(a)