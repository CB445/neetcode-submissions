class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # If it is a number, add it to the stack
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            # Otherwise, use the last two numbers
            else:
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                else:
                    # int() makes division truncate towards zero
                    result = int(left / right)

                # Store the result for the next operation
                stack.append(result)

        return stack[0]