class Solution(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        t_stack = []
        for char in s:
            if char != '#':
                s_stack.append(char)
            elif s_stack:
                s_stack.pop()
        for char in t:
            if char != '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()
        return ''.join(s_stack) == ''.join(t_stack)

