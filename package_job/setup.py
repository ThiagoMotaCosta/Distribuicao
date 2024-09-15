from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_job",
    version="0.0.1",
    author="Thiago_Mota.19-83",
    author_email="thimotacosta@gmail.com",
    description="trabalho de prática de pacotes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThiagoMotaCosta/package-template/tree/distribuicao"
    packages=find_packages(),
    install_requires=requirements,
)