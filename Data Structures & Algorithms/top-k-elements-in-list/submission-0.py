class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Build a hasmap of frequency with entry
        nums_freq = Counter(nums)
        sorted_freq = dict(sorted(nums_freq.items(), key=lambda item: item[1], reverse = True))
        first_k_keys = list(sorted_freq.keys())[:k]
        return first_k_keys



        