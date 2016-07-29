import setuptools import setup
from setuptools import find_packages


setup(
        name='bggpy',
        version='0.0.1',
        author='Jay Atkinson',
        author_email='jgatkinsn@gmail.com',
        maintainer='Jay Atkinson',
        maintainer_email='jgatkinsn@gmail.com',
        platforms='any',
        license='BSD',
        description='Set of python tools for accessing data from'
                     'Boardgamegeek',
        long_description=open('README.md').read(),
        install_requires=[
            'requests',
            'BeautifulSoup4'],
        )
