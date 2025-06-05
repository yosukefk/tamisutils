from setuptools import setup

setup(
        name='tamis_reader',
        version='1.0.0',
        description='tamis pipe delimted file',
        license='MIT',
        packages=['tamis_reader'],
        package_data={'tamis_reader': ['data/*.txt', 'data/*.csv']},
        install_requires=[
            'pandas>=1.0',
            ],
        )
