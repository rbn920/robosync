from setuptools import setup, find_packages
import robosync

setup(
    name='robosync',
    version=robosync.__version__,
    url='https://github.com/rbn920/robosync/',
    license='MIT',
    author='Robert Nelson',
    test_require=['unittest'],
    author_email='robertb.nelson@gmail.com',
    description='Sync with Python and robocopy',
    long_description='',
    packages=['robosync'],
    include_package_data=True,
    platforms='windows',
    test_suite='robosync.test.test_robosync',
    classifiers=['Programming Language :: Python',
                 'Development Status :: 3 - Alpha',
                 'Natural Language :: English',
                 'Intended Audience :: End Users/Desktop',
                 'License :: OSI Approved :: MIT',
                 'Environment :: Win32 (MS Windows)']
)
