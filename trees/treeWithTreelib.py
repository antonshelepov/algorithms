# this is an example of tree implementation using treelib package
# https://treelib.readthedocs.io/en/latest/
# https://medium.com/swlh/making-data-trees-in-python-3a3ceb050cfd

from treelib import Node, Tree

tree = Tree()
tree.create_node("CEO","CEO") #root
tree.create_node("VP_1","VP_1",parent="CEO" )
tree.create_node("VP_2","VP_2",parent="CEO" )
tree.create_node("GM_1","GM_1",parent="VP_1" )
tree.create_node("GM_2","GM_2",parent="VP_2" )
tree.show()
tree.save2file('tree.txt')
