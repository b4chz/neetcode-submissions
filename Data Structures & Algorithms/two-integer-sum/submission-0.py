class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Loop through each element index i
        for i in range(len(nums)):
            # Loop through all elements after i to avoid duplicate pairs and self-matching
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

