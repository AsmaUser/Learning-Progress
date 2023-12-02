#class Solution(object):
def two_sum(nums, target):
    # Iterate through each element in the list
    for i in range(len(nums)):
        # Check if the complement of the current element exists in the rest of the list
        complement = target - nums[i]
        if complement in nums[i + 1:]:
            # If found, return the indices of the two elements
            return [i, nums.index(complement, i + 1)]

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)