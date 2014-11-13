from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'django-requests-panel',
  version = '0.2.0',
  author = 'Guillaume Thomas',
  author_email='guillaume.thomas642@gmail.com',
  license='LICENCE.txt',
  description='',
  url = 'https://github.com/gtnx/django-requests-panel',
  install_requires = map(lambda line:line.strip("\n"), open('requirements.txt', 'r').readlines()),
  include_package_data = True,
  packages = find_packages(),
  )
