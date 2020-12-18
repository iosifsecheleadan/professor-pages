from setuptools import setup

setup(
    name='professor-pages',
    version='0.1.0',
    description='Console based application for creating Professor HTML Pages',
    url='https://github.com/iosifsecheleadan/professor-pages',
    author='Sechelea Iosif-Dan-Eugen',
    author_email='iosifsecheleadan@gmail.com',
    license='',  # todo add license
    packages=['src'],

    install_requires=[
        'commonmark'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ",  # todo ad license
        "Operating System :: OS Independent",
    ],
)
