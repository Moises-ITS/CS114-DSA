'''
You're building a sensor monitoring system. Given an array of sensor readings, return all readings that are anomalous — defined as any value strictly greater
 than twice the average of all readings. Important: The average must be computed using integer arithmetic only (no floats). To avoid float precision bugs, 
 the comparison must be done by rearranging the inequality so that no division ever occurs during the threshold check.
'''

#1. Input is an array of non-negative integers with lengths of n (1 <= n <= 10^5)
#2. Values range [0, 10^6]
#3. Output must be a list of all values strictly greater than 2 * average(readings), in the order they appear

#threshold = 2*sum(arr)
#threshold * n > 2 * sum(arr)
input = [3,3,3,100]

def anomaly(x):
    n = len(x)
    avg = sum(x)
    res = []
    for value in x:
        if value * n > avg * 2:
            res.append(value)
    return res
        


print(anomaly(input))