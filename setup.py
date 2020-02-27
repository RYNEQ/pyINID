from setuptools import setup, Extension
import os
import io

def read(*parts):
    filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts)

    with io.open(filename, encoding='utf-8', mode='rt') as fp:
        return fp.read()


setup(name='pyinid',
      version='0.4.4',
      description='Validate And Generate Iran National ID',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/RYNEQ/pyINID',
      author='Ariyan Eghbal (RYN)',
      author_email='ariyan.eghbal@gmail.com',
      license='GPLv2',
      packages=['inid'],
      keywords = ['nid', 'national id', 'NationalID', 'iran', 'ssn', 'social security number'],
      zip_safe=False,
      classifiers=[
        'Development Status :: 4 - Beta',      
        'Intended Audience :: Developers',     
        'Intended Audience :: Science/Research', 
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',   
        'Programming Language :: Python :: 3.6',
  ],

)

