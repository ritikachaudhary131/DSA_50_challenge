class Solution:
    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num  # original list me valid element daal rahe hain
                i += 1         # index badha rahe hain
        return i