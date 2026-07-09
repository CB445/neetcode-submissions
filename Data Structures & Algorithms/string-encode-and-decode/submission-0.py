class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
                    length = len(word)
                    encoded += str(length) + "#" + word
        return encoded


    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length
            word = s[word_start:word_end]

            decoded.append(word)
            i = word_end

        return decoded


