class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #Create hashmap of the order of the alphabet
        order_map = {}
        idx = 0
        for c in order:
            order_map[c] = idx
            idx += 1

        def compare(s1,s2):
            for a,b in zip(s1,s2):
                print(a,b)
                if a != b:
                    if order_map[a] < order_map[b]:
                        return True
                    else:
                        return False
            #Check for length
            return (len(s1)<=len(s2))

        for i in range(1,len(words)):
            if not compare(words[i-1],words[i]):
                return False
       
        return True
                
                

                    #diyap
                    #disk
                    
                
                
           
            
        

            
            


        