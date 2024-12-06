from setuptools import setup, find_packages

setup( 
    name="crime_test", 
    version="1.0", 
    author="Devin Taing", 
    author_email="devin.taing@sjsu.edu", 
    packages=find_packages(), 
    description="A package to validate and process crime data",  
    url="https://github.com/gituser/test-tackage",  
    install_requires=['pandas'] 
)