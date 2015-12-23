from setuptools import setup, find_packages


setup(
    name='img_resizer',
    version='0.0.0',
    description='resize 3x image to @1x and @2x for iOS App',
    author='Daniel Hsieh',
    author_email='a761007@gmail.com',
    packages = find_packages(),
    entry_points = '''
        [console_scripts]
        img_resizer=img_resizer.resizer:resize
    ''',
)
