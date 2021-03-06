#!/usr/bin/env python
"""The setup script."""

from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="aiophotoprism",
    version="0.1.0",
    author="Gleb Sinyavskiy",
    author_email="zhulik.gleb@gmail.com",
    description="Asynchronous Python client for the Photoprism REST API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zhulik/aiophotoprism",
    license="The MIT License",
    install_requires=["aiohttp==3.7.4", "yarl==1.6.3"],
    packages=["aiophotoprism"],
    package_dir={"aiophotoprism": "aiophotoprism"},
    include_package_data=True,
    zip_safe=True,
    keywords="photoprism,photo,api,aio,async,await",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Archiving :: Mirroring",
    ],
)
