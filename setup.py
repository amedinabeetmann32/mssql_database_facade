from setuptools import setup, find_packages

setup(
    name='mssql_database_facade',
    version='0.0.1',
    description='A package implement a facade fro acces to database mssql',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alan Medina',
    author_email='alan.medina@beetmann.com',
    url='https://github.com/tu_usuario/my_package',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        # Aquí las dependencias
    ],
)
