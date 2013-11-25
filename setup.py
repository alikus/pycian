from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='pycian',
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires,
    author='Albert Tugushev',
    author_email='albert@tugushev.ru',
    url='http://github.com/alikus/pycian',
    description='E-mail notifications of new flats from www.cian.ru',
    platforms='any',
    test_suite='tests',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
