from setuptools import setup


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='GBM Auto Benchmark',
    version='0.1',
    install_requires=requirements
)
