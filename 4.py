class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

# Example usage:
s1 = "()"
s2 = "()[]{}"
s3 = "(]"

# Using the Solution class
solution_instance = Solution()
print(solution_instance.isValid(s1))  # Output: True
print(solution_instance.isValid(s2))  # Output: True
print(solution_instance.isValid(s3))  # Output: False

