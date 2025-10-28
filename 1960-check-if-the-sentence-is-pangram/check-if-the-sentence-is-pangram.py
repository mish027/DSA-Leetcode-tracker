class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=set('abcdefghijklmnopqrstuvwxyz')
        sentence.lower()
        if len(set(sentence))==26:
            return True
        return False