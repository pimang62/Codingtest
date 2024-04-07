'''
[Valid Parenthesis String]
three types of characters: '(', ')' and '*'
return true if s is valid

'*' could be treated as a single ['(' or ')' or '']

1 <= s.length <= 100

- '(' : left+1, right+1
- ')' : left-1, right-1
- '*' : 
    left > 0: treat ')' left-1, 
    right-1 => right < 0 break
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
                right += 1  # 뒤에서 빼져야 함 
            elif s[i] == ')':
                left -= 1
                right -= 1  # ')'이 나오면 빼짐
            else:  # == '*'
                left -= 1
                right += 1
            if right < 0:  # ')'이 너무 많이 나왔단 소리
                return False
            left = max(0, left)  # 0: '' 취급, left: ')' 취급

        return left == 0


# Other Solution : with stack
class Solution:
    def checkValidString(self, s: str) -> bool:
        o_stack = []
        s_stack = []

        for index, char in enumerate(s):
            if char == '(':
                o_stack.append(index)
            elif char == ')':
                if o_stack:
                    o_stack.pop()
                elif s_stack:
                    s_stack.pop()
                else:
                    return False
            else:
                s_stack.append(index)

        while o_stack and s_stack:
            if o_stack.pop() > s_stack.pop():
                return False

        return not o_stack