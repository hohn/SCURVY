from setuptools import setup
import glob

setup(name='scurvy',
      version='0.1',
      description='Overview of offerings',
      url='https://github.com/hohn/SCURVY',
      author='Michael Hohn',
      author_email='hohn@github.com',
      license='https://creativecommons.org/licenses/by-sa/4.0',
      packages=['scurvy'],
      install_requires=[],
      include_package_data=True,
      scripts=glob.glob("bin/sc-*"),
      zip_safe=False,
      python_requires='>=3.9'
      )
