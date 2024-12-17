class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        last_word=words[-1]
        return len(last_word)

        