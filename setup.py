from distutils.core import setup

setup(
    name='IntelliParse',
    version='0.1.0',
    author='Danish Mujeeb',
    author_email='danish@dsharpapps.com',
    packages=['intelliparse', 'intelliparse.tests'],
    scripts=[],
    url='http://pypi.python.org/pypi/IntelliParse/',
    license='LICENSE.txt',
    description='A Python library to help parse product properties from simple English text',
    long_description=open('README.md').read(),
    install_requires=[],
)