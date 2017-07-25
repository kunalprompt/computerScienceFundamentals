# HEAP Data Structure Implementation

A heap is a binary tree (in which each node contains a Comparable key value), with two special properties:

1. The **ORDER** property:

    For every node n, the value in n is greater than or equal to the values in its children
    (and thus is also greater than or equal to all of the values in its subtrees).


2. The **SHAPE** property:

    1. All leaves are either at depth d or d-1 (for some value d).

    2. All of the leaves at depth d-1 are to the right of the leaves at depth d.

    3. (a) There is at most 1 node with just 1 child.

        (b) That child is the left child of its parent, and

        (c) it is the rightmost leaf at depth d.


Here are some binary trees, some of which violate the shape properties, and some of which respect those properties:

<img width="784" alt="heap trees"
src="https://user-images.githubusercontent.com/6684615/28576198-d13b1f9a-7170-11e7-9f53-5388df1c7710.png">


And here are some more trees; they all have the shape property, but some violate the order property:

<img width="588" alt="heap trees"
src="https://user-images.githubusercontent.com/6684615/28576317-4255aa38-7171-11e7-9a56-094f7f30bee0.png">


**References**

* http://pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html

**Images**

Images are also present in this directory for reference.
