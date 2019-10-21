================
conv
================


Description
=============


Conv is a simple Python >= 3 package, lightweight library to do for-loop-styled convolution passes on your iterable objects (e.g.: on a list).


Installation
=============
::

    pip install conv


Example Usage
=============
::

    from conv import convolved


    some_list = [1, 2, 3]
    for kernel_hover in convolved(some_list, kernel_size=2, stride=1, padding=2, default_value=42):
        print(kernel_hover)

Result:
----------
::

    [42, 42]
    [42, 1]
    [1, 2]
    [2, 3]
    [3, 42]
    [42, 42]

Unit Tests:
-----------
::

    python setup.py test

A ``convolved_2d`` function also exists. See tests for more examples.


Notes
=============


License: MIT

Author: Guillaume Chevalier
