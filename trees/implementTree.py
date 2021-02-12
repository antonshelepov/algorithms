def Binarytree(r):
    return [r, [], []]

def insertLeft(root,newBranche):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch,t,[]])
    else:
        root.insert(1, [newBranche, [], []])
    return root


def insertRight(root,newBranche):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch,t,[]])
    else:
        root.insert(2, [newBranche, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
