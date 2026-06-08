'''
Cloud Resource Optimizer
IBM is building a cloud resource management system. Each virtual machine (VM) is assigned to a data center, and each VM has an associated hourly cost.
Due to budget constraints, IBM wants to select exactly one VM per data center — specifically the cheapest VM in that data center — and report the total minimum cost across all selected VMs.

Problem
Given a list of VMs where each VM is represented as [datacenterId, cost], return the minimum total cost to operate one VM from each data center.

Input: vms = [[1, 300], [1, 100], [2, 500], [2,200], [3,400]]
Output: 700

'''
def minCost(vms):
    seen = {}
    for i in vms:
        num, power = i
        seen[num] = min(power, seen.get(num, float('inf')))
    return sum(seen.values())

vms = [[1, 300], [1, 100], [2, 500], [2,200], [3,400]]

print(minCost(vms))