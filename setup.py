from setuptools import setup, find_packages

setup(
    name='musictools',
    version='0.0.1',
    description='Lets you repair your music files by adding metadata and album art',
    url='https://github.com/lakshaykalbhor/musictools',
    author='Lakshay Kalbhor',
    author_email='lakshaykalbhor@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'colorama',
        'mutagen',
        'spotipy',
        'six',
        'requests',
        'configparser',
    ],
)