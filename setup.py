from setuptools import setup

setup(
   name='pautils',
   version='0.0.8',
   description='Proxy Analytics Utils',
   author='Proxy Analytics Engineering',
   packages=setuptools.find_packages(),
   install_requires=[
      'python-json-logger==0.1.11',
   ]
)