from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    return requirements


setup(
    name='end_to_end_ml_project',
    version='1.0.0',
    author='nigamar',
    author_email='arpitnigam.manit14@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)
