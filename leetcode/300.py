'''
[Longest Increasing Subsequence]
stack = []

if not stack or stack[-1]이 나보다 작으면 
    - append  # [2, ] <- 5 or 2
    - continue
while stack and stack[-1]이 나보다 크면 
    - pop  # [..., 7, (101)] <- 18 or 101
    - append

ex2. nums = [0,1,0,3,2,3]
stack = [(0, 1), 0, 2, 3] -> Nooooo!!

hint. O(n log(n))
'''
# class Solution:  # not fit in ex2!!
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         stack = []
#         answer = 0  # len
#         for i in range(len(nums)):
#             tmp = nums[i]
#             if not stack or stack[-1] < tmp:
#                 stack.append(tmp)
#                 answer = max(answer, len(stack))
#                 print(stack)
#             while stack and stack[-1] >= tmp:
#                 stack.pop()
#             stack.append(tmp)
#         return answer

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = [1]*len(nums)
        answer = 1  # maximum
        for i in range(len(nums)):  # [0, 1, 2, ..]
            for j in range(i, -1, -1):  # [0, 1] <- reverse
                if nums[j] < nums[i]:  
                    d[i] = max(d[i], d[j]+1)  # d{1}:2, d{0}:1, ..
                    answer = max(answer, d[i])
        return answer