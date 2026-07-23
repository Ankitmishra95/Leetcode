# 852. Peak Index in a Mountain Array
# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 0
        high = n-1

        ans = -1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] < arr[mid+1]:
                low = mid+1

            else:
                ans = mid
                high = mid-1

        return ans