"""
========================================================
Google Foobar challenge - Level 2, Challenge 2
========================================================

Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the 
code you agreed to use is... obscure, to say the least. The bunnies are given 
food on standard-issue prison plates that are stamped with the numbers 0-9 for 
easier sorting, and you need to combine sets of plates to create the numbers in 
the code. The signal that a number is part of the code is that it is divisible 
by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 
144 and 414 are a little trickier. Write a program to help yourself quickly create 
large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function solution(L) 
which finds the largest number that can be made from some or all of these digits 
and is divisible by 3. If it is not possible to make such a number, return 0 as 
the solution. L will contain anywhere from 1 to 9 digits.  The same digit may 
appear multiple times in the list, but each element in the list may only be used 
once.


Input:
solution.solution([3, 1, 4, 1])
Output:
    4311

Input:
solution.solution([3, 1, 4, 1, 5, 9])
Output:
    94311
"""

def solution(L):
    L.sort(reverse=True) 
    r = sum(L) % 3
    i = 0

    if r == 0:
        return int(''.join(map(str,L)))

    while i < len(L)**2:
        p = str(r+3*i).strip('0')
        l = L[:]
        for d in p:
            if int(d) in l and len(l) != 1:
                l.remove(int(d))
            if sum(l) % 3 == 0:
                return int(''.join(map(str,l)))
        i += 1
    
    return 0

print(solution([3, 1, 4, 1, 5, 9]))
