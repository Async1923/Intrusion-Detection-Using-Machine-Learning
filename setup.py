from setuptools import find_packages,setup
from typing import List

HYPEN_E='-e.'
def get_requirements(file_path:str)->List[str]:

    '''return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
    return requirements


setup(
    name='intrusion_detection',
    version='0.0.1',
    author='Harsh',
    author_email='harshsuman404@gmail.com',
    packages=find_packages(),

    install_requires=get_requirements('requirements.txt')
)