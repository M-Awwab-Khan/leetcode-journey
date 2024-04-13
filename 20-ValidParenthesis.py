class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = -1
        for char in s:
            if char in '({[':
                stack.append(char)
                i += 1
            else:
                try:
                    if char == ')' and stack[i] == '(':
                        stack.pop()
                    elif char == '}' and stack[i] == '{':
                        stack.pop()
                    elif char == ']' and stack[i] == '[':
                        stack.pop()
                    else:
                        return False

                except IndexError:
                    return False
                i -= 1
        if stack:
            return False
        return True


