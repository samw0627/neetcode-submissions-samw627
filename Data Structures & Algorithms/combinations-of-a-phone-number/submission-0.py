class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        #Create mapping for each of the digits:
        mapping = {}
        mapping[2] = ["a","b","c"]
        mapping[3] = ["d","e","f"]
        mapping[4] = ["g","h","i"]
        mapping[5] = ["j","k","l"]
        mapping[6] = ["m","n","o"]
        mapping[7] = ["p","q","r","s"]
        mapping[8] = ["t","u","v"]
        mapping[9] = ["w","x","y","z"]

        final = []
        def dfs(currString,index):
            if index == len(digits):
                if len(currString) != 0:
                    s = "".join(currString.copy())
                    final.append(s)
                return

            entry = mapping[int(digits[index])]
            for n in range(len(entry)):
                #For each entry in the current mapping
                currString.append(entry[n])
                dfs(currString,index+1)
                currString.pop()
        
        dfs([],0)
        return final
                

                



        