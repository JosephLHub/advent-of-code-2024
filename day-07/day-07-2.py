import sys, math
from itertools import combinations_with_replacement
from sympy.utilities.iterables import multiset_permutations
data = sys.stdin.read().split("\n")

operators = ["+", "*", "|"]

total = 0
for x in data:
    valid = False
    target = int(x.split(":")[0])
    nums = x.split(":")[1].strip().split(" ")
    seen = set()
    print(target)
    for operator_combo in combinations_with_replacement(operators, len(nums) - 1):
        for operator in multiset_permutations(operator_combo, len(nums) - 1):
            result = int(nums[0])
            for item in range(len(operator)):
                if operator[item] == "+":
                    result += int(nums[item+1])
                elif operator[item] == "*":
                    result *= int(nums[item+1])
                elif operator[item] =="|":
                    result = int(str(result) + nums[item+1])
            if result == target:
                valid = True
    if valid:
        total += target

print(total)