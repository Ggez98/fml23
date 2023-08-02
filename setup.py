from setuptools import setup, find_packages

setup(
    name='my_text_files',
    version='0.1',
    packages=find_packages(),
    package_data={
        'my_text_files': ['fml23/*'],
    },
)
