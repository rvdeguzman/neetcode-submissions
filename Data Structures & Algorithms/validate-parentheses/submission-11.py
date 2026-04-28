class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
                print(c)
            elif c in [')', ']', '}']:
                if len(stack) < 1:
                    return False
                a = stack[-1] 
                print('a: ' + str(a))
                print('c: ' + str(c))
                
                if (a == '(' and c == ')') or (a == '[' and c == ']') or (a == '{' and c == '}'):
                    stack.pop()
                else: 
                    return False
                
        if len(stack) == 0:
            return True
        return False
