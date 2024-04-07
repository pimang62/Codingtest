'''
[Minimum Remove to Make Valid Parentheses]
string s of '(' , ')' and lowercase
remove the minimum number of "parentheses"

- empty string
- written as AB
- written as (A)

1 <= s.length <= 10**5
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # '(' or ')'
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((i, '('))  # index, type
            elif s[i] == ')':
                if stack and stack[-1][1] == '(':  # s[i] == ')'
                    stack.pop()
                else:
                    stack.append((i, ')'))

        answer = ''
        for i in range(len(s)):
            if stack and i == stack[0][0]:  # the one that should removed
                stack.pop(0)
            else:
                answer += s[i]
        return answer

# Other Solution : with stack
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_count = 0
        right_count = 0
        stack = []

        # Pass 1
        for ch in s:
            if ch == '(':
                left_count += 1
            elif ch == ')':
                right_count += 1
            if right_count > left_count:
                right_count -= 1
            else:
                stack.append(ch)

        result = ""

        # Pass 2
        while stack:
            current_char = stack.pop()
            if left_count > right_count and current_char == '(':
                left_count -= 1
            else:
                result += current_char

        # Reverse the result string
        return result[::-1]

