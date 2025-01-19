class Solution:
    def countSegments(self, s: str) -> int:
        words=s.split()
        no_of_segments=len(words)
        return no_of_segments