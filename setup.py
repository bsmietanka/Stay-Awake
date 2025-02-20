from setuptools import setup, find_packages

setup(
    name='stay-awake',
    version='0.1.0',
    description='Stay awake utility script',
    author='Bartek Śmietanka',
    author_email='bartek.smietanka@gmail.com',
    packages=find_packages(include=["stay_awake", 'stay_awake.*']),
    install_requires=[
        'pyautogui',
    ],
    entry_points={
        'console_scripts': ['stay-awake=stay_awake:main']
    }
)
