"""
Platform   : Codeforces
Problem    : A. Only One Digit
Problem Code : 2126A
Language   : Python

Problem Statement:
    You are given an integer x.
    You need to find the smallest non-negative integer y such that the numbers x and y share at least one common digit. 
    In other words, there must exist a decimal digit d that appears in both the representation of the number x and the number y.

Approach:
- Take n as number of Digits it should accept.
- Store each input number as a string.
- Find the smallest digit present in the string using min().
- Print that digit.

"""

n = int(input())
x_list = []
for i in range(n):
    x = input()
    x_list.append(x)
for j in x_list:
    print(min(j))