import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="muzeek-sdk",
    version="1.0.0",
    author="Igal Cohen-Hadria",
    author_email="igal@muzeek.co",
    description="A framework library to access Muzeek API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muzeek-sdk/python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
