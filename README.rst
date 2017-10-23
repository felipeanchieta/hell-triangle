Hell Triangle Challenge Solution
================================

.. image:: https://travis-ci.org/felipeanchieta/hell-triangle.svg?branch=master
    :target: https://travis-ci.org/felipeanchieta/hell-triangle

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

would be defined as the argument of this max_sum_triangle function call:

>>> max_sum_triangle([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]])
26

and then would return **6 + 5 + 7 + 8 = 26** as its answer.

Proposed Solution
-----------------

The proposed solution was to use a recursive strategy, as the functional approach seems to be the most elegant. As
Python 3 is one of the languages that I know best, it was chose to work out the solution.

It has been developed a function in which we treat two special cases: empty triangle, which returns zero, and the case
of a triangle with one line, which returns its only element. The recursive case choose which neighbor, the left one or
the right one, is the largest and then recursively call the auxiliary inner function passing the tail of the triangle
list, an updated summation and the chosen index.
