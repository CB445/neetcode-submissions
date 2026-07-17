class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in s:

            # If it's an opening bracket, add it to the stack
            if bracket in "([{":
                stack.append(bracket)

            # Otherwise it's a closing bracket
            else:

                # No opening bracket to match
                if len(stack) == 0:
                    return False

                # Top of the stack doesn't match
                if stack[-1] != pairs[bracket]:
                    return False

                # Match found, remove opening bracket
                stack.pop()

        # If the stack is empty, everything matched
        return len(stack) == 0