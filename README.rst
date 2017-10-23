Hell Triangle Challenge Solution
================================

The Problem
-----------

The challenge proposed a problem in which one would receive a 'triangle' list defined by a list of list of integers,
and after that, the program should deliver the maximum sum regarding a rule in which we take a triangle and walk
through it, add its first element to a sum and, by choosing the largest neighbor below this initial element, and walk
on doing the same thing until we reach the end of the triangle.

So a triangle that looks like

``   6``

``  3 5``

`` 9 7 1``

``4 6 8 4``

would be defined as the argument of this max_sum_triangle method

>>> max_sum_triangle([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]])

and then would return **6 + 5 + 7 + 8 = 26** as its answer.

Proposed Solution
-----------------

The solution was to iterate through the triangle list such that for i-th position we working on, the two possible next
neighbors below can only be the *i*-th and *(i + 1)*-th item of the next line. We then choose which neighbor is the
largest and we took its index for the next iteration. Finally, out the for-loop, we take the final index and add its
element to our sum, returning it.

PS: We also have a special case for empty triangles, in which we return zero so as we keep the neutral property of sum.
