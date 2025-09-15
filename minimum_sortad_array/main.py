from typing import List

class Solution:
    def findMin(self, num: List[int]) -> int:
        l, r = 0, len(num) - 1

        while l < r:
            if num[l] < num[r]:  # subarray is already sorted
                return num[l]

            m = (l + r) // 2
            if num[m] >= num[l]:
                l = m + 1
            else:
                r = m

        return num[l]

