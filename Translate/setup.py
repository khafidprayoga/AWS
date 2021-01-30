import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='translate',
    version='0.1',
    author='Khafid Prayoga',
    author_email='khafidlinux@gmail.com',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    install_requires=[
        'Click',
        'boto3',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        translate=translate:translate
    ''',
)