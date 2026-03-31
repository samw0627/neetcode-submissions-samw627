class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def dfs(currSet,open_paren, close_paren):
            #Base Case: When the string reaches the right length
            if len(currSet) == 2*n:
                    s="".join(currSet)
                    final.append(s)
                    return
            
            if open_paren < n:
                currSet.append("(")
                dfs(currSet,open_paren+1, close_paren)
                currSet.pop()
            if close_paren < open_paren:
                currSet.append(")")
                dfs(currSet, open_paren, close_paren+1)
                currSet.pop()

        dfs([],0,0)
        return final




        