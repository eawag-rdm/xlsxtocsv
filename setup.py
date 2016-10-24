from setuptools import setup

setup(
    name='xlsxtocsv',
    version='1.0.1',
    author='Harald von Waldow',
    author_email='harald.vonwaldow@eawag.ch',
    packages=['xlsxtocsv'],
    url='https://github.com/eawag-rdm/xlsxtocsv.git',
    license='GNU Affero General Public License',
    description='Export from a .xlsx file to multiple .csv files',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
    install_requires=['openpyxl>=2.4.0'],
    entry_points={
        'console_scripts': ['xlsxtocsv=xlsxtocsv.xlsxtocsv:main']
    }
)
