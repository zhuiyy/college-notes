class node:
    def __init__(self, val, parent=None):
        self.parent = parent
        self.lchildren = None
        self.rchildren = None
        self.val = val

def rebuild(root_node_key, in_order_list, parent=None, left=True):
    current = node(s1[root_node_key], parent)
    root = False
    if parent:
        if left:
            parent.lchildren = current
        else:
            parent.rchildren = current
    else:
        root = True
    flag = None
    if len(in_order_list) == 1:
        return
    for i in range(len(in_order_list)):
        if in_order_list[i] == s1[root_node_key]:
            flag = i
            break
    if flag == None:
        print(f'there is no \'{s1[root_node_key]}\' in {in_order_list}')
        raise KeyError
    if flag != 0:
        rebuild(root_node_key + 1, in_order_list[:flag:], current)
    if flag != len(in_order_list) - 1:
        rebuild(root_node_key + flag + 1, in_order_list[flag + 1::], current, False)
    if root:
        return current
    return

def postshow(node):
    if not node:
        return
    if not node.lchildren and not node.rchildren:
        print(node.val, end='')
        return
    postshow(node.lchildren)
    postshow(node.rchildren)
    print(node.val, end='')

try:
    while True:
        s1, s2 = input().split()
        root = rebuild(0, s2)
        postshow(root)
        print()
except:
    pass