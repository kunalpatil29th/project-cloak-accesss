"""
Project Cloak Access Setup

Definition:
Setup Script - A Python script that installs the package and its dependencies, making it
available for import in other Python scripts.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="project-cloak-access",
    version="1.0.0",
    author="Kunal Patil",
    description="An educational Computer Vision project implementing an invisibility cloak effect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kunalpatil29th/project-cloak-accesss",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Image Recognition",
    ],
    python_requires=">=3.8",
    install_requires=[
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
        "Flask>=2.3.0",
    ],
)
