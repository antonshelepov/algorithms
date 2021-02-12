# https://github.com/c0fec0de/anytree
# https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

from anytree import Node, RenderTree

ceo = Node("CEO") #root
vp_1 = Node("VP_1", parent=ceo)
vp_2 = Node("VP_2", parent=ceo)
gm_1 = Node("GM_1", parent=vp_1)
gm_2 = Node("GM_2", parent=vp_2)

for pre, fill, node in RenderTree(ceo):
    print("%s%s" % (pre, node.name))

