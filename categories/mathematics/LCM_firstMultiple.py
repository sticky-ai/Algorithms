"""
Find the smallest integer not less than the given limit which is divisible by all integers from the given array.

Example

For divisors = [2, 3, 4] and start = 13, the output should be
firstMultiple(divisors, start) = 24.
"""

def firstMultiple(divisors, start):
    while True:
        if all([start % d == 0 for d in divisors]):
            return start
        start += 1
