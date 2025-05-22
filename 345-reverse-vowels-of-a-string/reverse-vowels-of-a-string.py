class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # string ko list me convert kiya (taaki modify kar sakein)
        vowels = "aeiouAEIOU"
        
        i, j = 0, len(s) - 1  # do pointer banaye: start aur end se

        while i < j:
            # agar s[i] vowel nahi hai, toh aage badho
            if s[i] not in vowels:
                i += 1
            # agar s[j] vowel nahi hai, toh peeche jao
            elif s[j] not in vowels:
                j -= 1
            # dono vowels mil gaye, swap kar do
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return "".join(s)  # list ko dubara string bana ke return
