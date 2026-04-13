"""
Problem: Caregiver worked shifts: [8, 6, 7, 5]. Calculate total hours recursively.

Base Case
Breakdown into Small problems
- last number + curr -> nums[i+1:]
Combine

[8, 6, 7, 5]

total_hours[6,7,5] + 8 
total_hours[7,5] + 6 + 8
total_hours[5] + 7 + 6 + 8 -> 


"""

def total_hours(nums):
    if not nums:
        return 0
    
    return nums[0] + total_hours(nums[1:])


"""
Nested Array Sum

1. Base Case - Empty case
2. Decision using a smaller problem. Or Simple case
3. Recurse function

arr = [1, [2, 3], [4, [5]], 6]

Decison with simpler case 

arr = [1, [2, [3]]]

"""

def nested_sum_array(arr):
    total_sum = 0

    for elem in arr:
                
        if isinstance(elem, int):
            total_sum += elem
        else:
            total_sum += nested_sum_array(elem)
        
    return total_sum

# arr = [1, [2, 3], [4, [5]], 6]
# print(nested_sum_array(arr))


"""
 Implement factorial(n) which returns n!

Base Case
Decision
recursion

Base case: is return 1
global variable
smaller problem is 2! - 2 * 1

How is the stack call trace for 5!?

2 * fact(1) -> 2
3 * fact(2) -> 6
4 * fact(3) -> 24
5 * fact(4) -> 120

recursion directly

"""

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))


"""

"""


