'''
the setup.py file is an essential part of packaging and
distributing python projects.it is used by setuptools 
(or distutils in older python versions) to define the 
configuration of ypur project,such as metadata,dependencies and more

'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirements

    '''
    requirement_lst:List[str]=[]
    try:
        with open ('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirement_lst

print(get_requirements())


setup(

    name="NetworkSecurity",
    version="0.0.1",
    author="Jenie Mariam Chacko",
    author_email="jeniemariamtvl@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()#to make sure that all the packages should be installed

)