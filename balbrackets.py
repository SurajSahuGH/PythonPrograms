##def is_balanced(s):
##    stack = []
##    mapping = {")": "(", "]": "[", "}": "{"}
##    for char in s:
##        if char in mapping.values():
##            stack.append(char)
##        elif char in mapping.keys():
##            if not stack or stack.pop() != mapping[char]:
##                return False
##    return not stack
##
##print(is_balanced('()[]{}'), \
##      is_balanced('{[()]}'), \
##      is_balanced('()[[[]'), \
##      is_balanced('()))'), \
##      is_balanced(''))


def is_balanced_par(st):
    stack = []
    for s in st:
        if s == '(':
            stack.append(s)
        elif not stack:
            return False
        elif s == ')':
            stack.pop()
    return not stack

print(is_balanced_par('()))'))#, \
##      is_balanced_par('((()))'), \
##      is_balanced_par('(()'), \
##      is_balanced_par(')'), \
##      is_balanced_par('('), \
##      is_balanced_par(''))

def req_para_for_balancing(st):
    stack = []
    counter=0
    for s in st:
        if s == '(':
            stack.append(s)
        elif not stack:
            counter+=1
        elif s == ')':
            stack.pop()
    return counter+len(stack)




