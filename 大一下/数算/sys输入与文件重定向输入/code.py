import sys
lines = [line.rstrip('\n') for line in sys.stdin]

class node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.lc = None
        self.rc = None

stack = []
root = None

def comprehend(s):
    depth = 0
    for i in s:
        if i == '\t':
            depth += 1
        else:
            return (i, depth)
        
for i in lines:
    s = i
    s, depth = comprehend(s)
    new = node(s)
    while stack:
        if stack[-1][1] >= depth:
            stack.pop()
        else:
            break
    if stack:
        if s !='*':
            new.parent = stack[-1][0]
            if stack[-1][0].lc != None:
                stack[-1][0].rc = new
            else:
                stack[-1][0].lc = new
            stack.append((new, depth))
        else:
            stack[-1][0].lc = '*'
    else:
        root = new
        stack.append((new, 0))

def preord(root):
    if root == None or root == '*':
        return ''
    return root.val + preord(root.lc) + preord(root.rc)

def inord(root):
    if root == None or root == '*':
        return ''
    return inord(root.lc) + root.val + inord(root.rc)

def postord(root):
    if root == None or root == '*':
        return ''
    return postord(root.lc) + postord(root.rc) + root.val 


print(preord(root))
print(inord(root))
print(postord(root))