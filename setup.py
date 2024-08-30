from setuptools import setup, find_packages

setup(
    name='my_ai_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my_ai_project = src.__main__:main'
        ]
    },
)