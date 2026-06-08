'''
Server Load Balancer
IBM's infrastructure team maintains a list of servers sorted by their processing capacity (in GHz). Given a target capacity, find the exact index of the server with that capacity.
 If no such server exists, return -1.

Problem
Given a sorted array of integers capacities and a target integer target, return the index of target in the array, or -1 if it doesn't exist.

Input:  capacities = [1, 3, 5, 7, 9, 11], target = 7
Output: 3

Input:  capacities = [2, 4, 6, 8, 10], target = 5
Output: -1
'''



def binarySearch(s, target):
    l = 0
    r = len(s)-1
    while l < r:
        midpoint = l + (r-l)//2
        if s[midpoint] == target:
            return midpoint
        elif midpoint < target:
            l = midpoint + 1
        else:
            r = midpoint - 1
    return -1


capacities = [1, 3, 5, 7, 9, 11]
print(binarySearch(capacities, 5))