from distutils.core import setup
from setuptools import Extension  # , setup
from Cython.Build import cythonize

extensions = [
    Extension(name="Brain", sources=["Brain.pyx"])
]

setup(
    name="Brain",
    ext_modules=cythonize('Brain.pyx')
)
# setup(ext_modules=cythonize(['Neuron.pyx'])) #, "Brain.pyx"]))


# run this in terminal:

# python setup.py build_ext --inplace
