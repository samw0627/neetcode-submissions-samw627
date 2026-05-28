class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = []
        for d in digits:
            string.append(str(d))
        s = "".join(string)
        num = int(s) + 1
        ans = [int(d) for d in str(num)]
        return ans
        