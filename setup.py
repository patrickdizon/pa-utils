from setuptools import setup

setup(
   name='pa-utils',
   version='0.0.1',
   description='Proxy Analytics Utils',
   author='Proxy Analytics Engineering',
   packages=setuptools.find_packages(),
   install_requires=[
      'python-json-logger==0.1.11',
   ]
)