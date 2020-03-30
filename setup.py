from setuptools import setup, find_packages

setup(
    name='bioconda_find_cli',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'click',
        'acclimatise',
        'ruamel.yaml==0.16.5',
    ],
    entry_points={
        "console_scripts": [
            'find_cli = bioconda_cli.main:main',
            # more script entry points ...
        ],
    }
)