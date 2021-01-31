from setuptools import setup, find_packages


setup(
    name='npl_hate_speech_on_twitter',
    packages=find_packages(where='source'),
    package_dir={
        '': 'source',
    },
    description='',
    version='1.0.1',
    author='Gabriel Ramos',
    install_requires=[
        "matplotlib == 3.3.4",
        "nltk == 3.5",
        "numpy == 1.19.5",
        "pandas == 1.1.5",
        "scikit_learn == 0.24.1",
        "tweepy == 3.10.0",
    ],
)
