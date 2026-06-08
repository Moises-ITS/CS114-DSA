'''
###Problem###
You're building a live crowd analytics tool for a stadium. Fans are chanting player numbers in sequence, recorded as an array.
Given a window size k, return the most frequent player number chanted in each window as it slides across the array.
If there's a tie, return the smallest number.

Input = [3,1,3,2,1,3], k = 3

Output = [3,1,1,1]
'''

#Inference - sliding window approach

def slidingWindow(array, k):
    hashMap = {}
    res = []

    for r in range(k):
        hashMap[array[r]] = hashMap.get(array[r], 0) + 1
    res.append(max(hashMap, key=hashMap.get))

    left = 0
    right = k
    while right < len(array):

        hashMap[array[right]] = hashMap.get(array[right], 0) + 1
        hashMap[array[left]] -= 1
        if hashMap[array[left]] == 0:
            del hashMap[array[left]]
        res.append(max(hashMap, key=hashMap.get))
        right += 1
        left += 1
    return res

print(slidingWindow([3,1,3,2,1,3], 3))

