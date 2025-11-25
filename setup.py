#!/usr/bin/env python3
"""
Setup script for Audience Cleaner
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding='utf-8') if readme_file.exists() else ""

setup(
    name="audience-cleaner",
    version="1.0.0",
    description="A reliable tool to clean and transform large CSV files from Audience Lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    py_modules=["clean_audience"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "clean-audience=clean_audience:main",
            "audience-cleaner=clean_audience:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="csv cleaning audience lab data processing",
)

