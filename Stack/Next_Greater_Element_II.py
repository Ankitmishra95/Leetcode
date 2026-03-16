# 503. Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

class Solution:
    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        arr += arr
        n = len(arr)

        ans = [0]*n
        st = []

        for i in range(n-1,-1,-1):
            while len(st)>0 and st[-1]<=arr[i]:
                st.pop()
            if len(st) == 0:
                ans[i]= -1
            else:
                ans[i] = st[-1]
            st.append(arr[i])

        return ans[:len(ans)//2]