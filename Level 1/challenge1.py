"""
========================================================
Google Foobar challenge - Level 1, Challenge 1
========================================================

Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", 
and other "good" numbers have been lording it over the poor minions who are stuck 
with more boring IDs. To quell the unrest, Commander Lambda has tasked you with 
reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 

She's concatenated the prime numbers in a single long string: "2357111317192329...". 
Now every minion must draw a number from a hat. That number is the starting index in 
that string of primes, and the minion's new ID number will be the next five digits in 
the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in 
the starting index n of Lambda's string of all primes, and returns the next five 
digits in the string. Commander Lambda has a lot of minions, so the value of n will
always be between 0 and 10000.


Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113
"""

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    D = {}
    q = 2
    
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

def string_of_primes(n):
    s = ""
    for x in gen_primes():
        s += str(x)
        if len(s) >= n+5:
            return s
        
def solution(n):
    return string_of_primes(n+5)[n:n+5]

print(solution(3))