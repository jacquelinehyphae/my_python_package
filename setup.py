from setuptools import setup, find_packages

setup(
  name='my_package',
  version='0.1.0',
  packages=find_packages(),
  install_requires=[
    'pandas>=1.1.0',
    'numpy>=1.19.5',
    'requests',
  ],
  author='jacquelinehyphae',
  author_email='jacqueline@hyphae.net',
  description='Testing python package hsoted on github',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/jacquelinehyphae/my_python_package',
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
  ],
)