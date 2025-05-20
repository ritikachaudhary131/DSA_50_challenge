class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''

        if len(word1) == len(word2):
            for i in range(len(word1)):
                answer = answer + word1[i] + word2[i]
        else:
            min_length = min(len(word1), len(word2))
            for i in range(min_length):
                answer = answer + word1[i] + word2[i]

            leftover = word1[min_length:] + word2[min_length:]
            answer = answer + leftover
            
        return answer

        
        