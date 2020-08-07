#Given n string of brackets, determine whether each sequence of brackets is
#balanced. If string is balanced, return YES, otherwise return NO.

def check_balanced_paranthesis(string):
    d={'{':'}','[':']','(':')'}
    stack=[]
    for char in string:
        if char in d:
            stack.append(char)
        else:
            if not stack:
                return 'NO'
            elif char==d[stack[-1]]:
                stack.pop()
            else:
                return 'NO'
    return 'YES' if not stack else 'NO'

t=int(input())
while t:
    print(check_balanced_paranthesis(input()))
    t-=1

