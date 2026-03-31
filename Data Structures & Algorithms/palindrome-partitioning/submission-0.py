class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #"aab"
        #"a\ab" 
        #"a\a\b" "aa\b"
        final, part = [], []
        def isPalindrome(string):
            if len(string) == 0:
                return True
            left = 0
            right = len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True


        def dfs(start):
            if start == len(s):
                final.append(part.copy())
                return           
            #if the current slice is a palindrome, add it to part
            for end in range(start,len(s)):
                if not isPalindrome(s[start:end+1]):
                    continue
                part.append(s[start:end+1])    
                dfs(end+1)
                part.pop()

        dfs(0)
        return final     



