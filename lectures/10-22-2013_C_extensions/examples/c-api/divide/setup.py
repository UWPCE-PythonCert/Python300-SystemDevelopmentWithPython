from distutils.core import setup, Extension

setup(
    name='Cdiv',
    version='1.0',
    description='Test description',
    ext_modules=[Extension('divide', sources=['divide.c'])],
)

