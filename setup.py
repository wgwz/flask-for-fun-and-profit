from setuptools import setup, find_packages

setup(
    name='myapp',
    version='0.1',
    description='code from armins talk, flask for fun and profit',
    packages=find_packages(),
    install_requires=[
        'flask'
    ]
)
