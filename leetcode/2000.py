'''
[Reverse Prefix of Word]
0-indexed string `word`, character `ch`
reverse the segment of word, 0 and ends at the index of the "first" occurrence of `ch`
'''
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)  # end index
        return word[0:idx+1][::-1] + word[idx+1:]