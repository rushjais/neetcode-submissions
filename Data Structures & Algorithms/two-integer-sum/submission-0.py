class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i and j set to 0 and 1
        # run a for loop for i to go till len-1
        # run a while loop to go to len-1 until i+j = target
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        