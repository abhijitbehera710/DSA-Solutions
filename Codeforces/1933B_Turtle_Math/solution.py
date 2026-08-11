"""
Platform   : Codeforces
Problem    : B. Turtle Math: Fast Three Task
Problem Code : 1933B
Language   : Python

Problem Statement:
    You are given an array a1,a2,…,an.
        In one move, you can perform either of the following two operations:
        Choose an element from the array and remove it from the array. As a result, the length of the array decreases by 1;
        Choose an element from the array and increase its value by 1.
        You can perform any number of moves. If the current array becomes empty, then no more moves can be made.
        Your task is to find the minimum number of moves required to make the sum of the elements of the array a divisible by 3. 
        It is possible that you may need 0 moves. Note that the sum of the elements of an empty array (an array of length 0) is equal to 0.

Approach:
- Calculate the sum of all elements.
- Find sum % 3.
- If the remainder is:
    0 → sum is already divisible by 3 → answer 0.
    2 → increase any element by 1 → answer 1.
    1 → try removing each element one by one.

- For remainder 1, check:
    (total - arr[j]) % 3 == 0
    If true for any element → remove that element → answer 1.
    If no such element exists → increase an element twice → answer 2.
- Use break as soon as you find a removable element that makes the sum divisible by 3.

Time Complexity: O(n) per test case
Space Complexity: O(n) for storing the array.
"""
"""Code Solution"""

t = int(input())
for i in range(t):
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)

    total = sum(arr_list)
    rem = total % 3

    if (rem == 0):
        print(0)
    elif (rem == 2):
        print(1)
    else:
        is_exist = False
        for j in range(n):
            if ((total - int(arr_list[j])) % 3 == 0):
                is_exist = True
                break
        if ( is_exist):
            print(1)
        else:
            print(2)