class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned = ""

        #removes spaces and punctuation as well as changing everythning to lower case
        for character in s:
            if character.isalnum():
                cleaned += character.lower()

        #reverses string
        reversed_string = cleaned[::-1]

        return cleaned == reversed_string