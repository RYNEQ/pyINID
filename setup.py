from setuptools import setup
import os
import io

def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


setup(name='pyinid',
      version='0.3.1',
      description='Validate And Generate Iran National ID',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/RYNEQ/pyINID',
      author='Ariyan Eghbal (RYN)',
      author_email='ariyan.eghbal@gmail.com',
      license='GPLv2',
      packages=['inid'],
      zip_safe=False)

