from setuptools import setup
# from distutils.core import setup


with open('README.rst') as _f:
    _README_RST = _f.read()

_VERSION = '0.2'


setup(
    name='conv',
    version=_VERSION,
    description='A lightweight library to do for-loop-styled convolution '
                'passes on your iterable objects (e.g.: on a list).',
    long_description=_README_RST,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        'Intended Audience :: Information Technology',
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    url='https://github.com/guillaume-chevalier/python-conv-lib',
    download_url='https://github.com/guillaume-chevalier/python-conv-lib/tarball/{}'.format(_VERSION),
    author='Guillaume Chevalier',
    author_email='guillaume-chevalier@outlook.com',
    packages=['conv'],
    test_suite="testing",
    tests_require=["pytest", "pytest-cov"],
    include_package_data=True,
    license='MIT',
    keywords='convolution conv conv1d conv2d convolve convolved'
)
