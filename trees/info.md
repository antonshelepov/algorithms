#Trees
##Main characteristics
+ A tree data structure has a root, branches, and leaves
+ the data structure has its root at the top and its leaves on the bottom
+ all the children of one node are *independent* of the children of another node
+ each leaf node is unique
	1. a node is a fundamental part of a tree. It can have a name, which we call the *key*
	2. Additional Information to a node, if provided, is called *payload*
+ Edges:
	1. connects two nodes to represent a relationship between them
	2. every node ( **except the root** ) is connected by exactly one incoming edge from another edge
	3. each node may have several outgoing edges
+ *Path* is an ordered list of nodes that are connected by edges
+ *subtree* is a set of nodes and edges comprised of a parent and all the descendants of that parent
+ a *lead node* is a node that has no children
+ *level* of a node **'n'** is the number of edges on the path from the root node to n
+ if each node in the tree has a max of two children, then it is called **binary tree**
## Examples
+ **File system** is an example of a tree
+ webpage -> on top is html, which is then divided into *head* and *body*
