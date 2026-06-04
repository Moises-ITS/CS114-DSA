'''
Write a function nanana_batman() that accepts an integer x and prints thr string "nanana batman!" where "na" us repeated x times.

Do not use the * operator
'''
x = 2
def nanana_batman(x: int):

    res = ""
    if x < 0:
        return "error"
    for i in range(x):
        res += "na"
    if res:
        return (res + " Batman!")
    else:
        ("Batman!")


print(nanana_batman(x))