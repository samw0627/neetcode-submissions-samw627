from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each word
        anagram_array = []
        for word in strs:
            anagram = "".join(sorted(word))
            anagram_array.append(anagram)
        
        
        #create a hashmap with {"anagram": [list,of,words]}
        anagram_dict = {}
        #if word is anagram, of key, then add it to the list of words
        for n,anagram in enumerate(anagram_array):
            #Check if the key exist:
            if anagram not in anagram_dict:
                anagram_dict[anagram]= [strs[n]]
            else:
                anagram_dict[anagram].append(strs[n])
        
        return list(anagram_dict.values())
        #if does not match