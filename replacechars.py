'''
Given a string that consists of lowercase English letters, select exactly one non-empty substring of s and replace each character of it with the previous character of the English
alphabet. For examples 'b' is converted to 'a', 'c' is converted to 'b', ..., and 'a' is converted to 'Z'.

Find the lexicographically smallest string that can be obtained after performing the above operation exactly once.

Example s = "hackerrank"

Select New string

h gackerrank

ha gzckerrank

err hackdqqank
'''

s = "aaaa"


def lexi(s):
    charList = list(s)
    modified = False

    for i in range(len(s)):
        if charList[i] == "a":
            if modified:
                break
            continue
        
        modified = True
        charList[i] = chr(ord(charList[i]) - 1)
    
    if not modified:
        charList[-1] = chr(ord(charList[-1]) - 1)

    if all(c == "a" for c in s):
        return s
    
    return ''.join(charList)




print(lexi(s))
