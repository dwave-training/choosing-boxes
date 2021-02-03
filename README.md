# Choosing Boxes

You're given three boxes with values 17, 21, and 19.

Write a QUBO and an Ocean program that returns the pair of boxes with the
smallest sum.  A starter file has been provided for you in
``choosing_boxes.py``.

**Remember:**

You will need to choose a value for your Lagrange parameter and number of QPU
reads.  The autograder will test if your Lagrange parameter is large enough
that the desired solution (boxes 17 and 19) has the smallest value.

*For students in class submitting to our autograder:*

Please index boxes 17, 21, and 19, using 0, 1, and 2, respectively, in your Q
dictionary.  For example, if the coefficient on the linear term for Box 17
is 5, your program will assign `Q[(0,0)]=5`.

## Instructions

To write your program, please complete the following in `choosing_boxes.py`:

- Add your token to the ``get_token`` function.
- Fill in the entries in your QUBO dictionary in the ``get_qubo`` function, and
  set the Lagrange parameter.
- Find a good value ``numruns`` in the ``run_on_qpu`` function
- Complete the main function (bottom of the file) by defining a sampler,
  running your problem on that sampler, and looking at the results.  "Looking
at the results" may be as simple as printing out the sampleset object - it's up
to you!
