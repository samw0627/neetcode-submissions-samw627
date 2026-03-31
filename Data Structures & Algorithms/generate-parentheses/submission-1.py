class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def paren(open_count, close_count,currSet):
            #Pruning: If at the end of the 
            #Pruning: 
            if open_count == n and close_count == n:
                string = "".join(currSet)
                final.append(string)
                return
            
            if open_count < close_count:
                return
            
            if open_count < n:
                currSet.append("(")
                paren(open_count+1, close_count, currSet)
                currSet.pop()
            if close_count < n:
                currSet.append(")")
                paren(open_count, close_count+1, currSet)
                currSet.pop()
        paren(0,0,[])
        return final




         

        