==============
Choosing Boxes 
==============

You're given three boxes with values 17, 21, and 19.

Write a QUBO and an Ocean program that returns the pair of boxes with the 
smallest sum.  A starter file has been provided for you in 
``choosing_boxes.py``.

**Remember:**

You will need to choose a value for your Lagrange parameter and chain strength.

*For students in class submitting to our autograder:*

Please index boxes 17, 21, and 19, using 0, 1, and 2, respectively, in your Q 
dictionary.  In other words, the coefficient on the linear term for Box 17 
should be placed in the (0,0) position in the dictionary (Q[(0,0)]).
