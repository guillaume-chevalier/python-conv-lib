"""A module to loop on iterables, with convolutional style."""

def convolved(iterable, kernel_size=1, stride=1, padding=0, default_value=None):
    """Iterate on an iterable so as to get every convolution window per loop iteration.

    For example, `convolved([1, 2, 3, 4], kernel_size=2)` will produce the following result: `[1, 2], [2, 3], [3, 4]`.

    Arguments:
        iterable: An object to iterate on. It should support slice indexing if `padding == 0`.
        kernel_size: The number of items yielded at every iteration.
        stride: The step size between each iteration.
        padding: Padding must be an integer or a string with value `SAME` or `VALID`. If it is an integer, it represents
            how many values we add with `default_value` on the borders. If it is a string, `SAME` means that the
            convolution will add some padding according to the kernel_size, and `VALID` is the same as
            specifying `padding=0`.
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
        iterable = list(iterable)

    # Add padding to iterable
    if padding > 0:
        pad = [default_value] * padding
        iterable = pad + list(iterable) + pad

    # Fill missing value to the right
    remainder = (kernel_size - len(iterable)) % stride
    extra_pad = [default_value] * remainder
    iterable = iterable + extra_pad

    i = 0
    while True:
        if i > len(iterable) - kernel_size:
            break
        yield iterable[i:i + kernel_size]
        i += stride


def convolved_1d(iterable, kernel_size=1, stride=1, padding=0, default_value=None):
    return convolved(iterable, kernel_size, stride, padding, default_value)


def dimensionize(maybe_a_list, nd=2):
    if not hasattr(maybe_a_list, '__iter__'):
        # Argument is probably an integer so we map it to a list of size `nd`.
        now_a_list = [maybe_a_list] * nd
        return now_a_list
    else:
        # Argument is probably an `nd`-sized list.
        return maybe_a_list


def convolved_2d(iterable, kernel_size=1, stride=1, padding=0, default_value=None):
    kernel_size = dimensionize(kernel_size, nd=2)
    stride = dimensionize(stride, nd=2)
    padding = dimensionize(padding, nd=2)
    final_list = []

    for row_packet in convolved_1d(iterable, kernel_size[0], stride[0], padding[0], default_value):
        transposed_inner = []
        for col in tuple(row_packet):
            transposed_inner.append(list(convolved_1d(iterable, kernel_size[1], stride[1], padding[1], default_value)))

        if len(transposed_inner) > 0:
            for col_i in range(len(transposed_inner[0])):
                yield tuple(row_j[col_i] for row_j in transposed_inner)


def convolve_nd(iterable, *kargs, **kwargs):
    raise NotImplementedError(
        "You might want to open a pull request on GitHub "
        "and donate your implementation. The code could "
        "also be more optimized. Thanks for contributing!"
    )
