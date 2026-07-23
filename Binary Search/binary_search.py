# 704. Binary Search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0 
        j = n-1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                i = mid + 1

            elif nums[mid] > target:
                j = mid - 1

        return -1