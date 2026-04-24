class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for n in range(len(nums)-1,-1,-1):
            nextDP = set()
            for s in dp:
                nextDP.add(nums[n]+s)
                nextDP.add(s)
                if target in nextDP:
                    return True
            dp = nextDP
        return False
        