class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mini_dis=nums[0]
        for i in nums:
            if abs(i)<abs(mini_dis):
                mini_dis=i
        return abs(mini_dis) if mini_dis<0 and abs(mini_dis) in nums else mini_dis
        