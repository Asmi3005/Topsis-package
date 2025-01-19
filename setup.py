from setuptools import setup, find_packages

setup(
    name='topsis-package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',  # List any dependencies here
    ],
    test_suite='tests',
    description='A Python implementation of the TOPSIS method for decision-making.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/topsis-package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
