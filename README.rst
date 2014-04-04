python data structures
======================

Data structure implementations in python


persistentheap
--------------

A persistent heap implementation.

::

   h = None  # empty node
   h = push(h, value) # add value to heap.
   count(h) # get element count of heap.
   (h, poped_value) = pop(h) # remove head and return new heap


persistentbst
-------------

A persistend binary search tree implementation.

::

   t = None # empty node
   t = push(t, value) # add value to bst
   t = count(t) # get element count of tree.
   (t, poped_value) = pop(t, val) # remove a value from tree
   contains(t, value) # returns True if tree contains given value
