from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyglatin',
    version='1.0',
    description='Convert English to Pig Latin',
    long_description=long_description,
    url='https://github.com/amake/pyglatin',
    author='Aaron Madlon-Kay',
    author_email='aaron@madlon-kay.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Pre-processors',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='conversion',
    py_modules=['pyglatin'],
    entry_points={
        'console_scripts': [
            'pyglatin=pyglatin:main',
        ],
    },
    test_suite='./test.TestPyglatin',
)
