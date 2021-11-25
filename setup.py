from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgquery',
    version='0.0.1',
    description='remote psql database query',
    long_descript=readme,
    author='funfunpluto',
    author_email='funfunpluto@gmail.com',
    install_requires=['boto3'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts':[
            'pgquery=pgquery.cli:main',
            ]
        }
)
