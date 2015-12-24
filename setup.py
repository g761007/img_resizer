import os

from setuptools import setup, find_packages

import img_resizer

def read_requirements(filename):
    content = open(os.path.join(here, filename)).read()
    requirements = map(lambda r: r.strip(), content.splitlines())
    return requirements


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requirements = read_requirements('requirements.txt')

setup(
    name='img_resizer',
    version=img_resizer.__version__,
    description='resize 3x image to @1x and @2x for iOS App',
    long_description=README,
    author='Daniel Hsieh',
    author_email='a761007@gmail.com',
    url='https://github.com/g761007/img_resizer',
    license='MIT',
    packages = find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points = '''
        [console_scripts]
        img_resizer=img_resizer.resizer:resize
    ''',
)
