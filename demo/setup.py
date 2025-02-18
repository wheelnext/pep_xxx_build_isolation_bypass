from setuptools import setup

from torch.utils.cpp_extension import CppExtension

# Find an artificial reason to use a non default package
from pybind11.commands import get_include as pybind11_include

setup(
    ext_modules=[
        CppExtension(
            'hello.ext',
            ['src/hello.c'],
            depends=['src/hello.h'],
            include_dirs=['src', pybind11_include()]
        )
    ],
)