from setuptools import setup

setup(
    name='ConvertToLetterSize',
    version='0.1',
    py_modules=['convert'],
    install_requires=[
        'Click',
        'PyMuPDF',
    ],
    entry_points='''
        [console_scripts]
        converttolettersize=convert:convert_to_lettersize
    ''',
)
