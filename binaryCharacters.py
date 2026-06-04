'''

IBM OA #1

Given a random list array of numbers, find the 2nd highest frequency item in the array.

'''

arr = [1, 1, 2, 2]
# 1. Similar structure to k highest frequency

# Q1. What happens when 2 chars are highest freq
# Q2. What are the bounds?

def frequency(arr):

    mapped = {}
    for i in arr:
        mapped[i] = mapped.get(i, 0) + 1

    if len(mapped) == 1:
        return None

    freq = [[] for i in range(len(arr)+1)]

    for num, freq_count in mapped.items():
        freq[freq_count].append(num)
    
    count = 0
    index = []
    for i in range(len(freq)-1, -1, -1):
        if count == 1 and freq[i] != []:
            return freq[i]
        if freq[i] != [] and count == 0:
            count += 1
            index = freq[i]
        if freq[i] == []:
            continue
    return index

print(frequency(arr))

