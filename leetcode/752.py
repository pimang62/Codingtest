'''
[Open the Lock]
turn '9' to be '0', or '0' to be '9'
initially starts at '0000'
deadends, the wheels of the lock will stop

"minimum" total number of turns
-1 if it is impossible.
'''
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0  # direct
        if "0000" in deadends:
            return -1

        q = deque([("0000", 0)])  # now_dial, turn_time
        visited = set("0000")
        
        while q:
            now_dial, turn_time = q.popleft()
            if now_dial == target:
                return turn_time

            for i in range(4):
                for bandit in [+1, -1]:  # control
                    tmp = (int(now_dial[i]) + bandit) % 10  # 0 to 9 or 9 to 0
                    nxt_dial = now_dial[:i] + str(tmp) + now_dial[i+1:]
                    if nxt_dial not in visited and nxt_dial not in deadends:
                        visited.add(nxt_dial)
                        q.append((nxt_dial, turn_time+1))
        return -1