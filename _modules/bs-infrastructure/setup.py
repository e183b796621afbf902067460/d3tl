from setuptools import setup, find_packages


with open('README.md', 'r') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name="bs-infrastructure",
    version="0.0.3",
    author="e183b796621afbf902067460",
    author_email="606d18446a06fe9738fd@gmail.com",
    url="https://github.com/e183b796621afbf902067460/bs-thesis/tree/master/_modules/bs-infrastructure",
    packages=find_packages(
        exclude=['bs_infrastructure_tests*']
    ),
    long_description=long_description,
    install_requires=required
)