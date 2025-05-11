
from setuptools import setup, find_packages

setup(
    name="probctrl",
    version="0.1.0",
    description="A lightweight Python decorator toolkit for probabilistic, delayed, and throttled execution.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/probctrl",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
)
