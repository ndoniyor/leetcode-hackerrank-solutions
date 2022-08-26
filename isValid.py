
def isValid(s):
    stack = ['.']
    key = {'(' : ')',
           '[' : ']',
           '{' : '}'}
    for i in s:
        if (i == '(' or i=='[' or i=='{'):
            stack.append(key[i])
        elif (i == ')' or i==']' or i=='}'):
            if (stack[-1] == i):
                stack.pop()
            else:
                return False
            
    if len(stack) == 1: return True
    else: return False

print(isValid("(()"))