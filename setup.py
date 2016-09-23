from setuptools import setup

setup(
    name='xlsxtocsv',
    version='1.0.0',
    author='Harald von Waldow',
    author_email='harald.vonwaldow@eawag.ch',
    packages=['xlsxtocsv'],
    url='https://github.com/eawag-rdm/xlsxtocsv.git',
    license='GNU Affero General Public License',
    description='Export from a .xlsx file to multiple .csv files',
    install_requires=['openpyxl'],
    entry_points={
        'console_scripts': ['xlsxtocsv.xlsxtocsv:main']
    }
)
