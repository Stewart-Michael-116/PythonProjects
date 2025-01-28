class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_string = ""
        
        # get max length
        max_length = len(word1)
        if len(word2) > max_length:
            max_length = len(word2)
        
        for i in range(max_length):
            if len(word1)-1 >= i:
                combined_string += word1[i]
            if len(word2)-1 >= i:
                combined_string += word2[i]
        
        return combined_string
        
