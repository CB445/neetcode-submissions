class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store groups of anagrams
        groups = {}

        # Loop through each word in the input list
        for word in strs:
            # Sort the letters to create a unique key for each anagram group
            key = "".join(sorted(word))

            # If this anagram group already exists,
            # add the original word to that group.
            # Otherwise, create a new group.
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        # Return all of the grouped anagrams
        return list(groups.values())

