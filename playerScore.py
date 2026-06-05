'''
You're building a matchmaking system. Given an array of player scores, find all pairs of players whose combined score hits exactly a target
rating needed to unlock a ranked match. Return the indices of each valid pair. Each player can only be used once per pair, and order doesn't 
matter — (i, j) is the same as (j, i).

Example:

Input = [30,70,50,20,80], target = 100

Output = [(0,1), (3,4)]
'''

Input, target = [30, 30, 70], 100

def playerScore(input: list, target: int):
    mapped = {}
    output = []
    for index, num in enumerate(input):
        total = target - num
        if total in mapped:
            for pastIndex in mapped[total]:
                output.append((pastIndex, index))
        mapped[num] = mapped.get(num, []) + [index]
    return  output


print(playerScore(Input, target))

