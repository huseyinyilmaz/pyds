pyds
====

Data structure implementations in python


persistentheap
--------------

A persistent heap implementation.

::

   h = None  # empty node
   h = push(h, value) # add value to heap.
   count(h) # get element count of heap.
   (h, poped_value) = pop(h) # remove head and return new heap
