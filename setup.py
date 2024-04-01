"""
installation library.
"""
from setuptools import setup
from setuptools import find_packages


setup(
    name='payze-pkg',
    version='2.1',
    license='MIT',
    author="paytechuz",
    author_email='paytechuz@gmail.com',
    packages=find_packages('payze'),
    package_dir={'': 'payze'},
    url='https://github.com/PayTechUz/payze-pkg',
    keywords='payze-merchant payze-uz payze-pkg payze-python payze-github',
    install_requires=[
        'requests==2.*',
        'pydantic==2.4.2',
        'dataclasses==0.*',
    ],
)
