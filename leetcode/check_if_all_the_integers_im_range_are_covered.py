from typing import List


class Solution:
        def isCovered(self, ranges, left, right):
            diff = [0] * 52
            for l, r in ranges:
                diff[l] += 1
                diff[r + 1] -= 1
            s = 0
            for i, x in enumerate(diff):
                s += x
                if s <= 0 and left <= i <= right:
                    return False
            return True