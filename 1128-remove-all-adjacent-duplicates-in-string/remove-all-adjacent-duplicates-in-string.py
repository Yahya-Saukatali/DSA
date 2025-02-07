class Solution:
    def removeDuplicates(self, s: str) -> str:
        s_stack = []
        for char in s:
            if s_stack and s_stack[-1] == char:
                s_stack.pop()
            else:
                s_stack.append(char)
        return ''.join(s_stack)
