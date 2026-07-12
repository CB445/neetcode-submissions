class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        #only begin counting if num starts a sequance
        for num in numbers:
            if num - 1 not in numbers:
                current_num = num
                current_length = 1

            # continue throught consecutive numbers
                while current_num + 1 in numbers:
                    current_num += 1
                    current_length += 1

            #save the longest sequence found
                longest = max(longest, current_length)

        return longest