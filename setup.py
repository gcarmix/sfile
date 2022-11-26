'''
setup.py
'''
import os
from setuptools import setup

def read(fname):
    '''
    Utility function to read the README file
    Used for the long_description.  It's nice, because now 1) we have a top level
    README file and 2) it's easier to type in the README file than to put a raw
    string in below ...
    '''
    return open(os.path.join(os.path.dirname(__file__), fname),encoding="utf-8").read()


setup(
  # METADATA...
  name = 'py-sfile',
  version = '0.1.0',
  url = 'https://github.com/gcarmix/sfile',
  download_url = "https://github.com/gcarmix/sfile/archive/master.zip",
  project_urls = {
    "Bug Tracker": "https://github.com/gcarmix/sfile/issues",
    "Documentation": "https://github.com/gcarmix/sfile/blob/master/README.md",
    "Source Code": "https://github.com/gcarmix/sfile.git",
  },
  author = 'gcarmix',
  author_email = 'carmixdev@gmail.com',
  maintainer = 'gcarmix',
  maintainer_email = 'carmixdev@gmail.com',
  description = 'sfile, cross platform file metadata analyzer',
  license = 'MIT',
  long_description = read('README.md'),
  long_description_content_type = 'text/markdown',
  platforms = ['LINUX', 'MAC', 'WINDOWS'],
  # OPTIONS...
  entry_points = {'console_scripts': ['sfile=sfile.sfile:main']},
  install_requires = ['importlib_resources','python-docx','Pillow','python-ffmpeg','pikepdf','openpyxl','pefile'],
  package_dir = {'sfile': 'src/sfile','libsfile':'src/sfile/libsfile','plugins':'src/sfile/libsfile/plugins'},
  packages = ['sfile','libsfile','plugins'],
)
