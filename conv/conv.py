"""A module to loop on iterables, with convolutional style."""

__author__ = "Guillaume Chevalier"
__license__ = """
MIT License

Copyright (c) 2018 Guillaume Chevalier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
__contributing__ = """
By contributing to this repository, you agree to donate your code to
Guillaume Chevalier for your code to be licensed under the MIT license's
terms. See the LICENSE file. By opening a pull request on GitHub,
your contributions should remain visible there online:
https://github.com/guillaume-chevalier/python-conv-lib
"""


def convolved(iterable, kernel_size=1, stride=1, padding=0, default_value=None, include_incomplete_pass=False):
    """Iterable to get every convolution window per loop iteration.

    For example:
        `convolved([1, 2, 3, 4], kernel_size=2)` 
            will produce the following result:
            `[[1, 2], [2, 3], [3, 4]]`.
        `convolved([1, 2, 3], kernel_size=2, stride=1, padding=2, default_value=42)` 
            will produce the following result:
            `[[42, 42], [42, 1], [1, 2], [2, 3], [3, 42], [42, 42]]`

    Arguments:
        iterable: An object to iterate on. It should support slice indexing if `padding == 0`.
        kernel_size: The number of items yielded at every iteration.
        stride: The step size between each iteration.
        padding: Padding must be an integer or a string with value `SAME` or `VALID`. If it is an integer, it represents
            how many values we add with `default_value` on the borders. If it is a string, `SAME` means that the
            convolution will add some padding according to the kernel_size, and `VALID` is the same as
            specifying `padding=0`.
        include_incomplete_pass: suppose you have a kernel_size of 7 and an iterable length of 3. If
            include_incomplete_pass is set to True, then you'll have 1 item returned in the loop, otherwise, 0 item.
        default_value: Default fill value for padding and values outside iteration range.
    """
    # Input validation and error messages
    if not hasattr(iterable, '__iter__'):
        raise ValueError(
            "Can't iterate on object.".format(
                iterable))
    if stride < 1:
        raise ValueError(
            "Stride must be of at least one. Got `stride={}`.".format(
                stride))
    if not (padding in ['SAME', 'VALID'] or type(padding) in [int]):
        raise ValueError(
            "Padding must be an integer or a string with value `SAME` or `VALID`.")
    if not isinstance(padding, str):
        if padding < 0:
            raise ValueError(
                "Padding must be of at least zero. Got `padding={}`.".format(
                    padding))
    else:
        if padding == 'SAME':
            padding = kernel_size // 2
        elif padding == 'VALID':
            padding = 0
    if not type(iterable) == list:
        iterable = list(iterable)  # TODO: don't cast as list. Chain iter or something like that instead.

    # Add padding to iterable
    if padding > 0:
        pad = [default_value] * padding
        iterable = pad + list(iterable) + pad  # TODO: don't cast as list. Chain iter or something like that instead.

    # Fill missing value to the right
    remainder = (kernel_size - len(iterable)) % stride
    extra_pad = [default_value] * remainder
    iterable = iterable + extra_pad

    i = 0
    has_passed_once = False
    while True:
        # If not the end or not the end but
        if i > len(iterable) - kernel_size:
            if not include_incomplete_pass or has_passed_once:
                break

            if i < len(iterable):
                has_passed_once = True
            else:
                break

        yield iterable[i:i + kernel_size]
        i += stride


def convolved_1d(iterable, kernel_size=1, stride=1, padding=0, default_value=None, include_incomplete_pass=False):
    return convolved(iterable, kernel_size, stride, padding, default_value, include_incomplete_pass)


def dimensionize(maybe_a_list, nd=2):
    if not hasattr(maybe_a_list, '__iter__'):
        # Argument is probably an integer so we map it to a list of size `nd`.
        now_a_list = [maybe_a_list] * nd
        return now_a_list
    else:
        # Argument is probably an `nd`-sized list.
        return maybe_a_list


def convolved_2d(iterable, kernel_size=1, stride=1, padding=0, default_value=None, include_incomplete_pass=False):
    # return range(10)
    kernel_size = dimensionize(kernel_size, nd=2)
    stride = dimensionize(stride, nd=2)
    padding = dimensionize(padding, nd=2)

    for row_packet in convolved(iterable, kernel_size[0], stride[0], padding[0], default_value,
                                include_incomplete_pass):
        transposed_inner = []
        for col in tuple(row_packet):
            transposed_inner.append(list(
                convolved(col, kernel_size[1], stride[1], padding[1], default_value, include_incomplete_pass)
            ))

        if len(transposed_inner) > 0:
            for col_i in range(len(transposed_inner[0])):
                yield tuple(row_j[col_i] for row_j in transposed_inner)


def convolve_nd(iterable, *kargs, **kwargs):
    raise NotImplementedError(
        "You might want to open a pull request on GitHub "
        "and donate your implementation. The code could "
        "also be more optimized. Thanks for contributing!"
    )
