from setuptools import setup

setup(
    name='fpp',


    version='0.0.1',

    description='A sample Python project',

    url='https://github.com/faineance/fpp',

    author='faineance',
    author_email='faineance@users.noreply.github.com',

    license='MIT',
    classifiers=[

        'Development Status :: 3 - Alpha',


        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',


        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],



    packages=['fpp'],

    install_requires=['six'],

    extras_require={
        'dev': [],
        'test': ['coverage'],
    },


)