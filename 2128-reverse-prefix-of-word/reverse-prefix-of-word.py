class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: #nahi h toh aesi return krdo
            return word
        idx = word.index(ch)#character ka index word k andr 
        return word[:idx+1][::-1] + word[idx+1:]
        #index+1 tk ka part reverse krdo + aage ka word same rkhdo