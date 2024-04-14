import sys
sys.set_int_max_str_digits(10000000)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):  # except
            return '0'

        stack = []
        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        if k > 0:
            # the last one is the biggest one
            stack = stack[:-k]

        # while k > 0:
        #     stack.pop()
        #     k -= 1

        answer = ''.join(stack).lstrip('0')  # faster than str(int())

        return answer if answer else "0"