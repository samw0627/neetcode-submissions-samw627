class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        for n in count:
            if count[n] > math.floor(len(nums)/2):
                return n


        